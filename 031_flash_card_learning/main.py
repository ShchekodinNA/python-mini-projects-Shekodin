from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT = "tahoma"
FONT_SIZE_TITLE = 24
FONT_SIZE_DESCR = 18
FONT_STYLE_TITLE = "bold"
PATH_BEGIN_FILE = "data/eng_to_rus.csv"
PATH_SAVE_FILE = "data/words_to_learn.csv"
TIME_TO_REMEMBER = 3000
COLOR_STDNG_WRLD = "black"
COLOR_DSCRPTN = "white"
ENCODING = "windows-1251"
PATH_CARD_BACK = "images/card_back.png"
PATH_CARD_FRNT = "images/card_front.png"
PATH_RIGHT = "images/right.png"
PATH_WRONG = "images/wrong.png"

timer = None
current_index = 0


# ++++++++++++++++++++++++++++++++++++++++++++++ CARD GENERATION ++++++++++++++++++++++++++++++++++


def word_gen():
    global timer, current_index
    if len(list_df) == 0:
        cnvs.itemconfig(cnvs_card_lang, text="", fill=COLOR_STDNG_WRLD)
        cnvs.itemconfig(cnvs_card_text, text="You learned all list. Congrats!", fill=COLOR_STDNG_WRLD)
        cnvs.itemconfig(cnvs_img, image=img_crd_frnt)
        if os.path.exists(PATH_SAVE_FILE):
            os.remove(PATH_SAVE_FILE)
        return
    if timer is not None:
        wd.after_cancel(timer)
    current_index = random.randint(0, len(list_df) - 1)
    cnvs.itemconfig(cnvs_card_lang, text=f"{df.columns[0]}", fill=COLOR_STDNG_WRLD)
    cnvs.itemconfig(cnvs_card_text, text=f"{list_df[current_index][df.columns[0]].title()}", fill=COLOR_STDNG_WRLD)
    cnvs.itemconfig(cnvs_img, image=img_crd_frnt)
    timer = wd.after(TIME_TO_REMEMBER, rotate_card, df.columns[1], list_df[current_index][df.columns[1]].title())


def click_yes():
    if len(list_df) != 0:
        del list_df[current_index]
        word_gen()


def window_close():
    if len(list_df) != 0:
        exit_answer = messagebox.askyesnocancel(title="Exit", message="You want save your result?")
        if exit_answer is None:
            return
        elif exit_answer:
            lt_df = pandas.DataFrame(data=list_df)
            lt_df.to_csv(PATH_SAVE_FILE, encoding=ENCODING, index=False)
        else:
            if os.path.exists(PATH_SAVE_FILE):
                os.remove(PATH_SAVE_FILE)
    wd.destroy()


def rotate_card(*args):
    cnvs.itemconfig(cnvs_card_lang, text=f"{args[0]}", fill=COLOR_DSCRPTN)
    cnvs.itemconfig(cnvs_card_text, text=f"{args[1]}", fill=COLOR_DSCRPTN)
    cnvs.itemconfig(cnvs_img, image=img_crd_back)


# ================================================= Load Csv from file =================================================

if os.path.exists(PATH_SAVE_FILE):
    df = pandas.read_csv(PATH_SAVE_FILE, encoding=ENCODING)
    list_df = df.to_dict(orient="records")
    messagebox.showinfo(title="MODE", message="Continue from last saved result.")
elif os.path.exists(PATH_BEGIN_FILE):
    df = pandas.read_csv(PATH_BEGIN_FILE, encoding=ENCODING)
    list_df = df.to_dict(orient="records")
else:
    messagebox.showerror(title="ERROR", message=f"Files:'\n{os.path.abspath(PATH_BEGIN_FILE)}'\n "
                                                f"or\n'{os.path.abspath(PATH_SAVE_FILE)}'\ndon't exist!")


# ================================================= GUI setting ========================================================
wd = Tk()
wd.config(pady=25, padx=25, bg=BACKGROUND_COLOR)
wd.protocol("WM_DELETE_WINDOW", window_close)

img_crd_frnt = PhotoImage(file=PATH_CARD_FRNT)
img_crd_back = PhotoImage(file=PATH_CARD_BACK)

cnvs = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
cnvs_img = cnvs.create_image(400, 263, image=img_crd_frnt)
cnvs_card_lang = cnvs.create_text(400, 180, font=(FONT, FONT_SIZE_DESCR))
cnvs_card_text = cnvs.create_text(400, 270, font=(FONT, FONT_SIZE_TITLE, FONT_STYLE_TITLE), width=700)
cnvs.grid(column=0, columnspan=2, row=0)


word_gen()

img_yes = PhotoImage(file=PATH_RIGHT)
btn_yes = Button(image=img_yes, highlightthickness=0, command=click_yes)
btn_yes.grid(column=0, row=1)

img_no = PhotoImage(file=PATH_WRONG)
btn_no = Button(image=img_no, highlightthickness=0, command=word_gen)
btn_no.grid(column=1, row=1)

wd.mainloop()
