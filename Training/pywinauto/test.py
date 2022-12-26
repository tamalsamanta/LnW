from pywinauto import Desktop, application
from subprocess import Popen
from time import sleep


Popen("code", shell=True)
sleep(5)
app = Desktop().window(title_re = 'Get Started')
app.draw_outline()
print(app.window_text())
app.type_keys("^O")
