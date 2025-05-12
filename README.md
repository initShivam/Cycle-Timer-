# Pomodoro Timer 🕒🍅

A simple and elegant **Pomodoro Timer** built with **Python** using the `tkinter` GUI library. This timer helps you manage your time more effectively using the **Pomodoro Technique** — work in focused intervals with short breaks.

## 🔧 Features

* **Work Sessions:** 1-minute focus time (customizable)
* **Short Breaks:** 5-minute breaks after each session
* **Long Breaks:** 20-minute break after every 4 work sessions
* **Automatic Timer Cycles**
* **Visual Progress Tracking** with ✔ checkmarks
* **Start & Reset Controls**
* **Tomato-themed UI** 🍅

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system
* `tkinter` is included by default in standard Python installations
* A `tomato.png` image file (place this in the same directory as the script)

### Installation & Run

1. Clone or download the repository:

```bash
git clone https://github.com/your-username/pomodoro-timer.git
cd pomodoro-timer
```

2. Ensure `tomato.png` is in the same directory.

3. Run the script:

```bash
python main.py
```

---

## 📁 File Structure

```
pomodoro-timer/
│
├── main.py          # Main script with timer logic
├── tomato.png       # Image used in the UI
└── README.md        # This file
```

---

## 🧠 How It Works

1. Press **Start** to begin the timer.
2. After each work session, a break session automatically starts.
3. After 4 work sessions, a long break begins.
4. Press **Reset** to restart the entire cycle.

Each completed work session adds a ✔ to the bottom of the window.

---

## ✏️ Customize Timer Lengths

Modify the constants in `main.py`:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

Set them to any values you prefer.

---

## 🧑‍💻 Author

Made with ❤️ by \Shivam Singh

---
