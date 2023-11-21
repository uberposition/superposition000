# Create Python App

- Install PyInstaller via pip if not already installed

```bash
pip install PyInstaller
```

- Navigate to your project directory
- Create a virtual environment and install your project's dependencies.

```bash
python3 -m venv myenv
source myenv/bin/activate
```

- Run PyInstaller with the appropriate flags to bundle the app and dependencies.
- Test the bundled app to ensure it works as expected.
- Might need to run the following command:

```bash
conda remove pathlib
```

- Wrap the script using the following command:

```bash
pyinstaller --onefile scriptName.py
```
