from tkinter import *
def admin_login():
    admin_login_window = Tk() #instantiate an instance of a window
    admin_login_window.geometry("1920x1080") #size of the window, chosing 
    admin_login_window.title("On Ice Skating") #title of the window screen
    admin_ShoeIcon = PhotoImage(file='Skating_Shoe_Icon.png') #converts the png to a usable image for the window icon and instantiates it as an object
    admin_login_window.iconphoto(True, admin_ShoeIcon) #sets the object ShoeIcon as the window icon

    #window.config(background="") can set a color such as "blue" in quotation marks or use a hex value (with hashtag) to set the background a certain color, google hex color picker
    #label.pack() #by default the widget will be placed in the top center of the window
    #button.pack() #button placed in the top center of the window

    admin_name_label = Label(admin_login_window,text="Administrator: ",font=("Arial",20)) #the second argument in this function is an option, a key-word argument that can be passed into the consctructor for the widget
    admin_name_label.place(x=100,y=100) #places the label at an x,y coordinate position
    admin_pw_label = Label(admin_login_window,text="Password: ",font=("Arial",20))
    admin_pw_label.place(x=100,y=150)
    
    def admin_login_click():
        print("Login succesful")
    admin_login_button = Button(admin_login_window,text="Login",command=admin_login_click,font=("Arial",20))
    admin_login_button.place(x=400,y=200)

    admin_name_entry = Entry(admin_login_window,font=("Arial",20))
    admin_name_entry.place(x=275,y=100)
    admin_pw_entry = Entry(admin_login_window,font=("Arial",20),show="*")
    admin_pw_entry.place(x=275,y=150)
    

    admin_login_window.mainloop() #makes the window visible, and will listen for events, it important this mainloop function is run after setting all the previous widgets

def user_login():
    user_login_window = Tk()
    user_login_window.geometry("1920x1080")
    user_login_window.title("On Ice Skating")
    user_ShoeIcon = PhotoImage(file='Skating_Shoe_Icon.png')
    user_login_window.iconphoto(True, user_ShoeIcon)
    user_name_label = Label(user_login_window,text="Username: ",font=("Arial",20))
    user_name_label.place(x=100,y=100)
    user_pw_label = Label(user_login_window,text="Password: ",font=("Arial",20))
    user_pw_label.place(x=100,y=150)
    def user_login_click():
        print("Login succesful")
    user_login_button = Button(user_login_window,text="Login",command=user_login_click,font=("Arial",20))
    user_login_button.place(x=400,y=200)
    user_name_entry = Entry(user_login_window,font=("Arial",20))
    user_name_entry.place(x=275,y=100)
    user_pw_entry = Entry(user_login_window,font=("Arial",20),show="*")
    user_pw_entry.place(x=275,y=150)
    
    user_login_window.mainloop()
