from tkinter import *
from tkinter import messagebox
import pymysql
import home_page
import login_page

def open_openskate_window_without_log_in():
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
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=4,column=0)
    openskate_title = Label(openskate_window,text='Open Skate',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)

    # how to do a tkinter dropdown menu example
    choose_rink_instruction = Label(openskate_window,text='Choose Skating Rink:',font=('Arial',12)).grid(row=3,column=4)
    choose_rink_var = StringVar()
    choose_rink_dropdown = OptionMenu(openskate_window,choose_rink_var,"Rink A","Rink B","Rink C")
    choose_rink_dropdown.grid(row=3,column=5)
    rink_entry_box = Entry(openskate_window,textvariable=choose_rink_var,font=('Arial',12),state='readonly')
    rink_entry_box.place(x=4000,y=5000) # this entry is for seeing the string in the box as it may be different from what is in the dropdown menu and cause errors
    # first set the box to be visible on screen for testing
    # once completed, place this entry box out of view of the window for example set x=4000,y=5000
    def attempt_to_reserve_skate_time_when_user_is_not_logged_in():
        if rink_entry_box.get()=='':
            messagebox.showerror('Error','Choose a skating rink')
        elif rink_entry_box.get()=='Rink A':
            messagebox.showerror('Error','You must be logged in to an account to register for an event.')
            openskate_window.destroy()
            login_page.user_login_then_redirect_to_openskate_logged_in()
        elif rink_entry_box.get()=='Rink B':
            messagebox.showerror('Error','You must be logged in to an account to register for an event.')
            openskate_window.destroy()
            login_page.user_login_then_redirect_to_openskate_logged_in()
        elif rink_entry_box.get()=='Rink C':
            messagebox.showerror('Error','You must be logged in to an account to register for an event.')
            openskate_window.destroy()
            login_page.user_login_then_redirect_to_openskate_logged_in()
    reserve_skate_time_button = Button(openskate_window,text='Reserve Open Skate Time',font=('Arial',12),command=attempt_to_reserve_skate_time_when_user_is_not_logged_in).grid(row=4,column=4,columnspan=2)
    # end of tkinter dropdown menu example

def open_rinkA_window():
    rinkA_window = Tk()
    rinkA_window.geometry("1920x1080")
    rinkA_window.title("Rink A Open Skate Schedule")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    rinkA_window.iconphoto(True, ShoeIcon)

def open_rinkB_window():
    rinkB_window = Tk()
    rinkB_window.geometry("1920x1080")
    rinkB_window.title("Rink B Open Skate Schedule")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    rinkB_window.iconphoto(True, ShoeIcon)

def open_rinkC_window():
    rinkC_window = Tk()
    rinkC_window.geometry("1920x1080")
    rinkC_window.title("Rink C Open Skate Schedule")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    rinkC_window.iconphoto(True, ShoeIcon)

def open_openskate_window_with_log_in():
    openskate_window = Tk()
    openskate_window.geometry("1920x1080")
    openskate_window.title("Logged Open Skate")
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
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=4,column=0)
    openskate_title = Label(openskate_window,text='Open Skate',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)

    # how to do a tkinter dropdown menu example
    choose_rink_instruction = Label(openskate_window,text='Choose Skating Rink:',font=('Arial',12)).grid(row=3,column=4)
    choose_rink_var = StringVar()
    choose_rink_dropdown = OptionMenu(openskate_window,choose_rink_var,"Rink A","Rink B","Rink C")
    choose_rink_dropdown.grid(row=3,column=5)
    rink_entry_box = Entry(openskate_window,textvariable=choose_rink_var,font=('Arial',12),state='readonly')
    rink_entry_box.place(x=4000,y=5000) # this entry is for seeing the string in the box as it may be different from what is in the dropdown menu and cause errors
    # first set the box to be visible on screen for testing
    # once completed, place this entry box out of view of the window for example set x=4000,y=5000
    def reserve_skate_time():
        if rink_entry_box.get()=='':
            messagebox.showerror('Error','Choose a skating rink')
        elif rink_entry_box.get()=='Rink A':
            openskate_window.destroy()
            open_rinkA_window()
        elif rink_entry_box.get()=='Rink B':
            openskate_window.destroy()
            open_rinkB_window()
        elif rink_entry_box.get()=='Rink C':
            openskate_window.destroy()
            open_rinkC_window()
    reserve_skate_time_button = Button(openskate_window,text='Reserve Open Skate Time',font=('Arial',12),command=reserve_skate_time).grid(row=4,column=4,columnspan=2)
    # end of tkinter dropdown menu example