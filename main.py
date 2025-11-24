from ui.calculator_ui import CalculatorUI
from core import operations
import tkinter as tk

def main():
    root = tk.Tk()
    CalculatorUI(root, operations)
    root.mainloop()

if __name__ == "__main__":
    main()
