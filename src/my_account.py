import home_page
import openskate
from tkinter import *

def open_my_account():
    my_account_window = Tk()
    my_account_window.geometry("1920x1080")
    my_account_window.title("My Account")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    my_account_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=0,column=9)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=4,column=0)
    empty_grid = Label(my_account_window,height=1,width=21).grid(row=5,column=0)
    my_account_title = Label(my_account_window,font=('Arial Bold',18),text='My Account').grid(row=1,column=4,rowspan=2,columnspan=2)
    def sign_out():
        my_account_window.destroy()
        home_page.open_home_screen_without_user_logged_in()
    sign_out_button = Button(my_account_window,font=('Arial',12),text='Sign Out',command=sign_out).grid(row=3,column=4,columnspan=2)