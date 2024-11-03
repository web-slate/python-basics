#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status.

# Define the root directory of your Python source files
ROOT_DIR="src"

# Define the output directory for Markdown files
OUTPUT_DIR="docs"

# Clean up any existing __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Create the main index.md for the docs folder
cat <<EOF > "$OUTPUT_DIR/index.md"
# Webslate - Python Basics

Welcome to the Webslate documentation for Python Basics.

## Table of Contents
EOF

# Function to process each directory
process_directory() {
    local dir="$1"
    local relative_path="${dir#$ROOT_DIR/}"
    local output_dir="$OUTPUT_DIR/$relative_path"

    # Skip __pycache__ directories and the root source directory itself
    if [[ "$dir" == "$ROOT_DIR" ]] || [[ "$(basename "$dir")" == "__pycache__" ]]; then
        return
    fi

    # Remove trailing slashes to prevent double slashes in paths
    output_dir="${output_dir%/}"

    # Create the output directory if it doesn't exist
    mkdir -p "$output_dir"

    # Create or merge an index.md for the current directory
    local md_file="$output_dir/index.md"

    # Function to convert underscore_case to Title Case
    convert_to_title_case() {
        echo "$1" | sed -E 's/_/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); print}'
    }

    # Start with the title and basic content
    echo "# $(convert_to_title_case "$(basename "$dir")")" > "$md_file"
    echo "" >> "$md_file"
    echo "This section covers $(basename "$dir")." >> "$md_file"
    echo "" >> "$md_file"

    # Check if the index.md already exists in the source and merge with existing content
    if [[ -f "$dir/index.md" ]]; then
        echo "Merging content from existing $dir/index.md into $md_file"
        cat "$dir/index.md" >> "$md_file"
        echo "" >> "$md_file"
    fi

    # Flag to track if any Python files were found
    local python_found=false

    # Add links to index.md for each .py file in the directory
    for py_file in "$dir"/*.py; do
        if [[ -f "$py_file" ]]; then
            # Skip __init__.py files
            if [[ "$(basename "$py_file")" == "__init__.py" ]]; then
                continue
            fi
            
            local file_name=$(basename "$py_file")
            local link_name="${file_name%.py}.md"  # Change extension to .md
            
            # Extract docstring comments from the Python file
            # This handles both triple single and double quotes
            local comments=$(awk '/^[[:space:]]*"""/{p=1;next}/"""{0,1}$/{if(p){p=0}};p' "$py_file" \
                           || awk "/^[[:space:]]*'''{/p=1;next}/'''{0,1}$/{if(p){p=0}};p" "$py_file")

            # Create a Markdown file for this Python file with syntax highlighting and comments
            {
                echo "> File Name: $file_name"
                echo '```python'
                cat "$py_file"  # Include the full Python code
                echo '```'
                echo ""  # Add an empty line before comments
                
                # Append extracted docstring comments at the bottom
                if [[ -n "$comments" ]]; then
                    echo "## Documentation"
                    echo "$comments"
                fi
            } > "$output_dir/$link_name"

            echo "Markdown file created: $output_dir/$link_name"

            python_found=true
            
            # Add link to index.md for this Python file's documentation
            echo "- [$file_name](./$link_name)" >> "$md_file"
        fi
    done

    # Only create index.md if Python files were found
    if ! $python_found; then
        rm "$md_file"  # Remove the empty index file
        echo "No Python files found in $dir, removed empty index.md"
    fi

    # Recursively process subdirectories, skipping __pycache__
    for subdir in "$dir"/*/; do
        if [[ -d "$subdir" ]] && [[ "$(basename "$subdir")" != "__pycache__" ]]; then
            process_directory "$subdir"
            
            # Check if the subdirectory has any Python files before adding a link
            if compgen -G "$subdir/*.py" > /dev/null || [[ -f "$subdir/index.md" ]]; then
                local subdir_name=$(basename "$subdir")
                echo "- [$subdir_name](./$subdir_name/index.html)" >> "$md_file"
            fi
        fi
    done

    # Copy existing .md files (like intro.md) to the output directory, excluding index.md
    for existing_md in "$dir"/*.md; do
        if [[ -f "$existing_md" && "$(basename "$existing_md")" != "index.md" ]]; then
            cp "$existing_md" "$output_dir/"
            echo "Copied existing Markdown file: $output_dir/$(basename "$existing_md")"
        fi
    done

    # Add link to the main docs/index.md, linking to index.html
    if [[ -n "$relative_path" ]]; then  # Check if relative_path is not empty
        local dir_name=$(basename "$dir")
        echo "- [$dir_name](./$relative_path/index.html)" >> "$OUTPUT_DIR/index.md"
    fi
}

# Start processing from the root directory
for dir in $ROOT_DIR/*; do 
    if [[ -d $dir ]] && [[ "$(basename "$dir")" != "__pycache__" ]]; then 
        process_directory "$dir"
    fi 
done

# Create the mkdocs.yml file outside the docs directory with theme settings
cat <<EOF > mkdocs.yml
site_name: 'Webslate - Python Basics'
site_url: 'https://web-slate.github.io/python-basics/'
theme:
  name: material
  features:
    - navigation.sections
    - navigation.footer
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy

plugins:
  - search
  - gen_nav:
      enabled: true
  - mkdocstrings:
      default_handler: python
      handlers:
        python:
          paths: [src]  # Path to your Python source files
          options:
            show_source: true

markdown_extensions:
  - pymdownx.highlight:
      use_pygments: true
      linenums: true
  - pymdownx.superfences

nav:
  - Basics: basics/introduction.md
  - Data Types: data_types/introduction.md
  - Methods: basics/methods/introduction.md
  - Recursions: basics/recursions/introduction.md
  - Data Structures: data_structures/introduction.md
  - OOPs: oops/introduction.md
  - Algorithms: algorithms/introduction.md
  - Leet Code: leet_code/introduction.md
EOF

echo "Documentation generation complete. Generated mkdocs.yml for MkDocs."