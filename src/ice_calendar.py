from tkinter import *
from tkinter import messagebox
import tkinter as tk
import datetime
import pymysql
import home_page
import login_page

def open_ice_calendar_logged_in():
    # Go Home
    def goHome():
        ice_calendar.destroy()
        home_page.open_home_screen_with_user_logged_in()

    # Open a new window to sign up for the event
    def SignUp(event,checkNum):
        signUpWindow = tk.Toplevel()
        signUpWindow.title("Sign Up For Event ?")
        signUpWindow.config(width = 300, height = 200)
        
        day = datetime.date.today().day
        
        if day < int(checkNum):
            query = tk.Label(signUpWindow, text = "Would you like to sign up for this event?").grid(row = 1, column = 1)

            buttonCancel = tk.Button(signUpWindow, text = "Cancel", command = signUpWindow.destroy)

            buttonSignUp = tk.Button(signUpWindow, text = "Yes",
            # Temp code, Proceede to add the event to a list ?
            command = signUpWindow.destroy)

            buttonCancel.grid(row = 10, column = 10)
            buttonSignUp.grid(row = 10, column = 11)
        else:
            messagebox.showerror('Error','It is too late to sign up for that event.')
            signUpWindow.destroy()



    ice_calendar = tk.Tk()
    ice_calendar.title("Calendar")
    ice_calendar.geometry("1920x1080")

    # Labels for the month and days along with placemnt 
    month =tk.Label(ice_calendar, text = "June 2023", height = 3, width = 10, font = 'bold')
    sunday = tk.Label(ice_calendar, text = "Sunday", height = 2, width = 10)
    monday = tk.Label(ice_calendar, text = "Monday", height = 2, width = 10)
    tuesday= tk.Label(ice_calendar, text = "Tuesday", height = 2, width = 10)
    wednesday = tk.Label(ice_calendar, text = "Wednesday", height = 2, width = 10)
    thursday = tk.Label(ice_calendar, text = "Thursday", height = 2, width = 10)
    friday = tk.Label(ice_calendar, text = "Friday", height = 2, width = 10)
    saturday = tk.Label(ice_calendar, text = "Saturday", height = 2, width = 10)

    month.grid(row = 1, column = 9, columnspan = 7, sticky = 'ew')
    sunday.grid(row = 2, column = 7)
    monday.grid(row = 2, column = 8)
    tuesday.grid(row = 2, column = 9)
    wednesday.grid(row = 2, column = 10)
    thursday.grid(row = 2, column = 11)
    friday.grid(row = 2, column = 12)
    saturday.grid(row = 2, column = 13)
    

    # Fillers
    fillerS = tk.Label(ice_calendar, height = 2, width = 10)
    fillerM = tk.Label(ice_calendar, height = 2, width = 10)
    fillerT = tk.Label(ice_calendar, height = 2, width = 10)
    fillerW = tk.Label(ice_calendar, height = 2, width = 10)
    filler1 = tk.Label(ice_calendar, height = 5, width = 10)
    filler2 = tk.Label(ice_calendar, height = 5, width = 10)
    filler3 = tk.Label(ice_calendar, height = 5, width = 10)
    filler4 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol1 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol2 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol3 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol4 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol5 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol6 = tk.Label(ice_calendar, height = 5, width = 10)

    fillerS.grid(row = 3, column = 7)
    fillerM.grid(row = 3, column = 8)
    fillerT.grid(row = 3, column = 9)
    fillerW.grid(row = 3, column = 10)
    filler1.grid(row = 4, column = 7)
    filler2.grid(row = 4, column = 8)
    filler3.grid(row = 4, column = 9)
    filler4.grid(row = 4, column = 10)
    fillerCol1.grid(row = 1, column = 1)
    fillerCol2.grid(row = 1, column = 2)
    fillerCol3.grid(row = 1, column = 3)
    fillerCol4.grid(row = 1, column = 4)
    fillerCol5.grid(row = 1, column = 5)
    fillerCol6.grid(row = 1, column = 6)


    # Labels for the numbers of the days in the month
    lbl1 = tk.Label(ice_calendar, text = "1", height = 2, width = 10)
    lbl1.grid(row = 3, column = 11)

    lbl2 = tk.Label(ice_calendar, text = "2", height = 2, width = 10)
    lbl2.grid(row = 3, column = 12)

    lbl3 = tk.Label(ice_calendar, text = "3", height = 2, width = 10)
    lbl3.grid(row = 3, column = 13)

    lbl4 = tk.Label(ice_calendar, text = "4", height = 2, width = 10)
    lbl4.grid(row = 5, column = 7)

    lbl5 = tk.Label(ice_calendar, text = "5", height = 2, width = 10)
    lbl5.grid(row = 5, column = 8)

    lbl6 = tk.Label(ice_calendar, text = "6", height = 2, width = 10)
    lbl6.grid(row = 5, column = 9)

    lbl7 = tk.Label(ice_calendar, text = "7", height = 2, width = 10)
    lbl7.grid(row = 5, column = 10)

    lbl8 = tk.Label(ice_calendar, text = "8", height = 2, width = 10)
    lbl8.grid(row = 5, column = 11)

    lbl9 = tk.Label(ice_calendar, text = "9", height = 2, width = 10)
    lbl9.grid(row = 5, column = 12)

    lbl10 = tk.Label(ice_calendar, text = "10", height = 2, width = 10)
    lbl10.grid(row = 5, column = 13)

    lbl11 = tk.Label(ice_calendar, text = "11", height = 2, width = 10)
    lbl11.grid(row = 7, column = 7)

    lbl12 = tk.Label(ice_calendar, text = "12", height = 2, width = 10)
    lbl12.grid(row = 7, column = 8)

    lbl13 = tk.Label(ice_calendar, text = "13", height = 2, width = 10)
    lbl13.grid(row = 7, column = 9)

    lbl14 = tk.Label(ice_calendar, text = "14", height = 2, width = 10)
    lbl14.grid(row = 7, column = 10)

    lbl15 = tk.Label(ice_calendar, text = "15", height = 2, width = 10)
    lbl15.grid(row = 7, column = 11)

    lbl16 = tk.Label(ice_calendar, text = "16", height = 2, width = 10)
    lbl16.grid(row = 7, column = 12)

    lbl17 = tk.Label(ice_calendar, text = "17", height = 2, width = 10)
    lbl17.grid(row = 7, column = 13)

    lbl18 = tk.Label(ice_calendar, text = "18", height = 2, width = 10)
    lbl18.grid(row = 9, column = 7)

    lbl19 = tk.Label(ice_calendar, text = "19", height = 2, width = 10)
    lbl19.grid(row = 9, column = 8)

    lbl20 = tk.Label(ice_calendar, text = "20", height = 2, width = 10)
    lbl20.grid(row = 9, column = 9)

    lbl21 = tk.Label(ice_calendar, text = "21", height = 2, width = 10)
    lbl21.grid(row = 9, column = 10)

    lbl22 = tk.Label(ice_calendar, text = "22", height = 2, width = 10)
    lbl22.grid(row = 9, column = 11)

    lbl23 = tk.Label(ice_calendar, text = "23", height = 2, width = 10)
    lbl23.grid(row = 9, column = 12)

    lbl24 = tk.Label(ice_calendar, text = "24", height = 2, width = 10)
    lbl24.grid(row = 9, column = 13)

    lbl25 = tk.Label(ice_calendar, text = "25", height = 2, width = 10)
    lbl25.grid(row = 11, column = 7)

    lbl26 = tk.Label(ice_calendar, text = "26", height = 2, width = 10)
    lbl26.grid(row = 11, column = 8)

    lbl27 = tk.Label(ice_calendar, text = "27", height = 2, width = 10)
    lbl27.grid(row = 11, column = 9)

    lbl28 = tk.Label(ice_calendar, text = "28", height = 2, width = 10)
    lbl28.grid(row = 11, column = 10)

    lbl29 = tk.Label(ice_calendar, text = "29", height = 2, width = 10)
    lbl29.grid(row = 11, column = 11)

    lbl30 = tk.Label(ice_calendar, text = "30", height = 2, width = 10)
    lbl30.grid(row = 11, column = 12)

    # Editable text boxes to place the events into
    text1 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text1.grid(row = 4, column = 11)

    text2 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text2.grid(row = 4, column = 12)

    text3 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text3.grid(row = 4, column = 13)

    text4 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text4.grid(row = 6, column = 7)

    text5 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text5.grid(row = 6, column = 8)

    text6 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text6.grid(row = 6, column = 9)

    text7 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text7.grid(row = 6, column = 10)

    text8 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text8.grid(row = 6, column = 11)

    text9 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text9.grid(row = 6, column = 12)

    text10 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text10.grid(row = 6, column = 13)

    text11 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text11.grid(row = 8, column = 7)

    text12 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text12.grid(row = 8, column = 8)

    text13 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text13.grid(row = 8, column = 9)

    text14 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text14.grid(row = 8, column = 10)

    text15 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text15.grid(row = 8, column = 11)

    text16 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text16.grid(row = 8, column = 12)

    text17 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text17.grid(row = 8, column = 13)

    text18 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text18.grid(row = 10, column = 7)

    text19 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text19.grid(row = 10, column = 8)

    text20 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text20.grid(row = 10, column = 9)

    text21 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text21.grid(row = 10, column = 10)

    text22 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text22.grid(row = 10, column = 11)

    text23 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text23.grid(row = 10, column = 12)

    text24 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text24.grid(row = 10, column = 13)

    text25 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text25.grid(row = 12, column = 7)

    text26 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text26.grid(row = 12, column = 8)

    text27 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text27.grid(row = 12, column = 9)

    text28 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text28.grid(row = 12, column = 10)

    text29 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text29.grid(row = 12, column = 11)

    text30 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text30.grid(row = 12, column = 12)

    homeBtn = tk.Button(ice_calendar, text = "Return to Home Page", command = goHome)
    homeBtn.grid(row = 13, column = 9, columnspan = 3)


    # Bind it so that should a user double click into the text box, it opens an event sign up window
    text1.bind("<Double-Button-1>", lambda event: SignUp(event, "1"))
    text2.bind('<Double-Button-1>', lambda event: SignUp(event, "2"))
    text3.bind('<Double-Button-1>', lambda event: SignUp(event, "3"))
    text4.bind('<Double-Button-1>', lambda event: SignUp(event, "4"))
    text5.bind('<Double-Button-1>', lambda event: SignUp(event, "5"))
    text6.bind('<Double-Button-1>', lambda event: SignUp(event, "6"))
    text7.bind('<Double-Button-1>', lambda event: SignUp(event, "7"))
    text8.bind('<Double-Button-1>', lambda event: SignUp(event, "8"))
    text9.bind('<Double-Button-1>', lambda event: SignUp(event, "9"))
    text10.bind('<Double-Button-1>', lambda event: SignUp(event, "10"))
    text11.bind('<Double-Button-1>', lambda event: SignUp(event, "11"))
    text12.bind('<Double-Button-1>', lambda event: SignUp(event, "12"))
    text13.bind('<Double-Button-1>', lambda event: SignUp(event, "13"))
    text14.bind('<Double-Button-1>', lambda event: SignUp(event, "14"))
    text15.bind('<Double-Button-1>', lambda event: SignUp(event, "15"))
    text16.bind('<Double-Button-1>', lambda event: SignUp(event, "16"))
    text17.bind('<Double-Button-1>', lambda event: SignUp(event, "17"))
    text18.bind('<Double-Button-1>', lambda event: SignUp(event, "18"))
    text19.bind('<Double-Button-1>', lambda event: SignUp(event, "19"))
    text20.bind('<Double-Button-1>', lambda event: SignUp(event, "20"))
    text21.bind('<Double-Button-1>', lambda event: SignUp(event, "21"))
    text22.bind('<Double-Button-1>', lambda event: SignUp(event, "22"))
    text23.bind('<Double-Button-1>', lambda event: SignUp(event, "23"))
    text24.bind('<Double-Button-1>', lambda event: SignUp(event, "24"))
    text25.bind('<Double-Button-1>', lambda event: SignUp(event, "25"))
    text26.bind('<Double-Button-1>', lambda event: SignUp(event, "26"))
    text27.bind('<Double-Button-1>', lambda event: SignUp(event, "27"))
    text28.bind('<Double-Button-1>', lambda event: SignUp(event, "28"))
    text29.bind('<Double-Button-1>', lambda event: SignUp(event, "29"))
    text30.bind('<Double-Button-1>', lambda event: SignUp(event, "30"))
   

def open_ice_calendar_not_logged_in():
    
    # Go Home
    def goHome():
        ice_calendar.destroy()
        home_page.open_home_screen_without_user_logged_in()

    # Open a new window to sign up for the event
    def SignUp(event):
        messagebox.showerror('Error','You must be logged in to an account to register for an event.')
        ice_calendar.destroy()
        login_page.user_login()

    ice_calendar = tk.Tk()
    ice_calendar.title("Calendar")
    ice_calendar.geometry("1920x1080")

    # Labels for the month and days along with placemnt 
    month =tk.Label(ice_calendar, text = "June 2023", height = 3, width = 10, font = 'bold')
    sunday = tk.Label(ice_calendar, text = "Sunday", height = 2, width = 10)
    monday = tk.Label(ice_calendar, text = "Monday", height = 2, width = 10)
    tuesday= tk.Label(ice_calendar, text = "Tuesday", height = 2, width = 10)
    wednesday = tk.Label(ice_calendar, text = "Wednesday", height = 2, width = 10)
    thursday = tk.Label(ice_calendar, text = "Thursday", height = 2, width = 10)
    friday = tk.Label(ice_calendar, text = "Friday", height = 2, width = 10)
    saturday = tk.Label(ice_calendar, text = "Saturday", height = 2, width = 10)
    
    month.grid(row = 1, column = 9, columnspan = 7, sticky = 'ew')
    sunday.grid(row = 2, column = 7)
    monday.grid(row = 2, column = 8)
    tuesday.grid(row = 2, column = 9)
    wednesday.grid(row = 2, column = 10)
    thursday.grid(row = 2, column = 11)
    friday.grid(row = 2, column = 12)
    saturday.grid(row = 2, column = 13)
    

    # Fillers
    fillerS = tk.Label(ice_calendar, height = 2, width = 10)
    fillerM = tk.Label(ice_calendar, height = 2, width = 10)
    fillerT = tk.Label(ice_calendar, height = 2, width = 10)
    fillerW = tk.Label(ice_calendar, height = 2, width = 10)
    filler1 = tk.Label(ice_calendar, height = 5, width = 10)
    filler2 = tk.Label(ice_calendar, height = 5, width = 10)
    filler3 = tk.Label(ice_calendar, height = 5, width = 10)
    filler4 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol1 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol2 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol3 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol4 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol5 = tk.Label(ice_calendar, height = 5, width = 10)
    fillerCol6 = tk.Label(ice_calendar, height = 5, width = 10)

    fillerS.grid(row = 3, column = 7)
    fillerM.grid(row = 3, column = 8)
    fillerT.grid(row = 3, column = 9)
    fillerW.grid(row = 3, column = 10)
    filler1.grid(row = 4, column = 7)
    filler2.grid(row = 4, column = 8)
    filler3.grid(row = 4, column = 9)
    filler4.grid(row = 4, column = 10)
    fillerCol1.grid(row = 1, column = 1)
    fillerCol2.grid(row = 1, column = 2)
    fillerCol3.grid(row = 1, column = 3)
    fillerCol4.grid(row = 1, column = 4)
    fillerCol5.grid(row = 1, column = 5)
    fillerCol6.grid(row = 1, column = 6)


    # Labels for the numbers of the days in the month
    lbl1 = tk.Label(ice_calendar, text = "1", height = 2, width = 10)
    lbl1.grid(row = 3, column = 11)

    lbl2 = tk.Label(ice_calendar, text = "2", height = 2, width = 10)
    lbl2.grid(row = 3, column = 12)

    lbl3 = tk.Label(ice_calendar, text = "3", height = 2, width = 10)
    lbl3.grid(row = 3, column = 13)

    lbl4 = tk.Label(ice_calendar, text = "4", height = 2, width = 10)
    lbl4.grid(row = 5, column = 7)

    lbl5 = tk.Label(ice_calendar, text = "5", height = 2, width = 10)
    lbl5.grid(row = 5, column = 8)

    lbl6 = tk.Label(ice_calendar, text = "6", height = 2, width = 10)
    lbl6.grid(row = 5, column = 9)

    lbl7 = tk.Label(ice_calendar, text = "7", height = 2, width = 10)
    lbl7.grid(row = 5, column = 10)

    lbl8 = tk.Label(ice_calendar, text = "8", height = 2, width = 10)
    lbl8.grid(row = 5, column = 11)

    lbl9 = tk.Label(ice_calendar, text = "9", height = 2, width = 10)
    lbl9.grid(row = 5, column = 12)

    lbl10 = tk.Label(ice_calendar, text = "10", height = 2, width = 10)
    lbl10.grid(row = 5, column = 13)

    lbl11 = tk.Label(ice_calendar, text = "11", height = 2, width = 10)
    lbl11.grid(row = 7, column = 7)

    lbl12 = tk.Label(ice_calendar, text = "12", height = 2, width = 10)
    lbl12.grid(row = 7, column = 8)

    lbl13 = tk.Label(ice_calendar, text = "13", height = 2, width = 10)
    lbl13.grid(row = 7, column = 9)

    lbl14 = tk.Label(ice_calendar, text = "14", height = 2, width = 10)
    lbl14.grid(row = 7, column = 10)

    lbl15 = tk.Label(ice_calendar, text = "15", height = 2, width = 10)
    lbl15.grid(row = 7, column = 11)

    lbl16 = tk.Label(ice_calendar, text = "16", height = 2, width = 10)
    lbl16.grid(row = 7, column = 12)

    lbl17 = tk.Label(ice_calendar, text = "17", height = 2, width = 10)
    lbl17.grid(row = 7, column = 13)

    lbl18 = tk.Label(ice_calendar, text = "18", height = 2, width = 10)
    lbl18.grid(row = 9, column = 7)

    lbl19 = tk.Label(ice_calendar, text = "19", height = 2, width = 10)
    lbl19.grid(row = 9, column = 8)

    lbl20 = tk.Label(ice_calendar, text = "20", height = 2, width = 10)
    lbl20.grid(row = 9, column = 9)

    lbl21 = tk.Label(ice_calendar, text = "21", height = 2, width = 10)
    lbl21.grid(row = 9, column = 10)

    lbl22 = tk.Label(ice_calendar, text = "22", height = 2, width = 10)
    lbl22.grid(row = 9, column = 11)

    lbl23 = tk.Label(ice_calendar, text = "23", height = 2, width = 10)
    lbl23.grid(row = 9, column = 12)

    lbl24 = tk.Label(ice_calendar, text = "24", height = 2, width = 10)
    lbl24.grid(row = 9, column = 13)

    lbl25 = tk.Label(ice_calendar, text = "25", height = 2, width = 10)
    lbl25.grid(row = 11, column = 7)

    lbl26 = tk.Label(ice_calendar, text = "26", height = 2, width = 10)
    lbl26.grid(row = 11, column = 8)

    lbl27 = tk.Label(ice_calendar, text = "27", height = 2, width = 10)
    lbl27.grid(row = 11, column = 9)

    lbl28 = tk.Label(ice_calendar, text = "28", height = 2, width = 10)
    lbl28.grid(row = 11, column = 10)

    lbl29 = tk.Label(ice_calendar, text = "29", height = 2, width = 10)
    lbl29.grid(row = 11, column = 11)

    lbl30 = tk.Label(ice_calendar, text = "30", height = 2, width = 10)
    lbl30.grid(row = 11, column = 12)

    # Editable text boxes to place the events into
    text1 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text1.grid(row = 4, column = 11)

    text2 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text2.grid(row = 4, column = 12)

    text3 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text3.grid(row = 4, column = 13)

    text4 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text4.grid(row = 6, column = 7)

    text5 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text5.grid(row = 6, column = 8)

    text6 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text6.grid(row = 6, column = 9)

    text7 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text7.grid(row = 6, column = 10)

    text8 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text8.grid(row = 6, column = 11)

    text9 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text9.grid(row = 6, column = 12)

    text10 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text10.grid(row = 6, column = 13)

    text11 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text11.grid(row = 8, column = 7)

    text12 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text12.grid(row = 8, column = 8)

    text13 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text13.grid(row = 8, column = 9)

    text14 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text14.grid(row = 8, column = 10)

    text15 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text15.grid(row = 8, column = 11)

    text16 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text16.grid(row = 8, column = 12)

    text17 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text17.grid(row = 8, column = 13)

    text18 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text18.grid(row = 10, column = 7)

    text19 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text19.grid(row = 10, column = 8)

    text20 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text20.grid(row = 10, column = 9)

    text21 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text21.grid(row = 10, column = 10)

    text22 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text22.grid(row = 10, column = 11)

    text23 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text23.grid(row = 10, column = 12)

    text24 = tk.Label(ice_calendar, text = "18+ Drop In 9:00am - 10:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text24.grid(row = 10, column = 13)

    text25 = tk.Label(ice_calendar, text = "Free Skate 2:30pm - 3:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text25.grid(row = 12, column = 7)

    text26 = tk.Label(ice_calendar, text = "Free Skate 8:00am - 9:00am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text26.grid(row = 12, column = 8)

    text27 = tk.Label(ice_calendar, text = "Hockey Game 7:00am - 8:30am", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text27.grid(row = 12, column = 9)

    text28 = tk.Label(ice_calendar, text = "Hockey Game 6:00pm - 7:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text28.grid(row = 12, column = 10)

    text29 = tk.Label(ice_calendar, text = "Free Skate 12:00pm - 1:00pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text29.grid(row = 12, column = 11)

    text30 = tk.Label(ice_calendar, text = "Hockey Game 12:00pm - 1:30pm", wraplength = 75, justify = LEFT, height = 5, width = 10, bg = "white", relief = "groove", borderwidth = 1)
    text30.grid(row = 12, column = 12)

    homeBtn = tk.Button(ice_calendar, text = "Return to Home Page", command = goHome)
    homeBtn.grid(row = 13, column = 9, columnspan = 3)


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