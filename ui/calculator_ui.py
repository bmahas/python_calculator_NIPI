import tkinter as tk

class CalculatorUI:
    def __init__(self, root, operations):
        self.operations = operations
        self.expression = ""
        self.root = root

        self.root.title("Custom Calculator")
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE)
        self.display.pack(fill="x", padx=10, pady=10)

        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"],
        ]

        frame = tk.Frame(root)
        frame.pack()

        for row in buttons:
            row_frame = tk.Frame(frame)
            row_frame.pack(fill="x")
            for text in row:
                tk.Button(
                    row_frame, text=text, width=5,
                    command=lambda t=text: self.on_button(t)
                ).pack(side="left", expand=True, fill="x")

    def on_button(self, char):
        if char == "=":
            self.calculate()
        else:
            self.expression += char
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            for op in ["+", "-", "*", "/"]:
                if op in self.expression:
                    a, b = map(float, self.expression.split(op))
                    func = {
                        "+": self.operations.add,
                        "-": self.operations.subtract,
                        "*": self.operations.multiply,
                        "/": self.operations.divide,
                    }[op]
                    result = func(a, b)
                    self.expression = str(result)
                    self.update_display()
                    return
        except:
            self.expression = "Error"
            self.update_display()
