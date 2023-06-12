from tkinter import Tk, Canvas, ttk
from tkinter import *
from framework_page import frame_gui
from homepage_buttons import buttonpack




root = Tk()
root.geometry("1920x1080")
root.title("On Ice Skating")
ShoeIcon = PhotoImage(file='src/img/Skating_Shoe_Icon.png')
root.iconphoto(True, ShoeIcon)
#Brings from the basic page everyone has
canvas = frame_gui(root)
#Components needed for homepage
components = buttonpack(canvas)
#main single window running
root.mainloop()
