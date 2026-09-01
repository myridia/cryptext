# AGENTS.md — cryptext

## What this is
A basic text editor that saves content as encrypted text. Python + Tkinter desktop GUI app.

## Stack
- Python 3.13
- Tkinter (GUI)
- m2secret / cryptography (encryption)
- Pillow (image support)
- PyInstaller (build to binary)

## Build
```bash
python3.13 -m venv env
source env/bin/activate
pip install -r requirements.txt
pyinstaller ct.py --onefile -w --icon=./ct.ico
```

## Run
```bash
python ct.py
```

## Structure
- `ct.py` — main GUI application
- `requirements.txt` — Python dependencies
- `ct.ico` / `ct.icns` — app icons
- `build.sh` / `make_*.sh` — build scripts per platform

## Conventions
- No comments in code unless asked.
- Verify: `python -m py_compile ct.py`
