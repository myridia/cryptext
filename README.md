# cryptext
Basic Text Editor what saves it content as encrypted text 

# Requirements
* OS with Python installed
* python3.13 -m venv env 
* source env/bin/activate
* pip install -r requirements.txt
* create64linux.sh or run : pyinstaller ct.py --onefile -w --icon=./ct.ico 


# debian:
```
apt-get install build-essential libssl-dev swig python3-dev python3-tk
```
# arch:
```
pacman -S extra/swig
```

# run the app 
```
python ct.py
