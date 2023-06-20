import home_page
import openskate
from tkinter import *

def open_my_account():
    my_account_window = Tk()
    my_account_window.geometry("1920x1080")
    my_account_window.title("My Account")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    my_account_window.iconphoto(True, ShoeIcon)