# opencode-back

OpenCode API: Python API with FastAPI

## opencode-back setup.

Create python virtual environment:

```console
$ py -m venv .venv
```

Activate python virtual environment:

```console
$ .venv\scripts\activate
```

Update pip package installer

```console
$ pip3 install --upgrade pip
```

Add the following requirements to "requirements.txt" file:

- fastapi[standard]

Install the requirements:

```console
$ python -m pip install -r requirements.txt
```

Start the FastAPI server

```console
$ fastapi dev main.py
```

Install SQLite VSCode extension. After installing it run in VSCode search bar. SQLITE EXPLORER will be opened inside the VSCode file explorer.

```console
>SQLite: Open Database
```
