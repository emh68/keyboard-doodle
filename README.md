# keyboard-doodle
A Python turtle-based drawing program inspired by Etch A Sketch. Control the turtle with arrow keys and change pen colors using letter keys. Includes instruction display and dark/light mode.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-Unlicense-lightgrey)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey)

![](.\images\keyboard_doodle_demo.gif)

## Description
* Use the arrow keys to move the turtle and draw
* Press letter keys to switch between unique, vibrant pen colors
* Toggle between light and dark backgrounds using the Tab key
* Open a help/instructions window by pressing the I key


## ⌨️ Controls

| Key             | Action                                      |
|-----------------|-----------------------------------------------|
| ↑ ↓ ← →         | Move turtle up, down, left, right            |
| `Tab`           | Toggle light/dark mode                       |
| `c`             | Clear the screen                             |
| `i`             | Show instruction menu                     |
| `+` or `-`      | Increase or decrease pen size                            |

![](.\images\keyboard_doodle_start_screen.jpg)

### Requirements

- Python 3.x
- Uses built-in `turtle` module

### Run the Program

```bash
git clone https://github.com/emh68/keyboard-doodle.git
cd keyboard-doodle
python main.py