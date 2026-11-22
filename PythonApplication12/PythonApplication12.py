
import tkinter as tk

def calculate():
    try:
        first = float(entry1.get())
        second = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                result_label.config(text="Ошибка: деление на ноль")
                return
            result = first / second

        result_label.config(text=f"Результат: {result:g}")

    except ValueError:
        result_label.config(text="Введите корректные числа")


window = tk.Tk()
window.title("Мой калькулятор")
window.geometry("350x300")
window.resizable(False, False)

title = tk.Label(
    window,
    text="КАЛЬКУЛЯТОР",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

entry1 = tk.Entry(window, font=("Arial", 14), justify="center")
entry1.pack(pady=5)

operation_var = tk.StringVar(value="+")

operation_menu = tk.OptionMenu(
    window,
    operation_var,
    "+", "-", "*", "/"
)
operation_menu.config(font=("Arial", 12))
operation_menu.pack(pady=5)

entry2 = tk.Entry(window, font=("Arial", 14), justify="center")
entry2.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Вычислить",
    font=("Arial", 12),
    command=calculate
)
calculate_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Результат:",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

window.mainloop()

