import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    # Get the input from the entry fields
    birth_date_str = entry.get()
    
    try:
        # Convert the input string to a date object
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        
        # Get the current date
        today = datetime.today()
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Update the label with the calculated age
        label_result.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create a Label for instructions
label= tk.Label(root, text="Enter your birth date (YYYY-MM-DD):")
label.pack(pady=10)

# Create an Entry widget for the birth date
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a Button to calculate the age
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=5)

# Create a Label to display the result
label_result = tk.Label(root, text="", width=30)
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
