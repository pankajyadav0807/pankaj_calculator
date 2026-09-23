import tkinter as tk
import math

# -----------------------------
# Calculator Functions
# -----------------------------

def press(value):
    current = display.get()

    # Prevent multiple decimal points in the same number
    if value == ".":
        last_number = current.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()[-1]
        if "." in last_number:
            return

    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()

        # Replace percentage
        expression = expression.replace("%", "/100")

        result = eval(expression)

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square():
    try:
        number = float(display.get())
        result = number ** 2

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def key_press(event):
    key = event.char

    if key in "0123456789.+-*/%":
        press(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        backspace()

    elif event.keysym == "Escape":
        clear()


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)

root.configure(bg="#202124")

# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    root,
    font=("Arial", 28),
    bg="#303134",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)

display.pack(
    fill="x",
    padx=15,
    pady=(20, 15),
    ipady=18
)

# -----------------------------
# Button Area
# -----------------------------

button_frame = tk.Frame(root, bg="#202124")
button_frame.pack(expand=True, fill="both", padx=12, pady=5)

buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "x²", "="]
]


def button_command(value):

    if value == "C":
        return clear

    elif value == "⌫":
        return backspace

    elif value == "=":
        return calculate

    elif value == "x²":
        return square

    elif value == "÷":
        return lambda: press("/")

    elif value == "×":
        return lambda: press("*")

    elif value == "−":
        return lambda: press("-")

    else:
        return lambda: press(value)


# -----------------------------
# Create Buttons
# -----------------------------

for row_index, row in enumerate(buttons):

    for column_index, value in enumerate(row):

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#3c4043",
            activebackground="#5f6368",
            activeforeground="white",
            bd=0,
            relief="flat",
            command=button_command(value)
        )

        button.grid(
            row=row_index,
            column=column_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


# Make rows and columns expand
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)


# Keyboard support
root.bind("<Key>", key_press)

# Start calculator
root.mainloop()