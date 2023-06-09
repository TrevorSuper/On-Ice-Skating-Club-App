from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import home_page
import pymysql

def admin_login():
    admin_login_window = Tk() #instantiate an instance of a window
    admin_login_window.geometry("1920x1080") #size of the window, chosing 
    admin_login_window.title("On Ice Skating Administrator Login") #title of the window screen
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png') #converts the png to a usable image for the window icon and instantiates it as an object
    admin_login_window.iconphoto(True, ShoeIcon) #sets the object ShoeIcon as the window icon
    #window.config(background="") can set a color such as "blue" in quotation marks or use a hex value (with hashtag) to set the background a certain color, google hex color picker
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=0,column=9)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(admin_login_window,height=1,width=21).grid(row=4,column=0)
    user_name_label = Label(admin_login_window,text="Administrator: ",font=("Arial",12)).grid(row=3,column=4)
    user_name_entry = Entry(admin_login_window,font=("Arial",12)).grid(row=3,column=5)
    user_pw_label = Label(admin_login_window,text="Password: ",font=("Arial",12)).grid(row=4,column=4)
    user_pw_entry = Entry(admin_login_window,font=("Arial",12),show="*").grid(row=4,column=5)
    def attempt_admin_login():
        print('attempt_admin_login')
        #end
    admin_login_button = Button(admin_login_window,text="Login",width = "15",command=attempt_admin_login,font=("Arial",12)).grid(row=5,column=4,columnspan=2)
    def open_user_login():
        admin_login_window.destroy()
        user_login()
        #end
    not_an_admin_button = Button(admin_login_window,text="Not An Admin?",width = "15",command=open_user_login,font=("Arial",12)).grid(row=6,column=4,columnspan=2)

    #admin_login_window.mainloop() #makes the window visible, and will listen for events, it important this mainloop function is run after setting all the previous widgets

def user_login():
    user_login_window = Tk()
    user_login_window.geometry("1920x1080")
    user_login_window.title("User Login")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    user_login_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=1)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=2)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=3)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=4)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=5)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=6)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=7)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=8)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=0,column=9)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=4,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=5,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=6,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=7,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=8,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=9,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=10,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=11,column=0)
    empty_grid = Label(user_login_window,height=1,width=21).grid(row=12,column=0)
    login_title_label = Label(user_login_window,text='Login',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)
    user_name_label = Label(user_login_window,text="Email: ",font=("Arial",12)).grid(row=3,column=4)
    email_entry = Entry(user_login_window,font=("Arial",12))
    email_entry.grid(row=3,column=5)
    user_pw_label = Label(user_login_window,text="Password: ",font=("Arial",12)).grid(row=4,column=4)
    user_pw_entry = Entry(user_login_window,font=("Arial",12),show="*")
    user_pw_entry.grid(row=4,column=5)
    def attempt_user_login():
        if email_entry.get()=='' or user_pw_entry.get()=='':
            messagebox.showerror('Error','Please enter an email and password.')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='legacyserverwhen')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Unable To Connect To Database.')
                return
            query='use userdata'
            mycursor.execute(query)
            query='select * from data where email=%s and password=%s'
            mycursor.execute(query,(email_entry.get(),user_pw_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid email or password.')
            else:
                messagebox.showinfo('Success','Login Successful')
                global emailEntry
                emailEntry = email_entry.get()
                user_login_window.destroy()
                home_page.home_screen()

        #end
    user_login_button = Button(user_login_window,text="Login",width = "15",command=attempt_user_login,font=("Arial",12)).grid(row=6,column=4,columnspan=2)

    def forgot_password():
        user_login_window.destroy()
        recover_window = Tk()
        recover_window.geometry("1920x1080")
        recover_window.title("Reset Password")
        ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
        recover_window.iconphoto(True, ShoeIcon)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=1)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=2)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=3)
        empty_grid = Label(recover_window,height=1,width=21,background='red').grid(row=0,column=4)
        empty_grid = Label(recover_window,height=1,width=21,background='blue').grid(row=0,column=5)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=6)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=7)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=8)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=0,column=9)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=1,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=2,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=3,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=4,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=5,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=6,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=7,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=8,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=9,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=10,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=11,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=12,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=13,column=0)
        empty_grid = Label(recover_window,height=1,width=21).grid(row=14,column=0)
        reset_password_label = Label(recover_window,text='Reset Password',font=("Arial Bold",18)).grid(row=1,column=4,rowspan=2,columnspan=2)
        recover_email_label = Label(recover_window,text='Email:',font=('Arial',12)).grid(row=3,column=4)
        recover_email_entry = Entry(recover_window,text='Email',font=('Arial',12))
        recover_email_entry.grid(row=3,column=5)

        def recover_to_login():
            recover_window.destroy()
            user_login()
        recover_to_login_button = Button(recover_window,text='Previous Page',width='13',command=recover_to_login,font=('Arial',12)).grid(row=0,column=0)
        choose_recover_q_label = Label(recover_window,text='Choose Recovery Question:',font=('Arial',12)).grid(row=4,column=4)
        answer_recover_q_label = Label(recover_window,text='Answer Recovery Question:',font=('Arial',12)).grid(row=5,column=4)
        answer_recover_q_entry = Entry(recover_window,font=('Arial',12))
        answer_recover_q_entry.grid(row=5,column=5)
        answer_recover_pw_questions = [
        "What street did you grow up on?",
        "What high school did you go to?",
        "What was the make and model of your first car?",
        "In what city or town did your parents meet?"
        ]
        recover_pw_dropdown = StringVar()
        recover_pw_dropdown = OptionMenu(recover_window,recover_pw_dropdown,*answer_recover_pw_questions)
        recover_pw_dropdown.grid(row=4,column=5)
        def reset_password():
            if recover_email_entry.get()=='' or answer_recover_q_entry.get()=='':
                messagebox.showerror('Error','All fields are required')
        reset_password_button = Button(recover_window,text='Reset Password',font=('Arial',12),command=reset_password).grid(row=7,column=4,columnspan=2)

    forgot_password_label = Label(user_login_window,text='Forgot Password?',font=('Arial',12)).grid(row=8,column=4,columnspan=2)
    forgot_password_button = Button(user_login_window,text='Reset Password',command=forgot_password,font=('Arial',12)).grid(row=9,column=4,columnspan=2)
    no_account = Label(user_login_window,text = "Don't have an Account?",font=('Arial',12)).grid(row=11,column=4,columnspan=2)
    def open_register():
        user_login_window.destroy()
        register_new_user()
        #end
    register_button = Button(user_login_window,text='Create Account',width='15',command=open_register,font=('Arial',12)).grid(row=12,column=4,columnspan=2)
    def open_admin_login():
        user_login_window.destroy()
        admin_login()
        #end
    are_you_an_admin_button = Button(user_login_window,text='Are you an Admin?',width = "15",command=open_admin_login,font=('Arial',12)).grid(row=14,column=4,columnspan=2)
    def return_home():
        user_login_window.destroy()
        home_page.home_screen()
        #end
    back_to_home_page_button = Button(user_login_window,text='Previous Page',width='13',command=return_home,font=('Arial',12)).grid(row=0,column=0)
    #end of user_login()

def register_new_user():
    def clear():
        email_entry.delete(0,END)
        confirm_email_entry.delete(0,END)
        user_pw_entry.delete(0,END)
        user_confirm_pw_entry.delete(0,END)
    register_window = Tk()
    register_window.geometry("1920x1080")
    register_window.title("Create New Account")
    ShoeIcon = PhotoImage(file='src\img\Skating_Shoe_Icon.png')
    register_window.iconphoto(True, ShoeIcon)
    empty_grid = Label(register_window,height=1,width=21).grid(row=0,column=0)
    empty_grid = Label(register_window,height=1,width=21,background='blue').grid(row=0,column=1)
    empty_grid = Label(register_window,height=1,width=21,background='red').grid(row=0,column=2)
    empty_grid = Label(register_window,height=1,width=21,background='blue').grid(row=0,column=3)
    empty_grid = Label(register_window,height=1,width=21,background='red').grid(row=0,column=4)
    empty_grid = Label(register_window,height=1,width=21,background='blue').grid(row=0,column=5)
    empty_grid = Label(register_window,height=1,width=21,background='red').grid(row=0,column=6)
    empty_grid = Label(register_window,height=1,width=21,background='blue').grid(row=0,column=7)
    empty_grid = Label(register_window,height=1,width=21,background='red').grid(row=0,column=8)
    empty_grid = Label(register_window,height=1,width=21,background='blue').grid(row=0,column=9)
    empty_grid = Label(register_window,height=1,width=21).grid(row=1,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=2,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=3,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=4,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=5,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=6,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=7,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=8,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=9,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=10,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=11,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=12,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=13,column=0)
    empty_grid = Label(register_window,height=1,width=21).grid(row=14,column=0)
    create_new_account_title_label = Label(register_window,text='Create New Account',font=('Arial Bold',18)).grid(row=1,column=4,rowspan=2,columnspan=2)
    email_label = Label(register_window,text="Email:",font=("Arial",12)).grid(row=3,column=3)
    email_entry = Entry(register_window,font=("Arial",12))
    email_entry.grid(row=3,column=4)
    confirm_email_label = Label(register_window,text="Confirm Email:",font=('Arial',12)).grid(row=4,column=3)
    confirm_email_entry = Entry(register_window,font=("Arial",12))
    confirm_email_entry.grid(row=4,column=4)
    user_pw_label = Label(register_window,text="Password:",font=("Arial",12)).grid(row=5,column=3)
    user_pw_entry = Entry(register_window,font=("Arial",12),show="*")
    user_pw_entry.grid(row=5,column=4)
    user_confirm_pw_label = Label(register_window,text="Confirm Password:",font=("Arial",12)).grid(row=6,column=3)
    user_confirm_pw_entry = Entry(register_window,font=("Arial",12),show="*")
    user_confirm_pw_entry.grid(row=6,column=4)
    recover_question_instructions = Label(register_window,font=("Arial",12),text='Enter a security question\nexactly as it appears from the\nfollowing list of questions.').grid(row=3,column=5,rowspan=3,columnspan=2)
    #recover_question1 = Entry(register_window,font=('Arial',12),text="What street did you grow up on?").grid(row=6,column=5)
    #"What high school did you go to?",
    #"What was the make and model of your first car?",
    #"In what city or town did your parents meet?"
    recover_question_label = Label(register_window,text="Security Question:",font=("Arial",12)).grid(row=7,column=3)
    recover_question_entry = Entry(register_window,font=('Arial',12))
    recover_question_entry.grid(row=7,column=4)
    recover_answer_label = Label(register_window,text='Security Answer:',font=('Arial',12)).grid(row=8,column=3)
    recover_answer_entry = Entry(register_window,font=('Arial',12))
    recover_answer_entry.grid(row=8,column=4)
    
    def create_account():
        if email_entry.get()=='' or confirm_email_entry.get()==''  or user_pw_entry.get()=='' or user_confirm_pw_entry.get()=='' or recover_answer_entry.get()=='':
            messagebox.showerror('Error','All fields are required')
            #end
        elif email_entry.get()!=confirm_email_entry.get():
            messagebox.showerror('Error','Email Mismatch')
        elif user_pw_entry.get() != user_confirm_pw_entry.get():
            messagebox.showerror('Error','Password Mismatch')
            #end
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='legacyserverwhen')
                mycursor=con.cursor()
                #end
            except:
                messagebox.showerror('Error','Unable To Connect To Database.')
                return
                #end
            try:
                query='create database userdata'
                mycursor.execute(query)
                query='use userdata'
                mycursor.execute(query)
                query='create table data(id int auto_increment primary key not null,email varchar(50),password varchar(20))'
                mycursor.execute(query)
            except:
                mycursor.execute('use userdata')
            query='select * from data where email=%s'
            mycursor.execute(query,(email_entry.get()))
            row=mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error','An account with this email already exists, please use another email.')
            else:
                query='insert into data(email,password) values(%s,%s)'
                mycursor.execute(query,(email_entry.get(),user_pw_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Account Created')
                clear()
                open_login()
                #end

    create_account_button = Button(register_window,text='Create Account',font=("Arial",12),command=create_account).grid(row=11,column=4,columnspan=2)
    def open_login():
        register_window.destroy()
        user_login()
        #end
    have_an_account_label = Label(register_window,text='Have an Account?',font=('Arial',12)).grid(row=13,column=4,columnspan=2)
    open_login_button = Button(register_window,text='Login',font=("Arial",12),command=open_login).grid(row=14,column=4,columnspan=2)
    def return_home():
        register_window.destroy()
        home_page.home_screen()
        #end
    back_to_home_page_button = Button(register_window,text='Return to home page',width='16',command=return_home,font=('Arial',12)).grid(row=0,column=0)