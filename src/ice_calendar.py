from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pymysql
import home_page
import login_page

def open_ice_calendar_logged_in():
    # Go Home
    def goHome():
        ice_calendar.destroy()
        home_page.open_home_screen_with_user_logged_in()

    # Open a new window to sign up for the event
    def SignUp(event):
        signUpWindow = tk.Toplevel()
        signUpWindow.title("Sign Up For Event ?")
        signUpWindow.config(width = 300, height = 200)
        

        query = tk.Label(signUpWindow,
            # Temp text, find out a way to include the actual event in the lable
            # ie. "Would you like to sign up for " + event + "?"
            text = "Would you like to sign up for this event?").grid(row = 1, column = 1)

        buttonCancel = tk.Button(signUpWindow, text = "Cancel", command = signUpWindow.destroy)

        buttonSignUp = tk.Button(signUpWindow, text = "Yes",
            # Temp code, Proceede to add the event to a list ?
            command = signUpWindow.destroy)

        buttonCancel.grid(row = 10, column = 10)
        buttonSignUp.grid(row = 10, column = 11)


    ice_calendar = tk.Tk()
    ice_calendar.title("Calendar")

    # Labels for the month and days along with placemnt 
    month =tk.Label(ice_calendar, text = "June 2023", height = 3, width = 10, font = 'bold')
    sunday = tk.Label(ice_calendar, text = "Sunday", height = 2, width = 10)
    monday = tk.Label(ice_calendar, text = "Monday", height = 2, width = 10)
    tuesday= tk.Label(ice_calendar, text = "Tuesday", height = 2, width = 10)
    wednesday = tk.Label(ice_calendar, text = "Wednesday", height = 2, width = 10)
    thursday = tk.Label(ice_calendar, text = "Thursday", height = 2, width = 10)
    friday = tk.Label(ice_calendar, text = "Friday", height = 2, width = 10)
    saturday = tk.Label(ice_calendar, text = "Saturday", height = 2, width = 10)

    month.grid(row = 1, column = 3, columnspan = 3, sticky = 'ew')
    sunday.grid(row = 2, column = 1)
    monday.grid(row = 2, column = 2)
    tuesday.grid(row = 2, column = 3)
    wednesday.grid(row = 2, column = 4)
    thursday.grid(row = 2, column = 5)
    friday.grid(row = 2, column = 6)
    saturday.grid(row = 2, column = 7)
    

    # Fillers
    fillerS = tk.Label(ice_calendar, height = 2, width = 10)
    fillerM = tk.Label(ice_calendar, height = 2, width = 10)
    fillerT = tk.Label(ice_calendar, height = 2, width = 10)
    fillerW = tk.Label(ice_calendar, height = 2, width = 10)
    filler1 = tk.Label(ice_calendar, height = 5, width = 10)
    filler2 = tk.Label(ice_calendar, height = 5, width = 10)
    filler3 = tk.Label(ice_calendar, height = 5, width = 10)
    filler4 = tk.Label(ice_calendar, height = 5, width = 10)

    fillerS.grid(row = 3, column = 1)
    fillerM.grid(row = 3, column = 2)
    fillerT.grid(row = 3, column = 3)
    fillerW.grid(row = 3, column = 4)
    filler1.grid(row = 4, column = 1)
    filler2.grid(row = 4, column = 2)
    filler3.grid(row = 4, column = 3)
    filler4.grid(row = 4, column = 4)


    # Labels for the numbers of the days in the month
    lbl1 = tk.Label(ice_calendar, text = "1", height = 2, width = 10)
    lbl1.grid(row = 3, column = 5)

    lbl2 = tk.Label(ice_calendar, text = "2", height = 2, width = 10)
    lbl2.grid(row = 3, column = 6)

    lbl3 = tk.Label(ice_calendar, text = "3", height = 2, width = 10)
    lbl3.grid(row = 3, column = 7)

    lbl4 = tk.Label(ice_calendar, text = "4", height = 2, width = 10)
    lbl4.grid(row = 5, column = 1)

    lbl5 = tk.Label(ice_calendar, text = "5", height = 2, width = 10)
    lbl5.grid(row = 5, column = 2)

    lbl6 = tk.Label(ice_calendar, text = "6", height = 2, width = 10)
    lbl6.grid(row = 5, column = 3)

    lbl7 = tk.Label(ice_calendar, text = "7", height = 2, width = 10)
    lbl7.grid(row = 5, column = 4)

    lbl8 = tk.Label(ice_calendar, text = "8", height = 2, width = 10)
    lbl8.grid(row = 5, column = 5)

    lbl9 = tk.Label(ice_calendar, text = "9", height = 2, width = 10)
    lbl9.grid(row = 5, column = 6)

    lbl10 = tk.Label(ice_calendar, text = "10", height = 2, width = 10)
    lbl10.grid(row = 5, column = 7)

    lbl11 = tk.Label(ice_calendar, text = "11", height = 2, width = 10)
    lbl11.grid(row = 7, column = 1)

    lbl12 = tk.Label(ice_calendar, text = "12", height = 2, width = 10)
    lbl12.grid(row = 7, column = 2)

    lbl13 = tk.Label(ice_calendar, text = "13", height = 2, width = 10)
    lbl13.grid(row = 7, column = 3)

    lbl14 = tk.Label(ice_calendar, text = "14", height = 2, width = 10)
    lbl14.grid(row = 7, column = 4)

    lbl15 = tk.Label(ice_calendar, text = "15", height = 2, width = 10)
    lbl15.grid(row = 7, column = 5)

    lbl16 = tk.Label(ice_calendar, text = "16", height = 2, width = 10)
    lbl16.grid(row = 7, column = 6)

    lbl17 = tk.Label(ice_calendar, text = "17", height = 2, width = 10)
    lbl17.grid(row = 7, column = 7)

    lbl18 = tk.Label(ice_calendar, text = "18", height = 2, width = 10)
    lbl18.grid(row = 9, column = 1)

    lbl19 = tk.Label(ice_calendar, text = "19", height = 2, width = 10)
    lbl19.grid(row = 9, column = 2)

    lbl20 = tk.Label(ice_calendar, text = "20", height = 2, width = 10)
    lbl20.grid(row = 9, column = 3)

    lbl21 = tk.Label(ice_calendar, text = "21", height = 2, width = 10)
    lbl21.grid(row = 9, column = 4)

    lbl22 = tk.Label(ice_calendar, text = "22", height = 2, width = 10)
    lbl22.grid(row = 9, column = 5)

    lbl23 = tk.Label(ice_calendar, text = "23", height = 2, width = 10)
    lbl23.grid(row = 9, column = 6)

    lbl24 = tk.Label(ice_calendar, text = "24", height = 2, width = 10)
    lbl24.grid(row = 9, column = 7)

    lbl25 = tk.Label(ice_calendar, text = "25", height = 2, width = 10)
    lbl25.grid(row = 11, column = 1)

    lbl26 = tk.Label(ice_calendar, text = "26", height = 2, width = 10)
    lbl26.grid(row = 11, column = 2)

    lbl27 = tk.Label(ice_calendar, text = "27", height = 2, width = 10)
    lbl27.grid(row = 11, column = 3)

    lbl28 = tk.Label(ice_calendar, text = "28", height = 2, width = 10)
    lbl28.grid(row = 11, column = 4)

    lbl29 = tk.Label(ice_calendar, text = "29", height = 2, width = 10)
    lbl29.grid(row = 11, column = 5)

    lbl30 = tk.Label(ice_calendar, text = "30", height = 2, width = 10)
    lbl30.grid(row = 11, column = 6)

    # Editable text boxes to place the events into
    text1 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text1.grid(row = 4, column = 5)

    text2 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text2.grid(row = 4, column = 6)

    text3 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text3.grid(row = 4, column = 7)

    text4 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text4.grid(row = 6, column = 1)

    text5 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text5.grid(row = 6, column = 2)

    text6 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text6.grid(row = 6, column = 3)

    text7 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text7.grid(row = 6, column = 4)

    text8 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text8.grid(row = 6, column = 5)

    text9 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text9.grid(row = 6, column = 6)

    text10 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text10.grid(row = 6, column = 7)

    text11 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text11.grid(row = 8, column = 1)

    text12 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text12.grid(row = 8, column = 2)

    text13 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text13.grid(row = 8, column = 3)

    text14 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text14.grid(row = 8, column = 4)

    text15 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text15.grid(row = 8, column = 5)

    text16 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text16.grid(row = 8, column = 6)

    text17 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text17.grid(row = 8, column = 7)

    text18 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text18.grid(row = 10, column = 1)

    text19 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text19.grid(row = 10, column = 2)

    text20 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text20.grid(row = 10, column = 3)

    text21 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text21.grid(row = 10, column = 4)

    text22 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text22.grid(row = 10, column = 5)

    text23 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text23.grid(row = 10, column = 6)

    text24 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text24.grid(row = 10, column = 7)

    text25 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text25.grid(row = 12, column = 1)

    text26 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text26.grid(row = 12, column = 2)

    text27 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text27.grid(row = 12, column = 3)

    text28 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text28.grid(row = 12, column = 4)

    text29 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text29.grid(row = 12, column = 5)

    text30 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text30.grid(row = 12, column = 6)

    homeBtn = tk.Button(ice_calendar, text = "Return to Home Page", command = goHome)
    homeBtn.grid(row = 13, column = 3, columnspan = 3)


    # Bind it so that should a user double click into the text box, it opens an event sign up window
    text1.bind("<Double-Button-1>", SignUp)
    text2.bind('<Double-Button-1>', SignUp)
    text3.bind('<Double-Button-1>', SignUp)
    text4.bind('<Double-Button-1>', SignUp)
    text5.bind('<Double-Button-1>', SignUp)
    text6.bind('<Double-Button-1>', SignUp)
    text7.bind('<Double-Button-1>', SignUp)
    text8.bind('<Double-Button-1>', SignUp)
    text9.bind('<Double-Button-1>', SignUp)
    text10.bind('<Double-Button-1>', SignUp)
    text11.bind('<Double-Button-1>', SignUp)
    text12.bind('<Double-Button-1>', SignUp)
    text13.bind('<Double-Button-1>', SignUp)
    text14.bind('<Double-Button-1>', SignUp)
    text15.bind('<Double-Button-1>', SignUp)
    text16.bind('<Double-Button-1>', SignUp)
    text17.bind('<Double-Button-1>', SignUp)
    text18.bind('<Double-Button-1>', SignUp)
    text19.bind('<Double-Button-1>', SignUp)
    text20.bind('<Double-Button-1>', SignUp)
    text21.bind('<Double-Button-1>', SignUp)
    text22.bind('<Double-Button-1>', SignUp)
    text23.bind('<Double-Button-1>', SignUp)
    text24.bind('<Double-Button-1>', SignUp)
    text25.bind('<Double-Button-1>', SignUp)
    text26.bind('<Double-Button-1>', SignUp)
    text27.bind('<Double-Button-1>', SignUp)
    text28.bind('<Double-Button-1>', SignUp)
    text29.bind('<Double-Button-1>', SignUp)
    text30.bind('<Double-Button-1>', SignUp)

def open_ice_calendar_not_logged_in():
    
    # Go Home
    def goHome():
        ice_calendar.destroy()
        home_page.open_home_screen_without_user_logged_in()

    # Open a new window to sign up for the event
    def SignUp(event):
        signUpWindow = tk.Toplevel()
        signUpWindow.title("Sign Up For Event ?")
        signUpWindow.config(width = 300, height = 200)
        
        messagebox.showerror('Error','You must be logged in to an account to register for an event.')
        signUpWindow.destroy()
        ice_calendar.destroy()
        login_page.user_login()


    ice_calendar = tk.Tk()
    ice_calendar.title("Calendar")

    # Labels for the month and days along with placemnt 
    month =tk.Label(ice_calendar, text = "June 2023", height = 3, width = 10, font = 'bold')
    sunday = tk.Label(ice_calendar, text = "Sunday", height = 2, width = 10)
    monday = tk.Label(ice_calendar, text = "Monday", height = 2, width = 10)
    tuesday= tk.Label(ice_calendar, text = "Tuesday", height = 2, width = 10)
    wednesday = tk.Label(ice_calendar, text = "Wednesday", height = 2, width = 10)
    thursday = tk.Label(ice_calendar, text = "Thursday", height = 2, width = 10)
    friday = tk.Label(ice_calendar, text = "Friday", height = 2, width = 10)
    saturday = tk.Label(ice_calendar, text = "Saturday", height = 2, width = 10)

    month.grid(row = 1, column = 3, columnspan = 3, sticky = 'ew')
    sunday.grid(row = 2, column = 1)
    monday.grid(row = 2, column = 2)
    tuesday.grid(row = 2, column = 3)
    wednesday.grid(row = 2, column = 4)
    thursday.grid(row = 2, column = 5)
    friday.grid(row = 2, column = 6)
    saturday.grid(row = 2, column = 7)
    

    # Fillers
    fillerS = tk.Label(ice_calendar, height = 2, width = 10)
    fillerM = tk.Label(ice_calendar, height = 2, width = 10)
    fillerT = tk.Label(ice_calendar, height = 2, width = 10)
    fillerW = tk.Label(ice_calendar, height = 2, width = 10)
    filler1 = tk.Label(ice_calendar, height = 5, width = 10)
    filler2 = tk.Label(ice_calendar, height = 5, width = 10)
    filler3 = tk.Label(ice_calendar, height = 5, width = 10)
    filler4 = tk.Label(ice_calendar, height = 5, width = 10)

    fillerS.grid(row = 3, column = 1)
    fillerM.grid(row = 3, column = 2)
    fillerT.grid(row = 3, column = 3)
    fillerW.grid(row = 3, column = 4)
    filler1.grid(row = 4, column = 1)
    filler2.grid(row = 4, column = 2)
    filler3.grid(row = 4, column = 3)
    filler4.grid(row = 4, column = 4)


    # Labels for the numbers of the days in the month
    lbl1 = tk.Label(ice_calendar, text = "1", height = 2, width = 10)
    lbl1.grid(row = 3, column = 5)

    lbl2 = tk.Label(ice_calendar, text = "2", height = 2, width = 10)
    lbl2.grid(row = 3, column = 6)

    lbl3 = tk.Label(ice_calendar, text = "3", height = 2, width = 10)
    lbl3.grid(row = 3, column = 7)

    lbl4 = tk.Label(ice_calendar, text = "4", height = 2, width = 10)
    lbl4.grid(row = 5, column = 1)

    lbl5 = tk.Label(ice_calendar, text = "5", height = 2, width = 10)
    lbl5.grid(row = 5, column = 2)

    lbl6 = tk.Label(ice_calendar, text = "6", height = 2, width = 10)
    lbl6.grid(row = 5, column = 3)

    lbl7 = tk.Label(ice_calendar, text = "7", height = 2, width = 10)
    lbl7.grid(row = 5, column = 4)

    lbl8 = tk.Label(ice_calendar, text = "8", height = 2, width = 10)
    lbl8.grid(row = 5, column = 5)

    lbl9 = tk.Label(ice_calendar, text = "9", height = 2, width = 10)
    lbl9.grid(row = 5, column = 6)

    lbl10 = tk.Label(ice_calendar, text = "10", height = 2, width = 10)
    lbl10.grid(row = 5, column = 7)

    lbl11 = tk.Label(ice_calendar, text = "11", height = 2, width = 10)
    lbl11.grid(row = 7, column = 1)

    lbl12 = tk.Label(ice_calendar, text = "12", height = 2, width = 10)
    lbl12.grid(row = 7, column = 2)

    lbl13 = tk.Label(ice_calendar, text = "13", height = 2, width = 10)
    lbl13.grid(row = 7, column = 3)

    lbl14 = tk.Label(ice_calendar, text = "14", height = 2, width = 10)
    lbl14.grid(row = 7, column = 4)

    lbl15 = tk.Label(ice_calendar, text = "15", height = 2, width = 10)
    lbl15.grid(row = 7, column = 5)

    lbl16 = tk.Label(ice_calendar, text = "16", height = 2, width = 10)
    lbl16.grid(row = 7, column = 6)

    lbl17 = tk.Label(ice_calendar, text = "17", height = 2, width = 10)
    lbl17.grid(row = 7, column = 7)

    lbl18 = tk.Label(ice_calendar, text = "18", height = 2, width = 10)
    lbl18.grid(row = 9, column = 1)

    lbl19 = tk.Label(ice_calendar, text = "19", height = 2, width = 10)
    lbl19.grid(row = 9, column = 2)

    lbl20 = tk.Label(ice_calendar, text = "20", height = 2, width = 10)
    lbl20.grid(row = 9, column = 3)

    lbl21 = tk.Label(ice_calendar, text = "21", height = 2, width = 10)
    lbl21.grid(row = 9, column = 4)

    lbl22 = tk.Label(ice_calendar, text = "22", height = 2, width = 10)
    lbl22.grid(row = 9, column = 5)

    lbl23 = tk.Label(ice_calendar, text = "23", height = 2, width = 10)
    lbl23.grid(row = 9, column = 6)

    lbl24 = tk.Label(ice_calendar, text = "24", height = 2, width = 10)
    lbl24.grid(row = 9, column = 7)

    lbl25 = tk.Label(ice_calendar, text = "25", height = 2, width = 10)
    lbl25.grid(row = 11, column = 1)

    lbl26 = tk.Label(ice_calendar, text = "26", height = 2, width = 10)
    lbl26.grid(row = 11, column = 2)

    lbl27 = tk.Label(ice_calendar, text = "27", height = 2, width = 10)
    lbl27.grid(row = 11, column = 3)

    lbl28 = tk.Label(ice_calendar, text = "28", height = 2, width = 10)
    lbl28.grid(row = 11, column = 4)

    lbl29 = tk.Label(ice_calendar, text = "29", height = 2, width = 10)
    lbl29.grid(row = 11, column = 5)

    lbl30 = tk.Label(ice_calendar, text = "30", height = 2, width = 10)
    lbl30.grid(row = 11, column = 6)

    # Editable text boxes to place the events into
    text1 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text1.grid(row = 4, column = 5)

    text2 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text2.grid(row = 4, column = 6)

    text3 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text3.grid(row = 4, column = 7)

    text4 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text4.grid(row = 6, column = 1)

    text5 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text5.grid(row = 6, column = 2)

    text6 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text6.grid(row = 6, column = 3)

    text7 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text7.grid(row = 6, column = 4)

    text8 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text8.grid(row = 6, column = 5)

    text9 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text9.grid(row = 6, column = 6)

    text10 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text10.grid(row = 6, column = 7)

    text11 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text11.grid(row = 8, column = 1)

    text12 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text12.grid(row = 8, column = 2)

    text13 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text13.grid(row = 8, column = 3)

    text14 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text14.grid(row = 8, column = 4)

    text15 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text15.grid(row = 8, column = 5)

    text16 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text16.grid(row = 8, column = 6)

    text17 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text17.grid(row = 8, column = 7)

    text18 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text18.grid(row = 10, column = 1)

    text19 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text19.grid(row = 10, column = 2)

    text20 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text20.grid(row = 10, column = 3)

    text21 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text21.grid(row = 10, column = 4)

    text22 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text22.grid(row = 10, column = 5)

    text23 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text23.grid(row = 10, column = 6)

    text24 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text24.grid(row = 10, column = 7)

    text25 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text25.grid(row = 12, column = 1)

    text26 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text26.grid(row = 12, column = 2)

    text27 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text27.grid(row = 12, column = 3)

    text28 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text28.grid(row = 12, column = 4)

    text29 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text29.grid(row = 12, column = 5)

    text30 = tk.Text(ice_calendar, height = 5, width = 10, state = 'disabled')
    text30.grid(row = 12, column = 6)

    homeBtn = tk.Button(ice_calendar, text = "Return to Home Page", command = goHome)
    homeBtn.grid(row = 13, column = 3, columnspan = 3)

    # Bind it so that should a user double click into the text box, it opens an event sign up window
    text1.bind("<Double-Button-1>", SignUp)
    text2.bind('<Double-Button-1>', SignUp)
    text3.bind('<Double-Button-1>', SignUp)
    text4.bind('<Double-Button-1>', SignUp)
    text5.bind('<Double-Button-1>', SignUp)
    text6.bind('<Double-Button-1>', SignUp)
    text7.bind('<Double-Button-1>', SignUp)
    text8.bind('<Double-Button-1>', SignUp)
    text9.bind('<Double-Button-1>', SignUp)
    text10.bind('<Double-Button-1>', SignUp)
    text11.bind('<Double-Button-1>', SignUp)
    text12.bind('<Double-Button-1>', SignUp)
    text13.bind('<Double-Button-1>', SignUp)
    text14.bind('<Double-Button-1>', SignUp)
    text15.bind('<Double-Button-1>', SignUp)
    text16.bind('<Double-Button-1>', SignUp)
    text17.bind('<Double-Button-1>', SignUp)
    text18.bind('<Double-Button-1>', SignUp)
    text19.bind('<Double-Button-1>', SignUp)
    text20.bind('<Double-Button-1>', SignUp)
    text21.bind('<Double-Button-1>', SignUp)
    text22.bind('<Double-Button-1>', SignUp)
    text23.bind('<Double-Button-1>', SignUp)
    text24.bind('<Double-Button-1>', SignUp)
    text25.bind('<Double-Button-1>', SignUp)
    text26.bind('<Double-Button-1>', SignUp)
    text27.bind('<Double-Button-1>', SignUp)
    text28.bind('<Double-Button-1>', SignUp)
    text29.bind('<Double-Button-1>', SignUp)
    text30.bind('<Double-Button-1>', SignUp)