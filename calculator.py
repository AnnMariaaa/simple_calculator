# Importing necessary libraries
from tkinter import * # For the GUI interface
import re

# Getting the previous state of the calculator (when there is incomplete expression)
prev_state = ""
# Getting the previous element clicked on the calculator
prev_element = ""

def main():
    # Creating the root widget
    root = Tk()
    root.title("Calculator")

    global e
    e = Entry(root, width = 30, borderwidth = 5, justify = 'right', font=('Times New Roman', 15, 'bold'))
    e.insert(0,"0")
    e.grid(row = 0, column = 0, columnspan = 4, pady = 10, ipady=10)

    # Disables the entry field to disallow typing from keyboard
    e.config(state = DISABLED)

    # Configure our grid rows and columns
    for row_count in range(0,6):
        Grid.rowconfigure(root, row_count, weight = 1)

    for column_count in range(0,4):
        Grid.columnconfigure(root, column_count, weight=1)

    # Creating buttons
    button_1 = Button(root, text = "1", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(1, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_2 = Button(root, text = "2", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(2, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_3 = Button(root, text = "3", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(3, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_4 = Button(root, text = "4", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(4, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_5 = Button(root, text = "5", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(5, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_6 = Button(root, text = "6", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(6, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_7 = Button(root, text = "7", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(7, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_8 = Button(root, text = "8", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(8, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_9 = Button(root, text = "9", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(9, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_0 = Button(root, text = "0", padx = 30, pady = 15, bg = '#d3d3d3', command=lambda: button_click(0, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))

    button_decimal = Button(root, text = ".", padx = 31, pady = 15, bg = '#d3d3d3', command=lambda: button_click(".", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))

    button_equal = Button(root, text = "=", padx = 29, pady = 15, bg = '#ADD8E6', command= lambda: equal(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal))
    button_clear = Button(root, text = "Clear", padx = 20, pady = 15, command= lambda: clear(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_back = Button(root, text = "Back", padx = 20, pady = 15, command= lambda: back(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal,e))

    button_add = Button(root, text = "+", padx = 28, pady = 15, command=lambda: button_click("+", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_subtract = Button(root, text = "-", padx = 30, pady = 15, command=lambda: button_click("-", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_multiply = Button(root, text = "*", padx = 30, pady = 15, command=lambda: button_click("*", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e))
    button_divide = Button(root, text = "/", padx = 30, pady = 15, command=lambda: button_click("/", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal,e))

    button_inverse = Button(root, text = "1/x", padx = 25, pady = 15, command=lambda: button_click("1/", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal,e))
    button_square = Button(root, text = "x^2", padx = 22, pady = 15, command=lambda: button_click("**2", button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal,e))

    # Put buttons on the screen in a grid format
    button_inverse.grid(row=1,column=0, sticky = "nsew")
    button_square.grid(row=1,column=1, sticky = "nsew")
    button_clear.grid(row=1,column=2, sticky = "nsew")
    button_back.grid(row=1,column=3, sticky = "nsew")

    button_7.grid(row=2,column=0, sticky = "nsew")
    button_8.grid(row=2,column=1, sticky = "nsew")
    button_9.grid(row=2,column=2, sticky = "nsew")
    button_divide.grid(row=2, column=3, sticky = "nsew")

    button_4.grid(row=3,column=0, sticky = "nsew")
    button_5.grid(row=3,column=1, sticky = "nsew")

    button_6.grid(row=3,column=2, sticky = "nsew")
    button_multiply.grid(row=3, column=3, sticky = "nsew")

    button_1.grid(row=4,column=0, sticky = "nsew")
    button_2.grid(row=4,column=1, sticky = "nsew")
    button_3.grid(row=4,column=2, sticky = "nsew")
    button_subtract.grid(row=4, column=3, sticky = "nsew")

    button_decimal.grid(row=5,column=0, sticky = "nsew")
    button_0.grid(row=5,column=1, sticky = "nsew")
    button_equal.grid(row=5,column=2, sticky = "nsew")
    button_add.grid(row=5,column=3, sticky = "nsew")

    root.mainloop()

# Function to change the state of buttons (enable/disable)
def buttons_state(new_state, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal):
    button_add.config(state = new_state)
    button_subtract.config(state = new_state)
    button_multiply.config(state = new_state)
    button_divide.config(state = new_state)
    button_decimal.config(state = new_state)
    button_square.config(state = new_state)
    button_inverse.config(state = new_state)
    button_equal.config(state = new_state)

# Function to decide what action is taken when a button is clicked
def button_click(element, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e):
    # Enabling all buttons
    buttons_state(NORMAL,button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal)
    e.config(state = NORMAL)

    global prev_element
    current = e.get()
    if current == "Cannot divide by zero" or current == "Incomplete expression" or (current in ["0", "0.0"] and type(element) is int) or (prev_element == "=" and (type(element) is int or element == ".")):
        current = ""

    # To avoid user from being able to start a number with 0
    if re.findall(r"[+|\-|*|/]0$", current) and type(element) is int:
        current = current[:-1]

    # To make sure two symbols cannot be pressed consecutively
    if re.findall(r"[+|\-|*|/]$", current) and element in ["+","-","/","*"]:
        current = current[:-1]
    e.delete(0,END)

    # If the "1/x" button is clicked
    last_index = -1
    for match in re.finditer(r'[-+*/]', current):
        last_index = match.start()

    if element == "1/":
        if last_index != -1:
            e.insert(0,str(current[:last_index+1]) + "1/" + str(current[last_index+1:]))
        else:
            e.insert(0, str(element) + str(current))
        e.config(state = DISABLED)
        prev_element = element
        return

    # If the "x^2" button is clicked
    if element == "**2":
        if not re.findall(r"[+|\-|*|/]$", current):
            e.insert(0, str(current) + "^2")
        else:
            e.insert(0, str(current))
        e.config(state = DISABLED)
        prev_element = element
        return

    # Ensuring consecutive decimal dots cannot be placed after the whole number eg: 5...6 is invalid
    if re.findall(r"\d+\.$", current) and element == ".":
        current = current[:-1]

    # Ensuring decimal dots cannot be placed after the fraction part eg: 55.66.7 is invalid
    if re.findall(r"\d+\.\d+$", current) and element == ".":
        e.insert(0,str(current))
        e.config(state = DISABLED)
        prev_element = element
        return

    # Converts decimal numbers with no whole part to start with 0. eg: .77 becomes 0.77
    if (re.findall(r"[+|\-|*|/]$", current)  or current == "") and element == ".":
        element = "0."

    # Converts decimal numbers with no fractional part to whole numbers. eg: 77. becomes 77
    if re.findall(r"\.$", current) and element in ["+","-","/","*"]:
        current = current[:-1]


    e.insert(0,str(current) + str(element))
    e.config(state = DISABLED)
    prev_element = element

# Function for the clear button
def clear(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e):
    # Enabling all buttons
    buttons_state(NORMAL, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse,button_equal)
    e.config(state = NORMAL)

    e.delete(0,END)
    e.insert(0,"0")
    e.config(state = DISABLED)

# Function for the equal button
def equal(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal):
    e.config(state = NORMAL)
    content = e.get()
    global prev_element
    try:
        if "^2" in content:
            content = content.replace("^2", "**2")
        total = eval(content)
        e.delete(0,END)
        e.insert(0, (str(int(total)) if total == int(total) else total))
        e.config(state = DISABLED)
        prev_element = "="
    except ZeroDivisionError: # Handle if user divides any number by 0
        e.delete(0,END)
        e.insert(0, "Cannot divide by zero")
        e.config(state = DISABLED)

        # Disabling buttons
        buttons_state(DISABLED, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal)
    except SyntaxError:
        global prev_state
        prev_state = content
        e.delete(0,END)
        e.insert(0, "Incomplete expression")
        e.config(state = DISABLED)
        # Disabling buttons
        buttons_state(DISABLED, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal)

# Function for the back button
def back(button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal, e):
    e.config(state = NORMAL)
    content = e.get()
    if len(content) == 1 or content == "Cannot divide by zero":
        if content == "Cannot divide by zero":
            buttons_state(NORMAL, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal)
        content = "0"
        e.delete(0,END)
        e.insert(0, str(content))
    elif content == "Incomplete expression":
        buttons_state(NORMAL, button_add, button_subtract, button_multiply, button_divide, button_decimal, button_square, button_inverse, button_equal)
        e.delete(0,END)
        global prev_state
        prev_state = prev_state.replace("**2", "^2")
        e.insert(0, str(prev_state))
    else:
        if content.endswith("^2"):  # Clicking back removes ^2 characters i.e., two characters
            content = content[:-2]
        else:
            content = content[:-1]  # Clicking back removes last character
        e.delete(0,END)
        e.insert(0, str(content))
    e.config(state = DISABLED)


if __name__ == "__main__":
    main()
