import time
from pywinauto.application import Application

exe = Application(backend='uia').start('notepad.exe')
app = exe.untitlednotepad
app.type_keys('hello world', with_spaces=True)
time.sleep(3)
app.menu_select("File -> Exit")
app.notepad.dontsave.click()
