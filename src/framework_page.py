from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from tkinter import *
import webbrowser
import homepage_buttons



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"img")

def open_facebook():
    webbrowser.open("https://www.facebook.com/detroitSkatingClub/")

def open_instagram():
    webbrowser.open("https://www.instagram.com/dscclub/?hl=en")

def open_twitter():
    webbrowser.open("https://twitter.com/dscclub?lang=en")

def show_buttons():
    components = buttonpack(canvas)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def frame_gui(root):
    root.geometry("1920x1080")
    root.configure(bg="#FFFFFF")

    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Create and store the images and buttons as attributes of the canvas
    canvas.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.image_1 = canvas.create_image(
        960.0000000000001,
        613.0,
        image=canvas.image_image_1
    )
    canvas.create_rectangle(
        1.1368683772161603e-13,
        5.684341886080802e-14,
        1920.0,
        180.00000000000006,
        fill="#006196",
        outline=""
    )

    canvas.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    canvas.button_1 = Button(
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("test"),
        relief="flat"
    )
    canvas.button_1.place(
        x=1417.0,
        y=93.99999999999994,
        width=214.0751953125,
        height=79.0
    )
    canvas.create_rectangle(
        1634.0,
        93.99999999999994,
        1920.0,
        172.99999999999994,
        fill="#002337",
        outline=""
    )


    # Load the image for button_2
    button_image_2_path = relative_to_assets("button_2.png")
    canvas.button_image_2 = PhotoImage(file=button_image_2_path)

    # Create button_2
    canvas.button_2 = Button(
    image=canvas.button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= print("login button clicked"), # this automatically runs once when main.py is run and can't be clicked again
    relief="flat"
)

# Place button_2 on the canvas
    canvas.button_2.place(
    x=1.1368683772161603e-13,
    y=93.99999999999994,
    width=330.0,
    height=79.0
)


    # Load the image for Meet the team
    Meet_the_team_image_path = relative_to_assets("button_3.png")
    canvas.Meet_the_team_image = PhotoImage(file=Meet_the_team_image_path)

    # Create button_3
    canvas.button_3 = Button(
        image=canvas.Meet_the_team_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Meet the team"),
        relief="flat"
    )

    # Place button_3 on the canvas
    canvas.button_3.place(
        x=1200.0,
        y=93.99999999999994,
        width=214.0751953125,
        height=79.0
    )

    # Load the image for button_4
    button_image_4_path = relative_to_assets("button_4.png")
    canvas.button_image_4 = PhotoImage(file=button_image_4_path)

    # Create button_4
    canvas.button_4 = Button(
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )

    # Place button_4 on the canvas
    canvas.button_4.place(
        x=983.0000000000001,
        y=93.99999999999994,
        width=214.0751953125,
        height=79.0
    )

    # Load the image for button_5
    button_image_5_path = relative_to_assets("button_5.png")
    canvas.button_image_5 = PhotoImage(file=button_image_5_path)

    # Create button_5
    canvas.button_5 = Button(
        image=canvas.button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )

    # Place button_5 on the canvas
    canvas.button_5.place(
        x=767.0000000000001,
        y=93.99999999999994,
        width=214.07513427734375,
        height=79.0
    )


    # Load the image for button_6
    button_image_6_path = relative_to_assets("button_6.png")
    canvas.button_image_6 = PhotoImage(file=button_image_6_path)

    # Create button_6
    canvas.button_6 = Button(
        image=canvas.button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )

    # Place button_6 on the canvas
    canvas.button_6.place(
        x=550.0000000000001,
        y=93.99999999999994,
        width=214.07513427734375,
        height=79.0
    )

    # Load the image for button_7
    button_image_7_path = relative_to_assets("button_7.png")
    canvas.button_image_7 = PhotoImage(file=button_image_7_path)

    # Create button_7
    canvas.button_7 = Button(
        image=canvas.button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )

    # Place button_7 on the canvas
    canvas.button_7.place(
        x=333.0000000000001,
        y=93.99999999999994,
        width=214.07513427734375,
        height=79.0
    )

    # Load the image for button_8
    button_image_8_path = relative_to_assets("button_8.png")
    canvas.button_image_8 = PhotoImage(file=button_image_8_path)

    # Create button_8
    canvas.button_8 = Button(
        image=canvas.button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_facebook(),
        relief="flat"
    )

    # Place button_8 on the canvas
    canvas.button_8.place(
        x=1663.0,
        y=107.99999999999994,
        width=54.0,
        height=54.0
    )

    # Load the image for button_9
    button_image_9_path = relative_to_assets("button_9.png")
    canvas.button_image_9 = PhotoImage(file=button_image_9_path)

    # Create button_9
    canvas.button_9 = Button(
        image=canvas.button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_twitter(),
        relief="flat"
    )

    # Place button_9 on the canvas
    canvas.button_9.place(
        x=1752.0,
        y=107.99999999999994,
        width=54.0,
        height=54.0
    )

    # Load the image for button_10
    button_image_10_path = relative_to_assets("button_10.png")
    canvas.button_image_10 = PhotoImage(file=button_image_10_path)

    # Create button_10
    canvas.button_10 = Button(
        image=canvas.button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_instagram(),
        relief="flat"
    )

    # Place button_10 on the canvas
    canvas.button_10.place(
        x=1837.0,
        y=107.99999999999994,
        width=54.0,
        height=54.0
    )



    canvas.pack()  # Add this line to pack the canvas widget

    return canvas