# This is a simple dice roller program that allows the user to roll different types of dice.
# The program uses the tkinter library to create a GUI with buttons for each type of die.
import random
import tkinter as tk

# Adds different global variables needed throughout the program.
num_dice = 0
add_rolls = 'true'

def roll_dice(sides):
    """Roll the selected dice type the specified number of times and display the results."""
    global num_dice
    global add_rolls
    try:
        num_dice = int(num_dice_entry.get())
        if num_dice <= 0:
            result_label.config(text="Enter a positive number of dice.")
            return
    except ValueError:
        result_label.config(text="Enter a valid number of dice.")
        return

    # Roll the dice a specified number of times
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    if add_rolls == 'true':
        total = sum(rolls)
        result_label.config(text=f'Rolls: {rolls} | Total: {total}') # this function adds the total rolls together. looking to change that
        update_button_colors(sides)
    else:
        result_label.config(text=f'Rolls: {rolls}')
        update_button_colors(sides)

# Function for the color change when pressing a button
def update_button_colors(sides):
    """Update button colors to highlight the selected die."""
    for key, button in buttons.items():
        button.config(bg='purple' if key == sides else 'SystemButtonFace')

# Function to toggle the add_rolls variable
def toggle_add_rolls():
    global add_rolls
    add_rolls = 'false' if add_rolls == 'true' else 'true'
    toggle_button.config(text=f'Add Rolls: {add_rolls.capitalize()}')


# GUI setup
window = tk.Tk()
window.title('Dice Roller')
window.geometry('800x800')
window.configure(bg='grey')

# Result display label
result_label = tk.Label(window, text='Enter the number of dice and select a dice type!', font=('Helvetica', 14))
result_label.pack(pady=10)

# Widget for the number of dice
num_dice_label = tk.Label(window, text='Number of dice:', font=('Helvetica', 14))
num_dice_label.pack()
num_dice_entry = tk.Entry(window, width=5)
num_dice_entry.pack()

# Creates a button to toggle the add_rolls variable
toggle_button = tk.Button(window, text=f'Add Rolls: {add_rolls.capitalize()}', command=toggle_add_rolls)
toggle_button.pack(pady=10)

# Frame for the dice buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack(padx=10)

# Create buttons for each dice type
buttons = {
    20: tk.Button(buttons_frame, text='D20', command=lambda: roll_dice(20)),
    12: tk.Button(buttons_frame, text='D12', command=lambda: roll_dice(12)),
    10: tk.Button(buttons_frame, text='D10', command=lambda: roll_dice(10)),
    8: tk.Button(buttons_frame, text='D8', command=lambda: roll_dice(8)),
    6: tk.Button(buttons_frame, text='D6', command=lambda: roll_dice(6)),
    4: tk.Button(buttons_frame, text='D4', command=lambda: roll_dice(4)),
}

# Arrange the buttons in a grid layout
for i, (sides, button) in enumerate(buttons.items()):
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()


