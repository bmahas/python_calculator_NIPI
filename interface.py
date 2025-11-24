import tkinter as tk
from tkinter import ttk

# Placeholder functions (to be implemented by your team)
def custom_add(a, b):
    raise NotImplementedError("custom_add is not implemented yet")

def custom_subtract(a, b):
    raise NotImplementedError("custom_subtract is not implemented yet")

def custom_multiply(a, b):
    raise NotImplementedError("custom_multiply is not implemented yet")

def custom_divide(a, b):
    raise NotImplementedError("custom_divide is not implemented yet")


class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Function Calculator")
        self.root.geometry("300x350")

        self.expression = ""

        # Display
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
        self.display.pack(fill="both", padx=10, pady=10)

        # Buttons frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(expand=True, fill="both")

        # Calculator buttons grid
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row in buttons:
            row_frame = tk.Frame(btn_frame)
            row_frame.pack(expand=True, fill="both")
            for btn_text in row:
                btn = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=("Arial", 16),
                    command=lambda bt=btn_text: self.on_button_click(bt),
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            # Parse manually to detect the operator
            for op, func in {
                "+": custom_add,
                "-": custom_subtract,
                "*": custom_multiply,
                "/": custom_divide,
            }.items():
                if op in self.expression:
                    a, b = self.expression.split(op)
                    a, b = float(a), float(b)
                    result = func(a, b)
                    self.expression = str(result)
                    self.update_display()
                    return

            # If no custom operator found
            self.expression = "Error"
            self.update_display()

        except Exception as e:
            self.expression = "Error"
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorUI(root)
    root.mainloop()
