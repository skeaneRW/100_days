import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    global timer
    root.after_cancel(timer)
    reps = 0
    timer = None
    check_mark_label["text"] = ""
    timer_string = "00:00"
    canvas.itemconfig(timer_text, text = timer_string)
    timer_label.config(text="Timer", font=("Courier",80,"bold"),foreground=GREEN, background=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mechanism():
    global timer
    global reps
    if reps == 8:
        countdown_time = LONG_BREAK_MIN
        timer_label.config(text="XBreak", font=("Courier",80,"bold"),foreground=RED, background=YELLOW)
    elif reps % 2 == 0:
        countdown_time = WORK_MIN
        timer_label.config(text="Work", font=("Courier",80,"bold"),foreground=GREEN, background=YELLOW)
    else:
        check_mark_count = len(check_mark_label["text"]) + 1
        new_check_mark_text = "✔" * check_mark_count
        check_mark_label["text"] = new_check_mark_text
        timer_label.config(text="Break", font=("Courier",80,"bold"),foreground=PINK, background=YELLOW)
        countdown_time = SHORT_BREAK_MIN
    reps += 1    
    countdown(countdown_time * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(start_time):
    global reps
    if start_time >= 0:
        minutes = int(start_time/60)
        seconds = start_time % 60 if start_time % 60 > 9 else f"0{start_time % 60}"
        timer_string = f"{minutes}:{seconds}"
        canvas.itemconfig(timer_text, text = timer_string)
        global timer
        timer = root.after(1000,countdown,start_time - 1)
    elif reps <= 8:
        timer_mechanism()
    else:
        timer_reset()
        
# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Pomodoro Timer")
root.config(bg=YELLOW, padx=100, pady=50)

timer_label = tk.Label(text="Timer", font=("Courier",80,"bold"),foreground=GREEN, background=YELLOW, width=6)
timer_label.grid(row=0, column=1)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="skeaneRW/day28/tomato.png")
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=("Courier",35,"bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="start", highlightthickness=0, command=timer_mechanism)
start_button.grid(row=2, column=0, sticky="W")
reset_button = tk.Button(text="reset", highlightthickness=0, command=timer_reset)
reset_button.grid(row=2, column=2, sticky="E")
check_mark_label = tk.Label(text="", font=("Courier", 24, "bold"), foreground=GREEN, background=YELLOW)
check_mark_label.grid(row=3, column=1, sticky="WE")



root.mainloop()