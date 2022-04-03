import random
import pyperclip
from tkinter import *
from tkinter import messagebox

FONT = "arial"
RED = "#FD5D5D"
GREEN = "#6BCB77"
FNT_SZ = 14
PSSWRD_LNGTH = 21

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generation():
    nr_letters = random.randint(1, PSSWRD_LNGTH - 2)
    nr_symbols = random.randint(1, PSSWRD_LNGTH - nr_letters - 1)
    nr_numbers = PSSWRD_LNGTH - nr_letters - nr_symbols

    password = [random.choice(letters) for _ in range(0, nr_letters)]
    password += [random.choice(numbers) for _ in range(0, nr_symbols)]
    password += [random.choice(symbols) for _ in range(0, nr_numbers)]

    random.shuffle(password)
    password = "".join(password)
    enr_psswrd.delete(0, END)
    enr_psswrd.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def file_saving():
    lv_webs = enr_webs.get()
    lv_usrn = enr_usrn.get()
    lv_psswrd = enr_psswrd.get()
    if len(lv_webs) == 0 or len(lv_usrn) == 0 or len(lv_psswrd) == 0:
        lbl_info.config(text="fill all entry fields", fg=RED)
        return
    lbl_info.config(text="")
    answer = messagebox.askyesno(title=f"Save data for {lv_webs}?", message=f"Details:\nEmail/Username:{lv_usrn}\n"
                                                                            f"Password:{lv_psswrd}")
    if answer:
        with open("password_savings.txt", mode="a") as file:
            file.write(f"{lv_webs}\n    {lv_usrn} | {lv_psswrd}\n")
        lbl_info.config(text="password saved", fg=GREEN)
        enr_webs.delete(0, END)
        enr_psswrd.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
wndw = Tk()
wndw.config(padx=40, pady=40)
wndw.title("password manager Shekodin")
wndw.resizable(False, False)
cnvs = Canvas(width=120, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
cnvs.create_image(60, 100, image=img)
cnvs.grid(column=2, row=1)

lbl_webs = Label(text="Website: ", font=(FONT, FNT_SZ))
lbl_webs.grid(column=1, row=2)

lbl_usrn = Label(text="Email/Username: ", font=(FONT, FNT_SZ))
lbl_usrn.grid(column=1, row=3)

lbl_psswrd = Label(text="Password: ", font=(FONT, FNT_SZ))
lbl_psswrd.grid(column=1, row=4)

lbl_info = Label(text="", font=(FONT, FNT_SZ))
lbl_info.grid(column=1, row=5)

enr_webs = Entry(width=34, font="consolas")
enr_webs.focus()
enr_webs.grid(column=2, row=2, columnspan=2)

enr_usrn = Entry(width=34, font="consolas")
enr_usrn.grid(column=2, row=3, columnspan=2)

enr_psswrd = Entry(width=21, font="consolas")
enr_psswrd.grid(column=2, row=4)

btn_gen = Button(text="Generate password", command=password_generation)
btn_gen.grid(column=3, row=4)

btn_add = Button(text="Add", width=17, command=file_saving)
btn_add.grid(column=2, row=5)

wndw.mainloop()
