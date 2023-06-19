from tkinter import *
from tkinter import messagebox
import pymysql
import home_page
import login_page

def openskate():
    openskate_window = Tk()
    openskate_window.geometry("1920x1080")
    openskate_window.title("Open Skate")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    openskate_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=0,column=9)