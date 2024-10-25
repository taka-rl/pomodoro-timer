import tkinter as tk
import time

# Constants
WORK_MINUTES = 50
BREAK_MINUTES = 10
POMODORO_CYCLES = 4

# Global variables
cycle_count = 0
is_running = False
timer = None


def start_timer():
    global is_running
    if not is_running:
        count_down(WORK_MINUTES * 60)
        is_running = True


def reset_timer():
    global is_running, cycle_count
    if timer:
        window.after_cancel(timer)
    is_running = False
    cycle_count = 0
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


def count_down(count):
    global cycle_count, timer

    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        cycle_count += 1
        if cycle_count % POMODORO_CYCLES == 0 or cycle_count % 2 == 0:
            label.config(text="Break")
            count_down(BREAK_MINUTES * 60)
        else:
            label.config(text="Study")
            count_down(WORK_MINUTES * 60)


# UI Setup
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=30)

label = tk.Label(window, text="Timer", font=("Arial", 30))
label.pack()

canvas = tk.Canvas(window, width=200, height=224)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Arial", 35))
canvas.pack()

start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack(side="left")

reset_button = tk.Button(window, text="Reset", command=reset_timer)
reset_button.pack(side="right")

window.mainloop()
