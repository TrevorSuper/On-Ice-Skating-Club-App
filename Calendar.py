# Test
# Placemnt and sizing and toggled editablilty of textboxes
import tkinter as tk

# Define the functionality of the 'save' and 'add event' buttons 
def addEvent():
    text1.config(state='normal')
    text2.config(state='normal')
    text3.config(state='normal')
    text4.config(state='normal')
    text5.config(state='normal')
    text6.config(state='normal')
    text7.config(state='normal')
    text8.config(state='normal')
    text9.config(state='normal')
    text10.config(state='normal')
    text11.config(state='normal')
    text12.config(state='normal')
    text13.config(state='normal')
    text14.config(state='normal')
    text15.config(state='normal')
    text16.config(state='normal')
    text17.config(state='normal')
    text18.config(state='normal')
    text19.config(state='normal')
    text20.config(state='normal')
    text21.config(state='normal')
    text22.config(state='normal')
    text23.config(state='normal')
    text24.config(state='normal')
    text25.config(state='normal')
    text26.config(state='normal')
    text27.config(state='normal')
    text28.config(state='normal')
    text29.config(state='normal')
    text30.config(state='normal')

def saveEvent():
    text1.config(state='disabled')
    text2.config(state='disabled')
    text3.config(state='disabled')
    text4.config(state='disabled')
    text5.config(state='disabled')
    text6.config(state='disabled')
    text7.config(state='disabled')
    text8.config(state='disabled')
    text9.config(state='disabled')
    text10.config(state='disabled')
    text11.config(state='disabled')
    text12.config(state='disabled')
    text13.config(state='disabled')
    text14.config(state='disabled')
    text15.config(state='disabled')
    text16.config(state='disabled')
    text17.config(state='disabled')
    text18.config(state='disabled')
    text19.config(state='disabled')
    text20.config(state='disabled')
    text21.config(state='disabled')
    text22.config(state='disabled')
    text23.config(state='disabled')
    text24.config(state='disabled')
    text25.config(state='disabled')
    text26.config(state='disabled')
    text27.config(state='disabled')
    text28.config(state='disabled')
    text29.config(state='disabled')
    text30.config(state='disabled')

# Open a new window to sign up for the event
def SignUp(event):
    signUpWindow = tk.Toplevel()
    signUpWindow.title("Sign Up For Event ?")
    signUpWindow.config(width=300, height=200)

    buttonCancel = tk.Button(
        signUpWindow,
        text="Cancel",
        command=signUpWindow.destroy
    )

    buttonSignUp = tk.Button(
        signUpWindow,
        text="Yes",
        command=signUpWindow.destroy
    )

    buttonCancel.grid(row= 10,column= 10)
    buttonSignUp.grid(row= 10,column=11)
    



root = tk.Tk()
root.title("July 2023")

# Labels for the month and days along with placemnt 
month =tk.Label(root, text= "June 2023", height = 3, width=10, font='bold')
sunday = tk.Label(root, text = "Sunday",height = 2, width = 10)
monday = tk.Label(root, text = "Monday",height = 2, width = 10)
tuesday= tk.Label(root, text = "Tuesday",height = 2, width = 10)
wednesday = tk.Label(root, text = "Wednesday",height = 2, width = 10)
thursday = tk.Label(root, text = "Thursday",height = 2, width = 10)
friday = tk.Label(root, text = "Friday",height = 2, width = 10)
saturday = tk.Label(root, text = "Saturday",height = 2, width = 10)

month.grid(row=1,column=3,columnspan=3, sticky='ew')
sunday.grid(row=2, column=1)
monday.grid(row=2, column=2)
tuesday.grid(row=2, column=3)
wednesday.grid(row=2, column=4)
thursday.grid(row=2, column=5)
friday.grid(row=2, column=6)
saturday.grid(row=2, column=7)


# Fillers
fillerS = tk.Label(root, height=2, width =10)
fillerM = tk.Label(root, height=2, width =10)
fillerT = tk.Label(root, height=2, width =10)
fillerW = tk.Label(root, height=2, width =10)
filler1 = tk.Label(root, height=5, width=10)
filler2 = tk.Label(root, height=5, width=10)
filler3 = tk.Label(root, height=5, width=10)
filler4 = tk.Label(root, height=5, width=10)

fillerS.grid(row=3, column=1)
fillerM.grid(row=3, column=2)
fillerT.grid(row=3, column=3)
fillerW.grid(row=3, column=4)
filler1.grid(row=4,column=1)
filler2.grid(row=4,column=2)
filler3.grid(row=4,column=3)
filler4.grid(row=4,column=4)


# Labels for the numbers of the days in the month
lbl1 = tk.Label(root, text="1",height=2, width=10)
lbl1.grid(row=3, column=5)

lbl2 = tk.Label(root, text="2",height=2, width=10)
lbl2.grid(row=3, column=6)

lbl3 = tk.Label(root, text="3",height=2, width=10)
lbl3.grid(row=3, column=7)

lbl4 = tk.Label(root, text="4",height=2, width=10)
lbl4.grid(row=5, column=1)

lbl5 = tk.Label(root, text="5",height=2, width=10)
lbl5.grid(row=5, column=2)

lbl6 = tk.Label(root, text="6",height=2, width=10)
lbl6.grid(row=5, column=3)

lbl7 = tk.Label(root, text="7",height=2, width=10)
lbl7.grid(row=5, column=4)

lbl8 = tk.Label(root, text="8",height=2, width=10)
lbl8.grid(row=5, column=5)

lbl9 = tk.Label(root, text="9",height=2, width=10)
lbl9.grid(row=5, column=6)

lbl10 = tk.Label(root, text="10",height=2, width=10)
lbl10.grid(row=5, column=7)

lbl11 = tk.Label(root, text="11",height=2, width=10)
lbl11.grid(row=7, column=1)

lbl12 = tk.Label(root, text="12",height=2, width=10)
lbl12.grid(row=7, column=2)

lbl13 = tk.Label(root, text="13",height=2, width=10)
lbl13.grid(row=7, column=3)

lbl14 = tk.Label(root, text="14",height=2, width=10)
lbl14.grid(row=7, column=4)

lbl15 = tk.Label(root, text="15",height=2, width=10)
lbl15.grid(row=7, column=5)

lbl16 = tk.Label(root, text="16",height=2, width=10)
lbl16.grid(row=7, column=6)

lbl17 = tk.Label(root, text="17",height=2, width=10)
lbl17.grid(row=7, column=7)

lbl18 = tk.Label(root, text="18",height=2, width=10)
lbl18.grid(row=9, column=1)

lbl19 = tk.Label(root, text="19",height=2, width=10)
lbl19.grid(row=9, column=2)

lbl10 = tk.Label(root, text="20",height=2, width=10)
lbl10.grid(row=9, column=3)

lbl1 = tk.Label(root, text="21",height=2, width=10)
lbl1.grid(row=9, column=4)

lbl2 = tk.Label(root, text="22",height=2, width=10)
lbl2.grid(row=9, column=5)

lbl3 = tk.Label(root, text="23",height=2, width=10)
lbl3.grid(row=9, column=6)

lbl4 = tk.Label(root, text="24",height=2, width=10)
lbl4.grid(row=9, column=7)

lbl5 = tk.Label(root, text="25",height=2, width=10)
lbl5.grid(row=11, column=1)

lbl6 = tk.Label(root, text="26",height=2, width=10)
lbl6.grid(row=11, column=2)

lbl7 = tk.Label(root, text="27",height=2, width=10)
lbl7.grid(row=11, column=3)

lbl8 = tk.Label(root, text="28",height=2, width=10)
lbl8.grid(row=11, column=4)

lbl9 = tk.Label(root, text="29",height=2, width=10)
lbl9.grid(row=11, column=5)

lbl10 = tk.Label(root, text="30",height=2, width=10)
lbl10.grid(row=11, column=6)



# Editable text boxes to place the events into  
text1 = tk.Text(root, height=5, width=10, state='disabled')
text1.grid(row=4, column=5)

text2 = tk.Text(root, height=5, width=10, state='disabled')
text2.grid(row=4, column=6)

text3 = tk.Text(root, height=5, width=10, state='disabled')
text3.grid(row=4, column=7)

text4 = tk.Text(root, height=5, width=10, state='disabled')
text4.grid(row=6, column=1)

text5 = tk.Text(root, height=5, width=10, state='disabled')
text5.grid(row=6, column=2)

text6 = tk.Text(root, height=5, width=10, state='disabled')
text6.grid(row=6, column=3)

text7 = tk.Text(root, height=5, width=10, state='disabled')
text7.grid(row=6, column=4)

text8 = tk.Text(root, height=5, width=10, state='disabled')
text8.grid(row=6, column=5)

text9 = tk.Text(root, height=5, width=10, state='disabled')
text9.grid(row=6, column=6)

text10 = tk.Text(root, height=5, width=10, state='disabled')
text10.grid(row=6, column=7)

text11 = tk.Text(root, height=5, width=10, state='disabled')
text11.grid(row=8, column=1)

text12 = tk.Text(root, height=5, width=10, state='disabled')
text12.grid(row=8, column=2)

text13 = tk.Text(root, height=5, width=10, state='disabled')
text13.grid(row=8, column=3)

text14 = tk.Text(root, height=5, width=10, state='disabled')
text14.grid(row=8, column=4)

text15 = tk.Text(root, height=5, width=10, state='disabled')
text15.grid(row=8, column=5)

text16 = tk.Text(root, height=5, width=10, state='disabled')
text16.grid(row=8, column=6)

text17 = tk.Text(root, height=5, width=10, state='disabled')
text17.grid(row=8, column=7)

text18 = tk.Text(root, height=5, width=10, state='disabled')
text18.grid(row=10, column=1)

text19 = tk.Text(root, height=5, width=10, state='disabled')
text19.grid(row=10, column=2)

text20 = tk.Text(root, height=5, width=10, state='disabled')
text20.grid(row=10, column=3)

text21 = tk.Text(root, height=5, width=10, state='disabled')
text21.grid(row=10, column=4)

text22 = tk.Text(root, height=5, width=10, state='disabled')
text22.grid(row=10, column=5)

text23 = tk.Text(root, height=5, width=10, state='disabled')
text23.grid(row=10, column=6)

text24 = tk.Text(root, height=5, width=10, state='disabled')
text24.grid(row=10, column=7)

text25 = tk.Text(root, height=5, width=10, state='disabled')
text25.grid(row=12, column=1)

text26 = tk.Text(root, height=5, width=10, state='disabled')
text26.grid(row=12, column=2)

text27 = tk.Text(root, height=5, width=10, state='disabled')
text27.grid(row=12, column=3)

text28 = tk.Text(root, height=5, width=10, state='disabled')
text28.grid(row=12, column=4)

text29 = tk.Text(root, height=5, width=10, state='disabled')
text29.grid(row=12, column=5)

text30 = tk.Text(root, height=5, width=10, state='disabled')
text30.grid(row=12, column=6)


# Save and add event buttons 
saveBtn = tk.Button(root, text="Save", command=saveEvent)
saveBtn.grid(row=13, column=3)

saveBtn = tk.Button(root, text="Add Event", command=addEvent)
saveBtn.grid(row=13, column=5)

# Bind it so that should a user click into the text box, it opens an event sign up window 
text1.bind('<Double-Button-1>', SignUp)

root.mainloop()