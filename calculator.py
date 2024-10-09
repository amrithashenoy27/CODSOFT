import tkinter as tk
calculate = ""


def add(operator):
    global calculate
    calculate += str(operator)
    result.delete(1.0, "end")
    result.insert(1.0, calculate)


def evaluation():
    global calculate
    try:
        total = str(eval(calculate))
        calculate = ""
        result.delete(1.0, "end")
        result.insert(1.0, total)
    except:
        clear()
        result.insert(1.0, "Not divisible by zero")


def clear():
    global calculate
    calculate = ""
    result.delete(1.0, "end")


size = tk.Tk()
size.geometry("300x280")

result = tk.Text(size, height=2, width=18, font=("Times New Roman", 23))
result.grid(columnspan=5)

button_1 = tk.Button(size, text="1", command=lambda: add(1), width=5, font=("Times New Roman", 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(size, text="2", command=lambda: add(2), width=5, font=("Times New Roman", 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(size, text="3", command=lambda: add(3), width=5, font=("Times New Roman", 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(size, text="4", command=lambda: add(4), width=5, font=("Times New Roman", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(size, text="5", command=lambda: add(5), width=5, font=("Times New Roman", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(size, text="6", command=lambda: add(6), width=5, font=("Times New Roman", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(size, text="7", command=lambda: add(7), width=5, font=("Times New Roman", 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(size, text="8", command=lambda: add(8), width=5, font=("Times New Roman", 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(size, text="9", command=lambda: add(9), width=5, font=("Times New Roman", 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(size, text="0", command=lambda: add(0), width=5, font=("Times New Roman", 14))
button_0.grid(row=5, column=3)

button_add = tk.Button(size, text="+", command=lambda: add("+"), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                           "bold"))
button_add.grid(row=2, column=4)

button_subtract = tk.Button(size, text="-", command=lambda: add("-"), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                                "bold"))
button_subtract.grid(row=3, column=4)

button_multiply = tk.Button(size, text="*", command=lambda: add("*"), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                                "bold"))
button_multiply.grid(row=4, column=4)

button_divide = tk.Button(size, text="/", command=lambda: add("/"), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                              "bold"))
button_divide.grid(row=6, column=4)

button_dot = tk.Button(size, text=".", command=lambda: add("."), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                           "bold"))
button_dot.grid(row=5, column=4)

open_bracket = tk.Button(size, text="(", command=lambda: add("("), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                             "bold"))
open_bracket.grid(row=5, column=1)

close_bracket = tk.Button(size, text=")", command=lambda: add(")"), width=5, bg="pink", font=("Times New Roman", 14,
                                                                                              "bold"))
close_bracket.grid(row=5, column=2)

button_clear = tk.Button(size, text="C", command=clear, width=11, bg="grey", font=("Times New Roman", 14, "bold"))
button_clear.grid(row=6, column=1, columnspan=2)

button_equal = tk.Button(size, text="=", command=evaluation, width=5, bg="pink", font=("Times New Roman", 14, "bold"))
button_equal.grid(row=6, column=3)

size.mainloop()