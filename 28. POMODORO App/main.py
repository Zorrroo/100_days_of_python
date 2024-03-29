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
global reps
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    check_label.config(text="",fg=GREEN,bg = PINK)
    timer_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="BREAK!!!", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=RED)
        count_down(long_break_sec)


    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=YELLOW)
        count_down(short_break_sec)



    else:
        timer_label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=PINK)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN,bg = PINK)
check_label.grid(column=1, row=3)

bg_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=202, height=224, bg=PINK, highlightthickness=0)
canvas.create_image(102, 112, image=bg_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
