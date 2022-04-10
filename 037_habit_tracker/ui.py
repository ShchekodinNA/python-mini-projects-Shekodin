from tkinter import *
import work_with_pixela as wwp

FONT = "arial"
FONT_SIZE = 20


class Ui:
    def __init__(self, YYYYmmdd: str, pixela_obj: wwp.PixelaWork, icolor: str = None, ititle="title"):
        self.window = Tk()
        self.seconds = 0
        self.YYYYmmdd = YYYYmmdd
        self.timer_ref = None
        self.window.title(ititle)
        self.window.config(pady=15, padx=15)
        self.window.resizable(False, False)
        if icolor is not None:
            self.window.config(bg=icolor)

        self.time_label = Label(text="00:00", font=(FONT, FONT_SIZE))
        self.time_label.grid(column=0, row=0, columnspan=3, pady=25)

        self.btn_stop = Button(text="STOP", highlightthickness=0, borderwidth=1, width=8, command=self.stop_push,
                               state="disabled")
        self.btn_stop.grid(column=1, row=1, padx=15)

        self.btn_start = Button(text="START", highlightthickness=0, borderwidth=1, width=8, command=self.start_push)
        self.btn_start.grid(column=0, row=1, padx=15)

        self.btn_upload = Button(text="UPLOAD", highlightthickness=0, borderwidth=1, width=8, command=self.record_push,
                                 state="disabled")
        self.btn_upload.grid(column=2, row=1, padx=15)

        self.pixela_obj = pixela_obj

        self.window.mainloop()

    def start_push(self):
        self.btn_start.config(state="disabled")
        self.btn_stop.config(state="normal")
        self.timer(self.seconds)

    def stop_push(self):
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="disabled")
        self.window.after_cancel(self.timer_ref)

    def record_push(self):
        self.btn_start.config(state="normal")
        self.btn_stop.config(state="normal")
        self.btn_upload.config(state="disabled")
        self.window.after_cancel(self.timer_ref)
        mnts = self.seconds // 60
        result = self.pixela_obj.update_pixel(YYYYmmdd=self.YYYYmmdd, addquant=mnts)
        result.raise_for_status()
        self.seconds = 0
        self.time_label.config(text="00:00")

    def timer(self, new_second: int):
        minutes = str(new_second // 60)
        seconds = str(new_second % 60)
        if len(minutes) < 2:
            minutes = f"0{minutes}"
        if len(seconds) < 2:
            seconds = f"0{seconds}"
        self.time_label.config(text=f"{minutes}:{seconds}")
        self.seconds = new_second
        if self.seconds > 60:
            self.btn_upload.config(state="normal")
        self.timer_ref = self.window.after(1000, self.timer, self.seconds + 1)
