## Local Setup

### Create a virtual environment:

```
python -m venv venv
```

### Activate

> Windows

```
venv\Scripts\activate
```

> MacOS

```
source venv/bin/activate
```

### Deactivate

> Windows and Mac

```
deactivate
```

## Local Setup

```
python3 -m pip install --upgrade pip
pip install mkdocs mkdocs-material mkdocs-gen-nav-plugin mkdocs-awesome-pages-plugin
chmod +x ./generate_docs.sh
./generate_docs.sh
mkdocs serve
```