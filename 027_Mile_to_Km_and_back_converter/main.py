from tkinter import *


def clclt_dstnc():
    km_len = len(entr_km.get())
    mi_len = len(entr_mi.get())
    if km_len == 0 and mi_len == 0:
        lbl_extr.config(text="input!")
        return
    if km_len == 0:
        entr_km.delete(0, END)
        entr_km.insert(0, str(
            round(
                float(entr_mi.get()) * 1.60934, 2
            )
        ))
    else:
        entr_mi.delete(0, END)
        entr_mi.insert(0, str(
            round(
                float(entr_km.get()) / 1.60934, 2
            )
        ))


wndw = Tk()
wndw.title("Mi to Km converter")
wndw.minsize(width=250, height=60)
wndw.maxsize(width=250, height=60)
wndw.config(padx=15)


lbl_mi = Label(text="Miles")
lbl_mi.grid(column=0, row=0)

lbl_mi = Label(text="Kilometers")
lbl_mi.grid(column=2, row=0)


entr_mi = Entry(width=13)
entr_mi.focus()
entr_mi.grid(column=0, row=1)

entr_km = Entry(width=13)
entr_km.grid(column=2, row=1)

btn_calc = Button(text="=", width=7, command=clclt_dstnc)
btn_calc.grid(column=1, row=1)

lbl_extr = Label()
lbl_extr.grid(column=1, row=0)



wndw.mainloop()