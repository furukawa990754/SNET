@echo off
cd ./ 
pyinstaller "VM manager.spec" --onefile --noconsole -i ifs.ico
pause