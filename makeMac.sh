rm -r  output/mac  
rm -rf dist
rm -rf build


#py2applet --make-setup ct.py
#python setup.py py2app --iconfile ct.icns
pyinstaller ct.py --windowed  --onefile --icon ct.icns
tar -czf dist/ct.app.tar.gz   dist/ct.app



 

