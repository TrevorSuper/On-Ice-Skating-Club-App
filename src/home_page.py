from tkinter import *
from tkinter import ttk
import login_page

def home_screen():
    home_window = Tk()
    home_window.geometry("1920x1080")
    home_window.title("On Ice Skating")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    home_window.iconphoto(True, ShoeIcon)
    def open_user_login():
        home_window.destroy()
        login_page.user_login()
    #keep everything above this line and keep home_window.mainloop() below this line
    #keep the login button
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=0,column=0)
    empty_grid = Label(home_window,height=1,width=21,background='blue').grid(row=0,column=1)
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=0,column=2)
    empty_grid = Label(home_window,height=1,width=21,background='blue').grid(row=0,column=3)
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=0,column=4)
    empty_grid = Label(home_window,height=1,width=21,background='blue').grid(row=0,column=5)
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=0,column=6)
    empty_grid = Label(home_window,height=1,width=21,background='blue').grid(row=0,column=7)
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=0,column=8)
    empty_grid = Label(home_window,height=1,width=21,background='grey').grid(row=0,column=9)
    empty_grid = Label(home_window,height=1,width=21,background='red').grid(row=1,column=0)
    events_dropdown = Label(home_window,text="Events",font=('Arial',12)).grid(row=1,column=1)
    membership_dropdown = Label(home_window,text="Membership",font=('Arial',12)).grid(row=1,column=2)
    meet_the_team_dropdown = Label(home_window,text="Meet the team",font=('Arial',12)).grid(row=1,column=3)
    amenities_dropdown = Label(home_window,text="Amenities",font=('Arial',12)).grid(row=1,column=4)
    about_community_dropdown = Label(home_window,text='About/Community',font=('Arial',12)).grid(row=1,column=5)
    login_button = Button(home_window,text='Login',width=15,font=('Arial',12),command=open_user_login).grid(row=1,column=9)
    #empty_space = Label(home_window,text = "").pack() cannot use geometry manager pack inside . which already has slaves managed by grid
    home_window.mainloop()
