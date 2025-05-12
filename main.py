from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_btn.config(text="")
    global reps
    reps = 0
    start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
     global reps
     reps += 1
     work_sec = WORK_MIN * 60
     short_break_sec = SHORT_BREAK_MIN * 60
     long_break_sec = LONG_BREAK_MIN * 60
     if reps % 8 == 0:
         label.config(text="Break", fg=RED)
         count_down(long_break_sec)
     elif reps % 2 == 0:
            label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
     else:
            label.config(text="Work", fg=GREEN)
            count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_btn.config(text=marks)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)

    else:
         start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,  )

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(103,130,text="00:00",fill="white", font=(FONT_NAME, 30, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_btn = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_btn.grid(column=1, row=3)
window.mainloop()