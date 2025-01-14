import tkinter as tk
import random
import string
import pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols, custom_chars):
    char_set = ""
    
    # Include default character sets if user chooses to
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    
    # Add custom characters if any provided
    if custom_chars:
        char_set += custom_chars
    
    if not char_set:
        raise ValueError("At least one character set must be selected.")

    # Generate password using character set
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        custom_chars = custom_chars_entry.get()  # Get custom characters from input field
        password = generate_password(length, use_letters, use_numbers, use_symbols, custom_chars)
        password_var.set(password)
    except ValueError as e:
        password_var.set("Error: " + str(e))

def on_copy_button_click():
    pyperclip.copy(password_var.get())

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Add widgets for password length input
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Add checkboxes for character types
letters_var = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack()

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

symbols_var = tk.BooleanVar(value=True)
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

# Add input field for custom characters or symbols
custom_chars_label = tk.Label(root, text="Custom Characters (optional):")
custom_chars_label.pack()
custom_chars_entry = tk.Entry(root)
custom_chars_entry.pack()

# Add a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack()

# Display generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.pack()

# Add a button to copy the password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy_button_click)
copy_button.pack()

# Start main event loop
root.mainloop()
