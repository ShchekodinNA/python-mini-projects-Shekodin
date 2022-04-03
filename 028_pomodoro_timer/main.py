from tkinter import *

PINK = "#FFA8A8"
RED = "#C74B50"
GREEN = "#99FFCD"
YELLOW = "#E7FBBE"
BLACK = "#180A0A"
FONT_NAME = "Courier"
SCND_FNT_NM = "Consolas"
WORK_MIN = 25
SHRT_BRK_MIN = 5
LNG_BRK_MIN = 20
AMOUNT_OF_SESSIONS = 4
CHECK = "✓"
reps = AMOUNT_OF_SESSIONS * 2
mark = ""
cycles = 0
timer = None


def rest_part(tme):
    global mark
    mark += CHECK
    cnvs.itemconfig(check_txt, text=mark)
    cnvs.config(bg=GREEN)
    timer_pm(sec_in=tme * 60)


def start_push():
    global reps, mark, cycles
    brn_start.config(state="disabled")
    if reps == 1:
        cnvs.itemconfig(wrk_rst_txt, text="REST", fill=GREEN)
        reps = AMOUNT_OF_SESSIONS * 2 + 1
        rest_part(LNG_BRK_MIN)
    elif reps % 2 == 1:
        cnvs.itemconfig(wrk_rst_txt, text="REST", fill=GREEN)
        rest_part(SHRT_BRK_MIN)
    else:
        if len(mark) >= 4:
            cycles += 1
            mark = ""
            cnvs.itemconfig(check_txt, text=mark)
            cnvs.itemconfig(fll_cycl, text=f"Cycles: {cycles}")
        cnvs.itemconfig(wrk_rst_txt, text="WORK", fill=RED)
        cnvs.config(bg=PINK)
        timer_pm(sec_in=WORK_MIN * 60)
    reps -= 1


def reset_push():
    global reps, mark
    brn_start.config(state="normal")
    wndw.after_cancel(timer)
    cnvs.config(bg=YELLOW)
    cnvs.itemconfig(wrk_rst_txt, text="")
    cnvs.itemconfig(timer_txt, text="00:00")
    reps = AMOUNT_OF_SESSIONS * 2
    mark = ""


def timer_pm(sec_in):
    global timer
    min = str(sec_in // 60)
    if len(min) < 2:
        min = f"0{min}"
    sec = str(sec_in % 60)
    if len(sec) < 2:
        sec = f"0{sec}"
    cnvs.itemconfig(timer_txt, text=f"{min}:{sec}")
    if sec_in < 1:
        brn_start.config(state="normal")
        cnvs.config(bg=BLACK)
        wndw.attributes('-topmost', True)
        wndw.attributes('-topmost', False)
        return
    timer = wndw.after(1000, timer_pm, sec_in - 1)


# set GUI:

wndw = Tk()
wndw.resizable(False, False)
wndw.minsize(height=300, width=300)
wndw.maxsize(height=300, width=300)
wndw.config(bg=YELLOW)
wndw.title("pomodoro Shekodin")

cnvs = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tmt.png")
cnvs.create_image(150, 150, image=img)
timer_txt = cnvs.create_text(150, 81, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
wrk_rst_txt = cnvs.create_text(150, 20, font=(SCND_FNT_NM, 15))
check_txt = cnvs.create_text(150, 215, text=" ", font=(SCND_FNT_NM, 14), fill=GREEN)
fll_cycl = cnvs.create_text(150, 245, text="Cycles: 0", font=(SCND_FNT_NM, 14), fill="white")
cnvs.pack()

brn_start = Button(text="START", font=(SCND_FNT_NM, 13), command=start_push)
brn_reset = Button(text="RESET", font=(SCND_FNT_NM, 13), command=reset_push)

brn_start_cnvs = cnvs.create_window(55, 145, anchor="nw", window=brn_start)
brn_reset_cnvs = cnvs.create_window(190, 145, anchor="nw", window=brn_reset)

wndw.mainloop()
