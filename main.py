from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
FILL = "#570200"
MARKS = ["✔","✔ ✔","✔ ✔ ✔","✔ ✔ ✔ ✔"]
LABEL = ["Work Work Work", "5 Minute Break", "Take 20"]
check = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check, timer, clock, timer_label, reps
    window.after_cancel(timer)
    check = 0
    canvas.itemconfig(clock, text="00:00")
    timer_label.config(text="Pomodoro Timer", bg="pink")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global check
    check += 1

    if check >= 2:
        mark = floor(int(check / 2) - 1)
        canvas.itemconfig(checkmark, text=MARKS[mark])

    if check% 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text=LABEL[2], bg="pink")
        check = 0
    elif check%2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text=LABEL[1], bg="yellow")
    else:
        count_down(WORK_MIN)
        timer_label.config(text=LABEL[0], bg="light green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
        min = int(count / 60)
        sec = count % 60
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
        canvas.itemconfig(clock, text=f"{min}:{sec}")
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=444, height=480)
window.maxsize(width=444, height=480)


canvas = Canvas(width=460, height=550)
bg_image = PhotoImage(file="moon.gif")

canvas.create_image(220, 380, image=bg_image)
clock = canvas.create_text(222, 162, text="00:00", font=("Courier", 42, "bold"), fill=FILL)
checkmark = canvas.create_text(222, 250, text=" ", font=("verdana",23,"normal"), fill=FILL)
canvas.place(x=-2,y=0)

start_button = Button(text="Start", bg="light blue")
start_button.place(x=30,y=30,width=60)
start_button.config(command=start_timer)
timer_label = Label(text="Pomodoro Timer", width=25, height=2, font=("Courier", 18, "normal"), bg="pink")
timer_label.place(x=40, y=370)


reset_button = Button(text="Reset", bg="light blue")
reset_button.place(x=354,y=30,width=60)
reset_button.config(command=reset_timer)

window.mainloop()


