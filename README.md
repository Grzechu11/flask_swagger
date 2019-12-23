# Flask sample project

This is sample project to host Flask with Visual Studio Code debugger

## Thanks

- [Tutorial]('https://code.tutsplus.com/pl/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972')
- [Docs]('https://python101.readthedocs.io/pl/latest/webflask/')
- [Visual Studio Code Tutorial]('https://code.visualstudio.com/docs/python/tutorial-flask')

## Useful commands

### Python

- check Python version

```powershell
python --version
```

- update pip

```powershell
python -m pip install --upgrade pip
```

- instal requirements

```powershell
pip install -r [FILE_NAME]
```

- - examples

```powershell
pip install -r requirements.txt
```

- add virtual enviroment

```powershell
py -m venv env
```

- activate virtual enviroment

```powershell
.\env\Scripts\activate
```

- deactivate virtual enviroment

```powershell
deactivate
```

- check virtual enviroment

```powershell
where python
```

### Visual Studio Code

- Python: Select Interpreter

```code
Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter.
Select virtual environment. `./env/...` or `.\env\...`
```
