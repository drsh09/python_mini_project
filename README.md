# 🕐 Digital Clock, Stopwatch & Timer

A feature-rich desktop time utility built with Python and Tkinter, offering a real-time digital clock, a precise stopwatch with lap tracking, and a configurable countdown timer — all in one clean GUI application.

---

##  Features

###  Digital Clock
- Displays the current time in real-time (`HH:MM:SS AM/PM` format)
- Updates every second automatically

###  Stopwatch
- Tracks time with millisecond precision (`HH:MM:SS:ms`)
- **Start / Stop / Reset** controls
- **Lap recording** — capture and display multiple lap times in a scrollable list

###  Countdown Timer
- Set custom hours, minutes, and seconds via input fields
- Counts down to zero and displays **"Time's Up!"** on completion
- **Start / Stop / Reset** controls

###  Icon-Based Navigation
- Switch between Stopwatch and Timer modes using intuitive icon buttons

---

##  Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (for image/icon support)

Install dependencies:

```bash
pip install Pillow
```

---

##  Project Structure

```
DigitalClock/
├── digital_clock.py     # Main application script
├── timer1.jpg           # Icon for Timer button
├── stopwatch1.jpg       # Icon for Stopwatch button
└── README.md
```

---

##  Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/DigitalClock.git
   cd DigitalClock
   ```

2. **Install dependencies**
   ```bash
   pip install Pillow
   ```

3. **Add icon images**  
   Place `timer1.jpg` and `stopwatch1.jpg` in the project directory (or update the file paths in `digital_clock.py` to match your setup).

4. **Run the app**
   ```bash
   python digital_clock.py
   ```

---

##  Configuration

The icon image paths are currently hardcoded. Update these lines in `digital_clock.py` to match the location of your image files:

```python
timer_image = Image.open("path/to/timer1.jpg").resize((50, 50))
stopwatch_image = Image.open("path/to/stopwatch1.jpg").resize((50, 50))
```

---

##  Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new features, or UI improvements.

---

##  License

This project is open source and available under the [MIT License](LICENSE).
