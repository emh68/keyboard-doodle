from turtle import Turtle, Screen
import tkinter as tk
from tkinter import messagebox

# Turtle and screen setup
t = Turtle()
screen = Screen()
t.pensize(3)
t.shapesize(2, 2, 1)
t.pencolor("blue")

# Start color
current_pen_color = "blue"
t.pencolor(current_pen_color)

# Track dark mode
dark_mode = False

# Key state tracking
keys_pressed = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

# Pen colors
color_keys = {
    "a": "lime",
    "b": "dodger blue",
    "d": "dark violet",
    "e": "firebrick",
    "f": "deep pink",
    "g": "lime green",
    "h": "dark orchid",
    "j": "sea green",
    "k": "peru",
    "l": "white",
    "m": "yellow green",
    "n": "navy",
    "o": "dark orange",
    "p": "medium purple",
    "q": "blue violet",
    "r": "crimson",
    "s": "silver",
    "t": "turquoise",
    "u": "sienna",
    "v": "hot pink",
    "w": "orchid",
    "x": "black",
    "y": "gold",
    "z": "spring green"
}


def show_instructions():
    # Stop movement before showing messagebox
    for key in keys_pressed:
        keys_pressed[key] = False

    messagebox.showinfo("Instructions",
                        "Controls:\n"
                        "↑ Move forward\n"
                        "↓ Move backward\n"
                        "← Turn left\n"
                        "→ Turn right\n"
                        "(Hold combinations like ← + ↑ to move and turn)\n\n"
                        "C: Clear screen\n"
                        "I: Show instructions\n"
                        "Tab: Toggle dark mode\n"
                        "+ / - : Increase / Decrease pen size\n\n"
                        "Change pen color (press letter):\n" +
                        "\n".join(
                            [f"{k.upper()} = {v.title()}" for k, v in color_keys.items()])
                        )


def move():
    if keys_pressed["Up"]:
        t.forward(5)
    if keys_pressed["Down"]:
        t.backward(5)
    if keys_pressed["Left"]:
        t.left(5)
    if keys_pressed["Right"]:
        t.right(5)
    screen.ontimer(move, 50)  # Continuous check


def on_key_press(event):
    global dark_mode, current_pen_color
    key = event.keysym
    char = event.char.lower()

    if key in keys_pressed:
        keys_pressed[key] = True
    elif char in color_keys:
        current_pen_color = color_keys[char]
        t.pencolor(current_pen_color)
    elif char == "i":
        show_instructions()
    elif char == "c":
        clear()
    elif key == "Tab":
        dark_mode = not dark_mode
        screen.bgcolor("black" if dark_mode else "white")
    elif key in ("plus", "equal"):
        t.pensize(min(t.pensize() + 1, 50))
    elif key == "minus":
        t.pensize(max(t.pensize() - 1, 1))


def on_key_release(event):
    key = event.keysym
    if key in keys_pressed:
        keys_pressed[key] = False


# Clear canvas
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# Canvas setup
canvas = screen.getcanvas()
canvas.bind("<KeyPress>", on_key_press)
canvas.bind("<KeyRelease>", on_key_release)
canvas.focus_set()

# Initial screen setup
screen.bgcolor("white")
screen.listen()
screen.onkeypress(clear, "c")

show_instructions()
move()
screen.mainloop()
