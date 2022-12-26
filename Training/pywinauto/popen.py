from subprocess import Popen
from pywinauto import Desktop

Popen('calc.exe', shell=True)
exe = Desktop(backend='uia').Calculator
exe.wait('visible')