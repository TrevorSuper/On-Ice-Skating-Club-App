from tkinter import Tk, Canvas
from framework_page import frame_gui
from homepage_buttons import buttonpack




root = Tk()

#Brings from the basic page everyone has
canvas = frame_gui(root)
#Components needed for homepage
components = buttonpack(canvas)
#main single window running
root.mainloop()
