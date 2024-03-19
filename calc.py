import tkinter as tk

# Function to update the expression in the entry widget
def update_expression(value):
    entry_expression.insert(tk.END, value)

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry_expression.get())
        entry_expression.delete(0, tk.END)
        entry_expression.insert(tk.END, str(result))
    except Exception as e:
        entry_expression.delete(0, tk.END)
        entry_expression.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression and result
entry_expression = tk.Entry(root, width=20, font=('Arial', 16), justify="right")
entry_expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers
buttons_numbers = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', ' '
]
row_num = 1
col_num = 0
for button in buttons_numbers:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: update_expression(b)).grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Buttons for arithmetic operators
buttons_operators = ['/', '*', '-', '+']
row_num = 1
col_num = 4
for button in buttons_operators:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: update_expression(b)).grid(row=row_num, column=col_num, padx=5, pady=5)
    row_num += 1

# Clear button
tk.Button(root, text='C', width=5, height=2, command=lambda: entry_expression.delete(0, tk.END)).grid(row=5, column=3, padx=5, pady=5)

# Calculate button
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=5, column=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
