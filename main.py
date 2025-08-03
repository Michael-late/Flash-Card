from tkinter import *
import os
import sys 

BACKGROUND_COLOR = "#B1DDC6"
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder when bundled
    except Exception:
        base_path = os.path.abspath(".")  # when running normally
    return os.path.join(base_path, relative_path)

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
img = PhotoImage(file=resource_path("images\card_front.png"))
canvas.create_image(400,263,image=img)
canvas.grid(row=0,column=0,columnspan=2,sticky=EW)

wrongIMG = PhotoImage(file="images\wrong.png")
wrongBTN = Button(image=wrongIMG, highlightthickness=0)
wrongBTN.grid(row=1,column=0)

rightIMG = PhotoImage(file="images\correct.png")
rightBTN = Button(image=rightIMG, highlightthickness=0)
rightBTN.grid(row=1,column=1)

window.mainloop()