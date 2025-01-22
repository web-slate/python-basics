## Local Setup

### Create a virtual environment:

```
python -m venv venv
```

### Activate

> Windows


```
source venv/scripts/activate
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
python -m pip install --upgrade pip
pip install stylepy mkdocs mkdocs-material mkdocs-gen-nav-plugin mkdocs-awesome-pages-plugin pymdown-extensions mkdocstrings
chmod +x ./generate_docs.sh
./generate_docs.sh
mkdocs serve
```