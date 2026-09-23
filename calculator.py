import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.pack(fill="both", padx=10, pady=10, ipady=10)


def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Calculator buttons
buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "⌫"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "C":
            command = clear
        elif button == "=":
            command = calculate
        elif button == "⌫":
            command = lambda: display.delete(len(display.get()) - 1, tk.END)
        else:
            command = lambda value=button: click(value)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=2,
            pady=2
            
        )

root.mainloop()