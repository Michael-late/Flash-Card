from tkinter import *
import os
import sys 
import pandas as pd
from random import choice,randint

BACKGROUND_COLOR = "#B1DDC6"
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder when bundled
    except Exception:
        base_path = os.path.abspath(".")  # when running normally
    return os.path.join(base_path, relative_path)

def Change(save):
    indexs = randint(0,101)
    try:
        df = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        df = pd.read_csv("data/french_words.csv")
        os.makedirs("data/",exist_ok=True)
        df.to_csv("data/words_to_learn.csv",index=False)        
    finally:
        frenchDict = df.to_dict(orient="records")
        canvas.itemconfig(canvImg, image=front_img)
        canvas.itemconfig(titleLabel,text="French",fill="black")
        canvas.itemconfig(wordLabel,text=frenchDict[indexs]["French"],fill="black")
        if save:
            SaveProgress(indexs,frenchDict)
        timer(df,indexs)

def SaveProgress(i, frenchDict):
    frenchDict.pop(i)
    # print(len(frenchDict))  # number of cards LEFT to learn
    data = pd.DataFrame(frenchDict)
    data.to_csv("data/words_to_learn.csv", index=False)

def flip(df,i):
    frenchDict = df.to_dict(orient="records")
    canvas.itemconfig(canvImg, image=back_img)
    canvas.itemconfig(titleLabel,text="English", fill="White")
    canvas.itemconfig(wordLabel,text=frenchDict[i]["English"],fill="white")

def timer(df, i):
    window.after(3000, flip, df, i)

window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
front_img = PhotoImage(file=resource_path("images/card_front.png"))
back_img = PhotoImage(file=resource_path("images/card_back.png"))
canvImg = canvas.create_image(400,263,image=front_img)
titleLabel = canvas.create_text(400,150, text="Title",font=("Ariel",40,"italic"))
wordLabel = canvas.create_text(400,263, text="trouve",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2,sticky=EW)

wrongIMG = PhotoImage(file="images/wrong.png")
wrongBTN = Button(image=wrongIMG, highlightthickness=0, command=Change)
wrongBTN.grid(row=1,column=0)

rightIMG = PhotoImage(file="images/correct.png")
rightBTN = Button(image=rightIMG, highlightthickness=0, command=lambda:Change(True))
rightBTN.grid(row=1,column=1)



window.mainloop()