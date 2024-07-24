from tkinter import *

# Color scheme for the UI
LIGHT_BLUE = "#89CFF0"
WHITE = "#FFFFFF"
DARK_RED = "#800020"
GOLD = "#FFD700"
GREEN = "#9bdeac"

# Font and timer settings
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables for tracking repetitions and the current timer
REPS = 0
TIMER = None

def reset_timer():
    """
    Resets the timer and UI components to their initial states.
    Cancels the ongoing timer, resets repetition count,
    and updates the UI elements.
    """
    global REPS
    window.after_cancel(TIMER)  # Cancel the running timer
    REPS = 0  # Reset repetition counter
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text on canvas
    title_label.config(text="Timer", fg=DARK_RED)  # Reset title label
    check_mark.config(text="")  # Clear check marks
    start_button.config(state=NORMAL, bg=GOLD)  # Enable start button
    reset_button.config(state=DISABLED, bg=WHITE)  # Disable reset button

def start_timer():
    """
    Starts the timer based on the current session (work/break).
    Alternates between work sessions, short breaks, and long breaks,
    updating the UI accordingly.
    """
    global REPS
    REPS += 1  # Increment repetition counter

    # Convert durations to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the current session type and start countdown
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=GOLD)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=DARK_RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    
    # Disable start button and enable reset button
    start_button.config(state=DISABLED, bg=WHITE)
    reset_button.config(state=NORMAL, bg=GOLD)

def count_down(count):
    """
    Handles the countdown mechanism for the timer.
    Updates the timer display every second and manages session transitions.
    """
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"  # two-digit format for seconds
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")  # Update timer text
    
    if count > 0:
        # Continue countdown if time remains
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        # Start the next session and update check marks when time is up
        start_timer()
        marks = ""
        work_sessions = REPS // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)

# Initialize main window
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=LIGHT_BLUE)

# Title label for the timer
title_label = Label(text="Timer", fg=DARK_RED, bg=LIGHT_BLUE, font=(FONT_NAME, 52, "bold"))
title_label.grid(column=1, row=0)

# Canvas for timer display with tomato image
canvas = Canvas(width=200, height=224, bg=LIGHT_BLUE, highlightthickness=0)
my_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button to begin the timer
start_button = Button(text="Start", command=start_timer, bg=GOLD, highlightbackground=WHITE)
start_button.grid(column=0, row=2)

# Reset button to reset the timer
reset_button = Button(text="Reset", command=reset_timer, bg=WHITE, highlightbackground=GOLD, state=DISABLED)
reset_button.grid(column=2, row=2)

# Label to display check marks indicating completed sessions
check_mark = Label(text="", fg=DARK_RED, bg=LIGHT_BLUE, font=(FONT_NAME, 24))
check_mark.grid(column=1, row=3)

# Start the Tkinter main loop
window.mainloop()
