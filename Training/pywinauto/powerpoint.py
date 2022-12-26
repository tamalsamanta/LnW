from pywinauto.application import Application

app = Application(backend='uia').start(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.exe", timeout = 10)

app.window(title_re = ".*PowerPoint*.").wait('ready visible', timeout=10, retry_interval=1)
main = app.window(title_re = ".*PowerPoint*.")
main.wrapper_object().maximize()

main.child_window(title = "New", control_type = "ListItem").click_input()
main.child_window(title = "Blank Presentation", control_type = "ListItem").click_input()
