# LayoutSwitcher
A simple script that allows you to correct the keyboard layout of a mistyped word. RUS &lt;-> ENG

---

## Features

- Instantly switches the layout of selected text between Russian and English.
- Works system-wide with the <kbd>Cmd</kbd>+<kbd>Ctrl</kbd> hotkey.

---

## Installation

1. **Open Terminal** and navigate to the script folder:
	```sh
	cd /path/to/LayoutSwitcher
	```

2. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```

---

## Running the Script in the Background (macOS)

1. **Start the script in the background:**
	```sh
	nohup python3 layout_switcher.py &
	```
	- The script will keep running even if you close the terminal.

2. **Check if the script is running:**
	```sh
	ps aux | grep layout_switcher.py
	```
	- You should see a line with the process ID (PID).

---

## Stopping the Script

1. **Find the script's PID:**
	```sh
	ps aux | grep layout_switcher.py
	```

2. **Stop the process:**
	```sh
	kill <PID>
	```
	- Replace `<PID>` with the actual number from the previous command.

---

## Usage

1. Select the word or line you want to fix.
2. Press <kbd>Cmd</kbd>+<kbd>Ctrl</kbd> together.
3. The text will be automatically replaced with the corrected layout.

---

## Notes

- Requires Python 3 and accessibility permissions ("System Settings" → "Privacy & Security" → "Accessibility").



