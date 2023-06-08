from pathlib import Path
from tkinter import Tk, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"src\img")
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def buttonpack(canvas):
    components = {}

    # Assign the PhotoImage object to an attribute of the canvas
    canvas.new_image_9 = PhotoImage(file=relative_to_assets("new_9.png"))
    components['new_9'] = Button(
        canvas,
        image=canvas.new_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("new_9 clicked"),
        relief="flat"
    )
    components['new_9'].place(
        x=1102.0,
        y=274.0,
        width=331.0,
        height=559.0
    )
    return canvas
