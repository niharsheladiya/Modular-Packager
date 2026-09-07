<div align="center">

![Modular Packager](https://capsule-render.vercel.app/api?type=rect&color=0D1117&height=220&section=header&text=Modular%20Packager&fontSize=56&fontColor=39FF14&animation=fadeIn&fontAlignY=38&desc=Pack%20Every%20Python%20Task%20Into%20One%20Menu&descAlignY=62&descSize=16&descColor=ffffff)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2200&pause=900&color=39FF14&background=000000&center=true&vCenter=true&width=600&lines=%24+python3+main.py;Welcome+to+Multi-Utility+Toolkit;%3E+Loading+modules...+done.;%3E+6+tools+%2F+0+dependencies)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.8+-39FF14?style=flat-square&logo=python&logoColor=FFFFFF&labelColor=000000)
![Status](https://img.shields.io/badge/Status-Active-00F5FF?style=flat-square&labelColor=000000)
![License](https://img.shields.io/badge/License-MIT-FFD60A?style=flat-square&labelColor=000000)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-FF00E4?style=flat-square&labelColor=000000)

</div>

---

## 📚 Table of Contents

- [🎬 Video Explanation](#video-explanation)
- [🧭 Overview](#overview)
- [🧩 Features](#features)
- [🗃️ Project Structure](#project-structure)
- [✅ Requirements](#requirements)
- [▶️ Quick Start](#quick-start)
- [💻 See It In Action](#see-it-in-action)
- [🔧 Under the Hood](#under-the-hood)
- [🛣️ Roadmap](#roadmap)
- [🤝 Contributing](#contributing)
- [💡 FAQ](#faq)
- [🛠️ Tech Stack](#tech-stack)
- [📜 License](#license)
- [🙌 Show Some Love](#show-some-love)
- [🙋 Meet the Developer](#meet-the-developer)

---

## 🎬 Video Explanation

Prefer watching over reading? Here's a full walkthrough of Modular Packager in action:

▶️ **[Watch the Video Explanation](https://drive.google.com/file/d/1lgvapDMySX260B-ZPgcm8SsGTxhCc6Jl/view?usp=sharing)**

> 🔧 Swap the link above for your real YouTube / Google Drive / Loom recording.

---

## 🧭 Overview

**Modular Packager** is a menu-driven Python CLI that bundles six independent utility modules — date/time tools, math, random data, UUIDs, file handling, and a live module explorer — behind one clean entry point (`main.py`).

No scattered one-off scripts, no external packages to install — just a single organized toolkit where every feature lives in its own module, ready to run with `python3 main.py`.

---

## 🧩 Features

<details>
<summary><b>📅 Datetime & Time Operations</b></summary>
<br>

- Display current date and time
- Calculate the difference between two dates
- Format dates into a custom pattern
- Stopwatch (start/stop with elapsed time)
- Countdown timer
</details>

<details>
<summary><b>🔢 Mathematical Operations</b></summary>
<br>

- Calculate factorials
- Solve compound interest
- Trigonometric calculations (sin, cos, tan)
- Area of circles, rectangles & triangles
</details>

<details>
<summary><b>🎲 Random Data Generation</b></summary>
<br>

- Generate a random number
- Generate a random list
- Create a random password
- Generate a random OTP
</details>

<details>
<summary><b>🆔 UUID Generator</b></summary>
<br>

- Instantly generate a UUID4 identifier
</details>

<details>
<summary><b>📁 File Operations</b></summary>
<br>

- Create a new file
- Write data to a file
- Read content from a file
- Append data to a file
</details>

<details>
<summary><b>🔍 Module Explorer</b></summary>
<br>

- Enter any importable module name (e.g. <code>math</code>, <code>os</code>, <code>random</code>)
- Inspect its attributes live using <code>dir()</code>
</details>

<details>
<summary><b>🚪 Exit</b></summary>
<br>

- Leaves the toolkit with a friendly goodbye message
</details>

---

## 🗃️ Project Structure

```
Modular package/
└── packager/
    ├── main.py                # Entry point — main menu & routing
    ├── datetime_ops.py        # Datetime and Time Operations
    ├── math_ops.py            # Mathematical Operations
    ├── random_ops.py          # Random Data Generation
    ├── uuid_ops.py             # UUID Generator
    ├── file_ops.py            # File Operations (Custom Module)
    └── explorer.py            # Module Attribute Explorer (dir())
```

> 💡 Rename the files above to match your actual module names if they differ.

---

## ✅ Requirements

- 🐍 Python **3.8+** (tested on Python 3.14.6)
- 📦 **Zero external dependencies** — pure standard library:
  `datetime` · `math` · `random` · `uuid` · `time` · built-in file I/O

---

## ▶️ Quick Start

```bash
# 1. Clone or download the project
git clone https://github.com/your-username/modular-packager.git

# 2. Move into the project folder
cd "Modular package/packager"

# 3. Run it
python3 main.py
```

Then just type the number of the option you want and hit **Enter**. Every sub-menu loops back on itself, so you can run several operations before heading back to the main menu.

---

## 💻 See It In Action

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

---

## 🔧 Under the Hood

- 🧩 **Modular by design** — every feature lives in its own module, so adding a new tool is just a new module + one new menu entry.
- 🔁 **Self-looping menus** — each sub-menu redisplays itself after an action instead of dumping you back to the main menu every time.
- 🔍 **Built-in introspection** — the Module Explorer inspects *any* importable module at runtime with `dir()`.
- 🪶 **Lightweight** — no pip installs, no config files, no external services.

---

## 🛣️ Roadmap

| 🟢 Now | 🟡 Next | 🔴 Later |
|---|---|---|
| Input validation & error handling | Unit tests for every module | Pip-installable CLI (`argparse` / `click`) |
| Configurable output directory for files | Colorized terminal output | Optional GUI wrapper (Tkinter / PyQt) |

---

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a branch (`git checkout -b feature/your-feature`)
3. 💻 Make your changes
4. ✅ Commit (`git commit -m "Add your feature"`)
5. 📤 Push (`git push origin feature/your-feature`)
6. 🔁 Open a Pull Request

---

## 💡 FAQ

**Does this need an internet connection?**
No — everything runs locally on Python's standard library.

**Where do files created in "File Operations" get saved?**
In the current working directory by default, unless you pass a full path.

**Can I add my own tools?**
Yes — write a new module and wire it up to a new option in `main.py`.

**What Python version do I need?**
3.8 or higher. Tested on Python 3.14.6.

---

## 🛠️ Tech Stack

![Language](https://img.shields.io/badge/Language-Python-39FF14?style=flat-square&labelColor=000000)
![Interface](https://img.shields.io/badge/Interface-CLI-00F5FF?style=flat-square&labelColor=000000)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-FF00E4?style=flat-square&labelColor=000000)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-FFD60A?style=flat-square&labelColor=000000)

---

## 📜 License

Free to use and modify for personal or educational purposes. Swap in your preferred license below (MIT recommended):

```
MIT License © 2026 Nihar Sheladiya
```

---

## 🙌 Show Some Love

If Modular Packager saved you some typing, consider dropping the repo a star — it genuinely helps and costs nothing. 🌟

---

## 🙋 Meet the Developer

<table>
<tr>
<td width="130" align="center">
<img src="https://api.dicebear.com/7.x/avataaars/svg?seed=NiharSheladiya&backgroundColor=0D1117&radius=50" width="110" alt="Nihar Sheladiya avatar"/>
</td>
<td>

### Nihar Sheladiya
**Python Developer · Toolsmith · Automation Enthusiast**

I like taking the small scripts I keep rewriting and turning them into something reusable and well-organized. Modular Packager is exactly that — a handful of everyday utilities bundled into one clean, menu-driven toolkit instead of a dozen scattered files.

</td>
</tr>
</table>

- 🔭 **Currently building:** Modular Packager & other small CLI utilities
- 🌱 **Currently exploring:** clean, modular architecture in Python
- 💬 **Ask me about:** Python scripting, automation, CLI tool design
- ⚡ **Fun fact:** I'd rather write one well-structured script than ten messy ones

📫 **Let's connect:**

[![Email](https://img.shields.io/badge/Email-your.email%40example.com-39FF14?style=flat-square&logo=gmail&logoColor=FFFFFF&labelColor=000000)](mailto:your.email@example.com)
[![GitHub](https://img.shields.io/badge/GitHub-your--username-00F5FF?style=flat-square&logo=github&logoColor=FFFFFF&labelColor=000000)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-FF00E4?style=flat-square&logo=linkedin&logoColor=FFFFFF&labelColor=000000)](https://linkedin.com/in/your-profile)

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=2500&pause=900&color=39FF14&background=000000&center=true&vCenter=true&width=480&lines=Thanks+for+stopping+by+%F0%9F%91%8B;Feel+free+to+reach+out+anytime!)](https://git.io/typing-svg)

</div>

> ✏️ Email and social links above are placeholders — swap in your real ones, since I don't have your actual contact details.

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=rect&color=0D1117&height=100&section=footer)

</div>
