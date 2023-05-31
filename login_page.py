from tkinter import *
import home_page
def admin_login():
    admin_login_window = Tk() #instantiate an instance of a window
    admin_login_window.geometry("1920x1080") #size of the window, chosing 
    admin_login_window.title("On Ice Skating Administrator Login") #title of the window screen
    ShoeIcon = PhotoImage(file='Skating_Shoe_Icon.png') #converts the png to a usable image for the window icon and instantiates it as an object
    admin_login_window.iconphoto(True, ShoeIcon) #sets the object ShoeIcon as the window icon

    #window.config(background="") can set a color such as "blue" in quotation marks or use a hex value (with hashtag) to set the background a certain color, google hex color picker
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=0,column=0)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=0,column=1)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=0,column=2)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=1,column=0)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=2,column=0)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=3,column=0)
    empty_grid = Label(admin_login_window,height=1,width=20).grid(row=4,column=0)
    user_name_label = Label(admin_login_window,text="Administrator: ",font=("Arial",12)).grid(row=1,column=1)
    user_name_entry = Entry(admin_login_window,font=("Arial",12)).grid(row=1,column=2)
    user_pw_label = Label(admin_login_window,text="Password: ",font=("Arial",12)).grid(row=2,column=1)
    user_pw_entry = Entry(admin_login_window,font=("Arial",12),show="*").grid(row=2,column=2)
    def attempt_admin_login():
        print('attempt_admin_login')
        #end
    admin_login_button = Button(admin_login_window,text="Login",width = "10",command=attempt_admin_login,font=("Arial",12)).grid(row=3,column=1,columnspan=2)
    def open_user_login():
        admin_login_window.destroy()
        user_login()
        #end
    not_an_admin_button = Button(admin_login_window,text="Not An Admin?",width = "12",command=open_user_login,font=("Arial",12)).grid(row=4,column=1,columnspan=2)

    #admin_login_window.mainloop() #makes the window visible, and will listen for events, it important this mainloop function is run after setting all the previous widgets

def user_login():
    user_login_window = Tk()
    user_login_window.geometry("1920x1080")
    user_login_window.title("On Ice Skating User Login")
    ShoeIcon = PhotoImage(file='Skating_Shoe_Icon.png')
    user_login_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=0,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=0,column=1)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=0,column=2)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=1,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=2,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=3,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=4,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=5,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=6,column=0)
    empty_grid = Label(user_login_window,height=1,width=20).grid(row=7,column=0)
    user_name_label = Label(user_login_window,text="Username: ",font=("Arial",12)).grid(row=1,column=1)
    user_name_entry = Entry(user_login_window,font=("Arial",12)).grid(row=1,column=2)
    user_pw_label = Label(user_login_window,text="Password: ",font=("Arial",12)).grid(row=2,column=1)
    user_pw_entry = Entry(user_login_window,font=("Arial",12),show="*").grid(row=2,column=2)
    def attempt_user_login():
        print('attemt_user_login')
        #end
    user_login_button = Button(user_login_window,text="Login",width = "10",command=attempt_user_login,font=("Arial",12)).grid(row=3,column=1,columnspan=2)
    no_account = Label(user_login_window,text = "Don't have an Account?",font=('Arial',12)).grid(row=4,column=1,columnspan=2)
    def open_register():
        user_login_window.destroy()
        register_new_user()
        #end
    register_button = Button(user_login_window,text='Create One',width='10',command=open_register,font=('Arial',12)).grid(row=5,column=1,columnspan=2)
    def open_admin_login():
        user_login_window.destroy()
        admin_login()
        #end
    are_you_an_admin_button = Button(user_login_window,text='Are you an Admin?',width = "15",command=open_admin_login,font=('Arial',12)).grid(row=6,column=1,columnspan=2)
    def return_home():
        user_login_window.destroy()
        home_page.home_screen()
        #end
    back_to_home_page_button = Button(user_login_window,text='Return to home page',width='16',command=return_home,font=('Arial',12)).grid(row=7,column=1,columnspan=2)
    
    #user_login_window.mainloop()

def register_new_user():
    register_window = Tk()
    register_window.geometry("1920x1080")
    register_window.title("Create New Account")
    ShoeIcon = PhotoImage(file='Skating_Shoe_Icon.png')
    register_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(register_window,height=1,width=20).grid(row=0,column=0)
    empty_grid = Label(register_window,height=1,width=20).grid(row=0,column=1)
    empty_grid = Label(register_window,height=1,width=20).grid(row=0,column=2)
    empty_grid = Label(register_window,height=1,width=20).grid(row=1,column=0)
    empty_grid = Label(register_window,height=1,width=20).grid(row=2,column=0)
    empty_grid = Label(register_window,height=1,width=20).grid(row=3,column=0)
    empty_grid = Label(register_window,height=1,width=20).grid(row=4,column=0)
    user_name_label = Label(register_window,text="Username: ",font=("Arial",12)).grid(row=1,column=1)
    user_name_entry = Entry(register_window,font=("Arial",12)).grid(row=1,column=2)
    user_pw_label = Label(register_window,text="Password: ",font=("Arial",12)).grid(row=2,column=1)
    user_pw_entry = Entry(register_window,font=("Arial",12),show="*").grid(row=2,column=2)
    def create_account():
        print('create_account')
        #end
    create_account_button = Button(register_window,text='Create Account',font=("Arial",12),command=create_account).grid(row=3,column=1,columnspan=2)
    def return_home():
        register_window.destroy()
        home_page.home_screen()
        #end
    back_to_home_page_button = Button(register_window,text='Return to home page',width='16',command=return_home,font=('Arial',12)).grid(row=4,column=1,columnspan=2)
    #end