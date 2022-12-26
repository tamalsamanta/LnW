from pywinauto import application
app = application.Application()
app.start("notepad.exe")
app.UntitledNotepad.type_keys("A quick brown fox jumps over the lazy dog", with_spaces= True)
# app.UntitledNotepad.type_keys("^S") // save - ^ctrl
# app.UntitledNotepad.type_keys("%FX") // quit - %alt
app.UntitledNotepad.menu_select("File -> Exit")
app.Notepad.DontSave.click()
