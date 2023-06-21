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
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=5,column=0)
    openskate_title = Label(openskate_window,text='Open Skate',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)
    def openskate_without_login_to_home_page_without_login():
        openskate_window.destroy()
        home_page.open_home_screen_without_user_logged_in()
    openskate_without_login_to_home_page_without_login_button = Button(openskate_window,font=('Arial',12),text='Go to home page',command=openskate_without_login_to_home_page_without_login).grid(row=0,column=0)
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
    reserve_skate_time_button = Button(openskate_window,text='Reserve Open Skate Time',font=('Arial',12),command=attempt_to_reserve_skate_time_when_user_is_not_logged_in).grid(row=5,column=4,columnspan=2)
    # end of tkinter dropdown menu example

def open_rinkA_window():
    rinkA_window = Tk()
    rinkA_window.geometry("1920x1080")
    rinkA_window.title("Rink A Open Skate Schedule")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    rinkA_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(rinkA_window,height=1,width=13,background='green',text='0').grid(row=0,column=0)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='1').grid(row=0,column=1)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='2').grid(row=0,column=2)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='3').grid(row=0,column=3)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='4').grid(row=0,column=4)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='5').grid(row=0,column=5)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='6').grid(row=0,column=6)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='7').grid(row=0,column=7)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='8').grid(row=0,column=8)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='9').grid(row=0,column=9)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='10').grid(row=0,column=10)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='11').grid(row=0,column=11)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='12').grid(row=0,column=12)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='13').grid(row=0,column=13)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='14').grid(row=0,column=14)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='15').grid(row=0,column=15)
    empty_grid = Label(rinkA_window,height=1,width=11,background='green',text='16').grid(row=0,column=16)
    empty_grid = Label(rinkA_window,height=1,width=11,background='red',text='17').grid(row=0,column=17)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='1').grid(row=1,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='2').grid(row=2,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='3').grid(row=3,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='4').grid(row=4,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='5').grid(row=5,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='6').grid(row=6,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='7').grid(row=7,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='8').grid(row=8,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='9').grid(row=9,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='10').grid(row=10,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='red',text='11').grid(row=11,column=0)
    empty_grid = Label(rinkA_window,height=3,width=13,background='green',text='12').grid(row=12,column=0)
    def rinkA_to_openskate_with_login():
        rinkA_window.destroy()
        open_openskate_window_with_log_in()
    rinkA_to_openskate_with_login_button = Button(rinkA_window,height=1,width=13,font=('Arial',12),text='Previous Page',command=rinkA_to_openskate_with_login).grid(row=0,column=0)
    rinkA_title = Label(rinkA_window,text='Reserve your skating time in chunks of 30 minutes',font=('Arial Bold',16)).grid(row=1,column=4,columnspan=10)
    rinkA_date = Label(rinkA_window,text='Friday June 23, 2023',font=('Arial',15)).grid(row=2,column=4,columnspan=10)
    def attempt_reserve_openskate_time():
        if(var_800_830.get()==1):
            print('You Registered for 8:00AM-8:30AM')
        if(var_830_900.get()==1):
            print('You Registered for 8:30AM-9:00AM')
        if(var_900_930.get()==1):
            print('You Registered for 9:00AM-9:30AM')
        if(var_930_1000.get()==1):
            print('You Registered for 9:30AM-10:00AM')
        if(var_1000_1030.get()==1):
            print('You Registered for 10:00AM-10:30AM')
        if(var_1030_1100.get()==1):
            print('You Registered for 10:30AM-11:00AM')
        if(var_1100_1130.get()==1):
            print('You Registered for 11:00AM-11:30AM')
        if(var_1130_1200.get()==1):
            print('You Registered for 11:30AM-12:00PM')
        if(var_1200_1230.get()==1):
            print('You Registered for 12:00PM-12:30PM')
        if(var_1230_100.get()==1):
            print('You Registered for 12:30PM-1:00PM')
        if(var_100_130.get()==1):
            print('You Registered for 1:00PM-1:30PM')
        if(var_130_200.get()==1):
            print('You Registered for 1:30PM-2:00PM')
        if(var_200_230.get()==1):
            print('You Registered for 2:00PM-2:30PM')
        if(var_230_300.get()==1):
            print('You Registered for 2:30PM-3:00PM')
        if(var_300_330.get()==1):
            print('You Registered for 3:00PM-3:30PM')
        if(var_330_400.get()==1):
            print('You Registered for 3:30PM-4:00PM')

    var_800_830 = IntVar()
    var_830_900 = IntVar()
    var_900_930 = IntVar()
    var_930_1000 = IntVar()
    var_1000_1030 = IntVar()
    var_1030_1100 = IntVar()
    var_1100_1130 = IntVar()
    var_1130_1200 = IntVar()
    var_1200_1230 = IntVar()
    var_1230_100 = IntVar()
    var_100_130 = IntVar()
    var_130_200 = IntVar()
    var_200_230 = IntVar()
    var_230_300 = IntVar()
    var_300_330 = IntVar()
    var_330_400 = IntVar()
    time_800_830_AM = Checkbutton(rinkA_window,text='8:00AM-8:30AM',font=('Arial',12),variable=var_800_830,onvalue=1,offvalue=0).grid(row=3,column=1,columnspan=2)
    time_830_900_AM = Checkbutton(rinkA_window,text='8:30AM-9:00AM',font=('Arial',12),variable=var_830_900,onvalue=1,offvalue=0).grid(row=3,column=3,columnspan=2)
    time_900_930_AM = Checkbutton(rinkA_window,text='9:00AM-9:30AM',font=('Arial',12),variable=var_900_930,onvalue=1,offvalue=0).grid(row=3,column=5,columnspan=2)
    time_930_1000_AM = Checkbutton(rinkA_window,text='9:30AM-10:00AM',font=('Arial',12),variable=var_930_1000,onvalue=1,offvalue=0).grid(row=3,column=7,columnspan=2)
    time_1000_1030_AM = Checkbutton(rinkA_window,text='10:00AM-10:30AM',font=('Arial',12),variable=var_1000_1030,onvalue=1,offvalue=0).grid(row=3,column=9,columnspan=2)
    time_1030_1100_AM = Checkbutton(rinkA_window,text='10:30AM-11:00AM',font=('Arial',12),variable=var_1030_1100,onvalue=1,offvalue=0).grid(row=3,column=11,columnspan=2)
    time_1100_1130_AM = Checkbutton(rinkA_window,text='11:00AM-11:30AM',font=('Arial',12),variable=var_1100_1130,onvalue=1,offvalue=0).grid(row=3,column=13,columnspan=2)
    time_1130AM_1200PM = Checkbutton(rinkA_window,text='11:30AM-12:00PM',font=('Arial',12),variable=var_1130_1200,onvalue=1,offvalue=0).grid(row=3,column=15,columnspan=2)
    time_1200PM_1230_PM = Checkbutton(rinkA_window,text='12:00PM-12:30PM',font=('Arial',12),variable=var_1200_1230,onvalue=1,offvalue=0).grid(row=4,column=1,columnspan=2)
    time_1230_100_PM = Checkbutton(rinkA_window,text='12:30PM-1:00PM',font=('Arial',12),variable=var_1230_100,onvalue=1,offvalue=0).grid(row=4,column=3,columnspan=2)
    time_100_130_PM = Checkbutton(rinkA_window,text='1:00PM-1:30PM',font=('Arial',12),variable=var_100_130,onvalue=1,offvalue=0).grid(row=4,column=5,columnspan=2)
    time_130_200_PM = Checkbutton(rinkA_window,text='1:30PM-2:00PM',font=('Arial',12),variable=var_130_200,onvalue=1,offvalue=0).grid(row=4,column=7,columnspan=2)
    time_200_230_PM = Checkbutton(rinkA_window,text='2:00PM-2:30PM',font=('Arial',12),variable=var_200_230,onvalue=1,offvalue=0).grid(row=4,column=9,columnspan=2)
    time_230_300_PM = Checkbutton(rinkA_window,text='2:30PM-3:00PM',font=('Arial',12),variable=var_230_300,onvalue=1,offvalue=0).grid(row=4,column=11,columnspan=2)
    time_300_330_PM = Checkbutton(rinkA_window,text='3:00PM-3:30PM',font=('Arial',12),variable=var_300_330,onvalue=1,offvalue=0).grid(row=4,column=13,columnspan=2)
    time_330_400_PM = Checkbutton(rinkA_window,text='3:30PM-4:00PM',font=('Arial',12),variable=var_330_400,onvalue=1,offvalue=0).grid(row=4,column=15,columnspan=2)
    reserve_openskate_time_button = Button(rinkA_window,text='Reserve Skate Time',font=('Arial',12),command=attempt_reserve_openskate_time).grid(row=6,column=8,columnspan=2)
    rinkA_window.mainloop()

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
    empty_grid = Label(openskate_window,height=1,width=21).grid(row=5,column=0)
    openskate_title = Label(openskate_window,text='Open Skate',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)
    def openskate_with_login_to_home_page_with_login():
        openskate_window.destroy()
        home_page.open_home_screen_with_user_logged_in()
    openskate_without_login_to_home_page_without_login_button = Button(openskate_window,font=('Arial',12),text='Go to home page',command=openskate_with_login_to_home_page_with_login).grid(row=0,column=0)
    choose_rink_instruction = Label(openskate_window,text='Choose Skating Rink:',font=('Arial',12)).grid(row=3,column=4)
    choose_rink_var = StringVar()
    choose_rink_dropdown = OptionMenu(openskate_window,choose_rink_var,"Rink A","Rink B","Rink C")
    choose_rink_dropdown.grid(row=3,column=5)
    rink_entry_box = Entry(openskate_window,textvariable=choose_rink_var,font=('Arial',12),state='readonly')
    rink_entry_box.place(x=4000,y=5000)
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
    reserve_skate_time_button = Button(openskate_window,text='Reserve Open Skate Time',font=('Arial',12),command=reserve_skate_time).grid(row=5,column=4,columnspan=2)