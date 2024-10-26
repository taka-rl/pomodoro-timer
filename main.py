import tkinter as tk
import time

# Constants
WORK_MINUTES = 0.25
BREAK_MINUTES = 0.1
POMODORO_CYCLES = 2
STUDY_LABEL = "Study"
BREAK_LABEL = "Break"


# Global variables
cycle_count = 0
is_running = False
timer = None


def start_timer():
    global is_running
    if not is_running:
        execute_session()
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
    global cycle_count, timer, is_running

    # Update timer display
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")

    if count > 0:
        # Continue counting down
        timer = window.after(1000, count_down, count - 1)

    else:
        execute_session()


def execute_session():
    global cycle_count, is_running

    cycle_count += 1
	
	# Execute the break session at the last of the cycle
    if cycle_count == POMODORO_CYCLES * 2:
        run_break_session()
    # Stop the timer if the number of cycles reaches the limit
    elif cycle_count > POMODORO_CYCLES * 2:
        label.config(text="Timer Completed")
        is_running = False  # Set is_running to False so the timer can be restarted
        return  # Exit the function to stop further execution

    # Switch to the next session (work or break)
    else:
        start_next_session()


def start_next_session():
    if cycle_count % 2 == 0:  # Even count: break session
        run_break_session()
    else:  # Odd count: work session
        run_study_session()


def run_study_session():
    label.config(text=STUDY_LABEL)
    count_down(int(WORK_MINUTES * 60))


def run_break_session():
    label.config(text=BREAK_LABEL)
    count_down(int(BREAK_MINUTES * 60))


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
