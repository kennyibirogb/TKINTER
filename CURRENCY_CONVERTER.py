from tkinter import *

# Currency rates against USD (subject to change)
currency_rates = {
    'EUR': 1.1,  # Euro
    'GBP': 1.32,  # British Pound
    'JPY': 0.0091,  # Japanese Yen
    'CNY': 0.15,  # Chinese Yuan
    'INR': 0.014,  # Indian Rupee
    'AUD': 0.77,  # Australian Dollar
    'CAD': 0.81,  # Canadian Dollar
    'CHF': 1.08,  # Swiss Franc
    'MXN': 0.052,  # Mexican Peso
    'RUB': 0.014,  # Russian Ruble
    'ZAR': 0.069,  # South African Rand
    'BRL': 0.25,  # Brazilian Real
    'KRW': 0.00088,  # South Korean Won
    'TRY': 0.12,  # Turkish Lira
}

def button_click(value):
    """Append the clicked button's value to the first entry."""
    current_text = e1.get()
    e1.delete(0, END)  # Clear the entry
    e1.insert(0, current_text + str(value))  # Insert the new value

def clear_entry():
    """Clear the first entry."""
    e1.delete(0, END)

def convert_currency():
    """Convert the currency based on the input in the first entry."""
    try:
        amount = float(e1.get())
        currency = var.get()  # Get the selected currency
        rate = currency_rates[currency]  # Get the conversion rate
        converted_amount = amount * rate  # Convert the amount
        e2.delete(0, END)  # Clear the second entry
        e2.insert(0, f"{converted_amount:.2f} {currency}")  # Insert the converted amount
    except ValueError:
        e2.delete(0, END)
        e2.insert(0, "Error")

root = Tk()
root.title('CURRENCY_CONVERTER')
root.geometry('700x700')
root.configure(bg='black')

e1 = Entry(root, width='15', borderwidth='5', bg='grey', font=("Helvetica", 16))
e1.grid(row=1, column=1, padx=10, pady=10)

e2 = Entry(root, width='15', borderwidth='5', bg='grey', font=("Helvetica", 16))
e2.grid(row=2, column=1, padx=10, pady=10)

label = Label(root, text="CURRENCY CONVERTER", bg='black', fg='white', pady=20, font=("Helvetica", 15))
label.grid(row=0, column=0, columnspan=3, sticky='nsew')

# Create buttons
buttons = [
    ('', 1, 0),('$', 2, 0), ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('C', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('+', 5, 3),
    ('0', 6, 0), ('.', 6, 1), ('->', 6, 2)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = Button(root, text=text, padx=40, pady=20, bg='black', fg='white', font=("Helvetica", 15), command=clear_entry)
    elif text == '->':
        button = Button(root, text=text, padx=40, pady=20, bg='red', fg='white', font=("Helvetica", 15), command=convert_currency)
    else:
        button = Button(root, text=text, padx=40, pady=20, bg='black', fg='white', font=("Helvetica", 15), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=10, pady=10)

# Create currency options
var = StringVar(root) #Create a StringVar object to store the selected currency
var.set('EUR')  #set EUR to default currency

options = list(currency_rates.keys()) # Get the lsit of available currencies from the currency_rates dictionary
option_menu = OptionMenu(root, var, *options)
option_menu.grid(row=1)


root.mainloop()
