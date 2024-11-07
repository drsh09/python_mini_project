import tkinter as tk  # Required for Tkinter GUI
import time
from time import strftime
from PIL import Image, ImageTk  # Requires Pillow library

# Set up the tkinter window
root = tk.Tk()
root.title("Digital Clock, Stopwatch, and Timer")
root.geometry("500x500")
root.resizable(False, False)

# Variable to store stopwatch time in milliseconds
stopwatch_running = False
stopwatch_milliseconds = 0
lap_times = []  # To store lap times

# Variables for the mode and timer
current_mode = "Stopwatch"
timer_seconds = 0
timer_running = False

# Function to switch to the stopwatch mode
def show_stopwatch():
    global current_mode
    current_mode = "Stopwatch"
    stopwatch_frame.pack(anchor="center", pady=20)
    timer_frame.pack_forget()
    update_lap_display()  # Update lap display when switching to stopwatch

# Function to switch to the timer mode
def show_timer():
    global current_mode
    current_mode = "Timer"
    timer_frame.pack(anchor="center", pady=20)
    stopwatch_frame.pack_forget()

# Function to update the digital clock every second
def update_time():
    current_time = strftime("%H:%M:%S %p")  # 12-hour format with AM/PM
    time_label.config(text=current_time)  # Update the label with current time
    root.after(1000, update_time)  # Call update_time after 1 second

# Stopwatch functions
def update_stopwatch():
    if stopwatch_running:
        global stopwatch_milliseconds
        stopwatch_milliseconds += 10
        milliseconds = stopwatch_milliseconds % 1000 // 10  # Get the milliseconds (0-99)
        seconds = (stopwatch_milliseconds // 1000) % 60  # Get seconds (0-59)
        minutes = (stopwatch_milliseconds // (1000 * 60)) % 60  # Get minutes (0-59)
        hours = (stopwatch_milliseconds // (1000 * 60 * 60)) % 24  # Get hours (0-23)

        # Display in HH:MM:SS:MS format
        stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}")
        root.after(10, update_stopwatch)  # Update every 10 milliseconds (0.01 seconds)

def start_stopwatch():
    global stopwatch_running
    if not stopwatch_running:
        stopwatch_running = True
        update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_milliseconds, stopwatch_running, lap_times
    stopwatch_running = False
    stopwatch_milliseconds = 0
    lap_times = []  # Reset lap times
    stopwatch_label.config(text="00:00:00:00")
    update_lap_display()  # Clear the lap display

def record_lap():
    """Record the current lap time."""
    if stopwatch_running:
        # Calculate current lap time
        current_time = (stopwatch_milliseconds // 1000)  # Total seconds
        minutes, seconds = divmod(current_time, 60)
        hours, minutes = divmod(minutes, 60)
        lap_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        lap_times.append(lap_time)  # Store the lap time
        update_lap_display()  # Update lap display

def update_lap_display():
    """Update the lap display with recorded lap times."""
    lap_display.delete(1.0, tk.END)  # Clear previous lap times
    for index, lap in enumerate(lap_times, start=1):
        lap_display.insert(tk.END, f"Lap {index}: {lap}\n")  # Show each lap time

# Timer functions
def update_timer():
    global timer_seconds, timer_running
    if timer_running and timer_seconds > 0:
        timer_seconds -= 1
        minutes, seconds = divmod(timer_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        if timer_seconds > 0:
            root.after(1000, update_timer)
        else:
            timer_label.config(text="Time's Up!")  # Show "Time's Up!" when timer reaches zero

def start_timer():
    global timer_running, timer_seconds
    if not timer_running:
        # Get values from hours, minutes, and seconds entry fields
        hours = int(hour_entry.get() or 0)
        minutes = int(minute_entry.get() or 0)
        seconds = int(second_entry.get() or 0)
        timer_seconds = hours * 3600 + minutes * 60 + seconds
        timer_running = True
        update_timer()

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global timer_seconds, timer_running
    timer_running = False
    timer_seconds = 0
    timer_label.config(text="00:00:00")

# Styling the time label for the digital clock
time_label = tk.Label(root, font=("Helvetica", 48), fg="cyan", bg="black")
time_label.pack(anchor="center", fill="both", expand=True)

# Call update_time to initialize the digital clock
update_time()

# Load icons for Timer and Stopwatch (make sure to replace with your actual file paths)
try:
    timer_image = Image.open("A:\\pythonProject1\\DigitalClock\\timer1.jpg").resize((50, 50))
    timer_icon = ImageTk.PhotoImage(timer_image)
    stopwatch_image = Image.open("A:\\pythonProject1\\DigitalClock\\stopwatch1.jpg").resize((50, 50))
    stopwatch_icon = ImageTk.PhotoImage(stopwatch_image)
except FileNotFoundError:
    print("Error: Image files not found. Please check the file paths.")

# Buttons to switch between Timer and Stopwatch
button_frame = tk.Frame(root)
button_frame.pack(anchor="center", pady=10)

stopwatch_button = tk.Button(button_frame, image=stopwatch_icon, command=show_stopwatch)
stopwatch_button.grid(row=0, column=0, padx=20)

timer_button = tk.Button(button_frame, image=timer_icon, command=show_timer)
timer_button.grid(row=0, column=1, padx=20)

# Stopwatch frame and widgets
stopwatch_frame = tk.Frame(root)
stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00:00", font=("Helvetica", 36), fg="white", bg="grey")
stopwatch_label.pack(anchor="center")

stopwatch_button_frame = tk.Frame(stopwatch_frame)
start_button = tk.Button(stopwatch_button_frame, text="Start", command=start_stopwatch, font=("Helvetica", 14))
start_button.grid(row=0, column=0, padx=5)
stop_button = tk.Button(stopwatch_button_frame, text="Stop", command=stop_stopwatch, font=("Helvetica", 14))
stop_button.grid(row=0, column=1, padx=5)
reset_button = tk.Button(stopwatch_button_frame, text="Reset", command=reset_stopwatch, font=("Helvetica", 14))
reset_button.grid(row=0, column=2, padx=5)

lap_button = tk.Button(stopwatch_button_frame, text="Lap", command=record_lap, font=("Helvetica", 14))
lap_button.grid(row=0, column=3, padx=5)  # Add Lap button

stopwatch_button_frame.pack()

# Lap display widget to show recorded lap times
lap_display = tk.Text(stopwatch_frame, height=10, width=30, font=("Helvetica", 12))
lap_display.pack(anchor="center", pady=10)

# Timer frame and widgets
timer_frame = tk.Frame(root)
timer_label = tk.Label(timer_frame, text="00:00:00", font=("Helvetica", 36), fg="white", bg="grey")
timer_label.pack(anchor="center")

# Entry fields for hours, minutes, and seconds for the timer
time_entry_frame = tk.Frame(timer_frame)
time_entry_frame.pack(anchor="center", pady=10)

hour_entry = tk.Entry(time_entry_frame, font=("Helvetica", 16), width=5)
hour_entry.grid(row=0, column=0)
hour_entry.insert(0, "0")  # Default to 0

minute_entry = tk.Entry(time_entry_frame, font=("Helvetica", 16), width=5)
minute_entry.grid(row=0, column=1)
minute_entry.insert(0, "0")  # Default to 0

second_entry = tk.Entry(time_entry_frame, font=("Helvetica", 16), width=5)
second_entry.grid(row=0, column=2)
second_entry.insert(0, "0")  # Default to 0

# Labels for each time unit
hour_label = tk.Label(time_entry_frame, text="Hrs", font=("Helvetica", 12))
hour_label.grid(row=1, column=0)
minute_label = tk.Label(time_entry_frame, text="Mins", font=("Helvetica", 12))
minute_label.grid(row=1, column=1)
second_label = tk.Label(time_entry_frame, text="Secs", font=("Helvetica", 12))
second_label.grid(row=1, column=2)

# Timer control buttons
timer_button_frame = tk.Frame(timer_frame)
start_timer_button = tk.Button(timer_button_frame, text="Start", command=start_timer, font=("Helvetica", 12))
start_timer_button.grid(row=0, column=0, padx=5)
stop_timer_button = tk.Button(timer_button_frame, text="Stop", command=stop_timer, font=("Helvetica", 12))
stop_timer_button.grid(row=0, column=1, padx=5)
reset_timer_button = tk.Button(timer_button_frame, text="Reset", command=reset_timer, font=("Helvetica", 12))
reset_timer_button.grid(row=0, column=2, padx=5)

timer_button_frame.pack()

# Finally, run the tkinter event loop
root.mainloop()