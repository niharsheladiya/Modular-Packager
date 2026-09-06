<div align="center">

![Modular Packager Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Modular%20Packager&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Multi-Utility%20Toolkit&descAlignY=58&descSize=20)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=00FFB2&center=true&vCenter=true&width=600&lines=%F0%9F%A7%B0+Multi-Utility+Toolkit;%F0%9F%93%85+Datetime+%2B+%F0%9F%94%A2+Math+%2B+%F0%9F%8E%B2+Random;%F0%9F%86%94+UUID+%2B+%F0%9F%93%81+Files+%2B+%F0%9F%94%8D+Explorer;Built+with+Python+%F0%9F%90%8D)](https://git.io/typing-svg)

</div>

A modular, menu-driven Python command-line application that bundles several everyday utilities — date/time tools, math operations, random data generation, UUID creation, file handling, and module introspection — into a single interactive program.

Built with a clean **modular package structure**, where each feature category lives in its own module and `main.py` acts as the central packager/entry point tying everything together.

---

## 🎥 Video Explanation

Want to see the Modular Packager in action? Check out the walkthrough video below:

▶️ **[Watch the video explanation here](https://drive.google.com/file/d/1lgvapDMySX260B-ZPgcm8SsGTxhCc6Jl/view?usp=sharing)**

---

## ✨ Features

### 1. 📅 Datetime and Time Operations
- Display current date and time
- Calculate the difference between two dates
- Format a date into a custom format (`strftime` style, e.g. `%d/%m/%Y`)
- Stopwatch (start/stop with elapsed time)
- Countdown timer (input seconds, live countdown)

### 2. 🔢 Mathematical Operations
- Calculate factorial of a number
- Solve compound interest (principal, rate, time)
- Trigonometric calculations (sin, cos, tan for a given angle in degrees)
- Area of geometric shapes (Circle, Rectangle, Triangle)

### 3. 🎲 Random Data Generation
- Generate a random number
- Generate a random list of a given length
- Create a random password of a given length
- Generate a random OTP

### 4. 🆔 Generate Unique Identifiers (UUID)
- Generate a UUID4 identifier instantly

### 5. 📁 File Operations (Custom Module)
- Create a new file
- Write data to a file
- Read content from a file
- Append data to an existing file

### 6. 🔍 Explore Module Attributes (`dir()`)
- Enter any importable Python module name (e.g. `math`, `os`, `random`)
- View its available attributes/functions using `dir()`

### 7. 🚪 Exit
- Cleanly exits the toolkit with a thank-you message

---

## 🗂️ Project Structure

```
Modular package/
└── packager/
    ├── main.py                # Entry point — displays main menu & routes to modules
    ├── datetime_ops.py        # Datetime and Time Operations
    ├── math_ops.py            # Mathematical Operations
    ├── random_ops.py          # Random Data Generation
    ├── uuid_ops.py            # UUID Generator
    ├── file_ops.py            # File Operations (Custom Module)
    └── explorer.py            # Module Attribute Explorer (dir())
```

> Note: Adjust the file names above to match your actual module files — this reflects the standard modular layout implied by the menu options. Feel free to rename `main.py`'s helper modules however you've split them internally.

---

## ⚙️ Requirements

- Python 3.8+ (tested on Python 3.14.6)
- No external dependencies — uses only the Python **standard library**:
  - `datetime`
  - `math`
  - `random`
  - `uuid`
  - `time`
  - `os` / built-in file I/O

---

## 🚀 Installation & Usage

1. Clone or download this repository.
2. Navigate to the project folder:
   ```bash
   cd "Modular package/packager"
   ```
3. Run the toolkit:
   ```bash
   python3 main.py
   ```
4. Use the on-screen menu to navigate between features by entering the corresponding number.

---

## 🖥️ Example Session

```
=======================================
Welcome to Multi-Utility Toolkit
=======================================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
=======================================
Enter your choice: 1

Datetime and Time Operations:
1. Display current date and time
...
Enter your choice: 1
Current Date and Time: 2026-09-06 18:48:23
=======================================
```

Every sub-menu loops back to itself after an action, and option **"Back to Main Menu"** returns you to the top-level menu.

---

## 🧩 Design Notes

- **Modular architecture**: each feature domain (datetime, math, random, files, etc.) is isolated into its own logical module, making the codebase easy to extend — adding a new tool means adding a new module + one new menu entry in `main.py`.
- **Loop-driven menus**: each sub-menu re-displays itself after every action until the user chooses to go back, so multiple operations can be performed without re-navigating from the main menu each time.
- **Dynamic introspection**: the "Explore Module Attributes" option lets users inspect *any* importable Python module at runtime using `dir()` — a handy built-in learning/debugging tool.

---

## 🛠️ Possible Future Improvements

- Add input validation / error handling for invalid menu choices and bad inputs (e.g. non-numeric entries, invalid dates)
- Persist file operations to a configurable directory instead of the working directory
- Add unit tests for each module
- Package as a pip-installable CLI tool with `argparse` / `click` for non-interactive use
- Add colored terminal output for better readability

---

## 📄 License

This project is free to use and modify for personal or educational purposes. Add your preferred license (MIT, Apache 2.0, etc.) here.

---

## 👤 Author

**Nihar Sheladiya**
