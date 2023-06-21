import login_page
import openskate
import my_account
import ice_calendar
from tkinter import *

def open_home_screen_without_user_logged_in():
    home_window = Tk()
    home_window.geometry("1920x1080")
    home_window.title("On Ice Skating v0.00.0013")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    home_window.iconphoto(True, ShoeIcon)
    def open_user_login():
        home_window.destroy()
        login_page.user_login()
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(home_window,height=1,width=21).grid(row=0,column=9)
    empty_grid = Label(home_window,height=1,width=21).grid(row=1,column=0)
    def unlogged_home_screen_to_unlogged_openskate():
        home_window.destroy()
        openskate.open_openskate_window_without_log_in()
    open_openskate_window_button = Button(home_window,text="Open Skate",width=15,font=('Arial',12),command=unlogged_home_screen_to_unlogged_openskate).grid(row=1,column=1)
    def open_calendar():
        home_window.destroy()
        ice_calendar.open_ice_calendar_not_logged_in()
    open_calendar_button = Button(home_window,text="Event Calendar",width=15,font=('Arial',12),command=open_calendar).grid(row=1,column=2)
    meet_the_team_dropdown = Label(home_window,text="Meet the team",font=('Arial',12)).grid(row=1,column=3)
    amenities_dropdown = Label(home_window,text="Amenities",font=('Arial',12)).grid(row=1,column=4)
    about_community_dropdown = Label(home_window,text='About/Community',font=('Arial',12)).grid(row=1,column=5)
    login_button = Button(home_window,text='Sign In',width=15,font=('Arial',12),command=open_user_login).grid(row=1,column=9)
    #empty_space = Label(home_window,text = "").pack() cannot use geometry manager pack inside . which already has slaves managed by grid
    home_window.mainloop()

def open_home_screen_with_user_logged_in():
    logged_window = Tk()
    logged_window.geometry("1920x1080")
    logged_window.title("On Ice Skating v0.00.0013")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    logged_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=0,column=9)
    empty_grid = Label(logged_window,height=1,width=21).grid(row=1,column=0)
    def logged_home_screen_to_logged_open_skate():
        logged_window.destroy()
        openskate.open_openskate_window_with_log_in()
    open_openskate_window_button = Button(logged_window,text="Open Skate",width=15,font=('Arial',12),command=logged_home_screen_to_logged_open_skate).grid(row=1,column=1)
    def open_calendar_not_logged_in():
        logged_window.destroy()
        ice_calendar.open_ice_calendar_logged_in()
    open_calendar_button = Button(logged_window,text="Event Calendar",width=15,font=('Arial',12),command=open_calendar_not_logged_in).grid(row=1,column=2)
    meet_the_team_dropdown = Label(logged_window,text="Meet the team",font=('Arial',12)).grid(row=1,column=3)
    amenities_dropdown = Label(logged_window,text="Amenities",font=('Arial',12)).grid(row=1,column=4)
    about_community_dropdown = Label(logged_window,text='About/Community',font=('Arial',12)).grid(row=1,column=5)
    def sign_out():
        logged_window.destroy()
        open_home_screen_without_user_logged_in()
        #my_account.open_my_account()
    my_account_button = Button(logged_window,text='Sign Out',width=15,font=('Arial',12),command=sign_out).grid(row=1,column=9)