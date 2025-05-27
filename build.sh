#!/bin/sh
#rm dist build -Rf

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo $OSTYPE
    pyinstaller ct.spec --onefile -w --path env/lib/site-packages --name=ct_linux --icon=./ct.ico --hidden-import=tkinter -y
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo $OSTYPE
    pyinstaller ct.py --onefile -w --path env/lib/site-packages --name=ct_macos --icon=./ct.ico 
elif [[ "$OSTYPE" == "cygwin" ]]; then
    pyinstaller ct.py --onefile --path env/lib/site-packages --name=ct_cygwin  --icon=./ct.ico 
elif [[ "$OSTYPE" == "msys" ]]; then
    echo $OSTYPE
        pyinstaller ct.py --onefile -w --path env/lib/site-packages --name=ct_win64 --icon=./ct.ico 
elif [[ "$OSTYPE" == "win32" ]]; then
    echo $OSTYPE
    pyinstaller ct.py --onefile -w --path env/lib/site-packages --name=ct_win32 --icon=./ct.ico 
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    echo $OSTYPE
    pyinstaller ct.py --onefile -w --path env/lib/site-packages --name=ct_freebsd --icon=./ct.ico 
else
    echo $OSTYPE
    pyinstaller ct.py --onefile -w --path env/lib/site-packages --name=ct_linux  --icon=./ct.ico 
fi






