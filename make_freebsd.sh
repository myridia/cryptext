rm -r  output/mac  
rm -rf dist
rm -rf build

pyinstaller ct.py --onefile -w --icon=./ct.ico -n ct_freebsd 
#mv dist/ct ct_freebsd






 

