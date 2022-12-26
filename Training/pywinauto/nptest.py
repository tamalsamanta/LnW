from pywinauto import application, mouse, keyboard
from time import sleep

# C:\Users\tamal_samanta\Desktop\LnW\Training
f = open(r"C:\Users\tamal_samanta\Desktop\LnW\Training\pywinauto\source.py")
np = application.Application()
np.start("notepad.exe")
for x in f:
    for xx in x:
        if xx in ['(', ')', '{', '}', '[', ']', '^', '%']:
            np.UntitledNotepad.type_keys("{"+xx+"}", with_spaces = True)
        else:
            np.UntitledNotepad.type_keys(xx, with_spaces = True)
    np.UntitledNotepad.type_keys("{ENTER}")

np.UntitledNotepad.menu_select("File -> Save")
np.SaveAs.ComboBox1.type_keys('testfile.py')
np.SaveAs.ComboBox2.select(1)
np.SaveAs.Save.click()
np.UntitledNotepad.type_keys("%FX")

sleep(5)

exp = application.Application()
exp.connect(title_re=".*Visual Studio Code")
exp.top_window().set_focus()

# mouse.click(button='left', coords=(200,450))
# mouse.click(button='left', coords=(1785, 75))

keyboard.send_keys("{RWIN}")
sleep(3)
keyboard.send_keys("cmd")
sleep(3)
keyboard.send_keys("{ENTER}")
sleep(3)
keyboard.send_keys(r'cd "C:\Users\tamal_samanta\Desktop\LnW\Training\pywinauto"', with_spaces=True)
keyboard.send_keys("{ENTER}")
sleep(3)
keyboard.send_keys("py testfile.py", with_spaces=True)
keyboard.send_keys("{ENTER}")