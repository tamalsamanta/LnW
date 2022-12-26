from pywinauto import Application

app = Application().connect(process= 6136) #current dynamic first instance of vscode
dlg = app.window()
# dlg.wrapper_object().minimize()
dlg.wrapper_object().type_keys("^+P") #opens command palette
