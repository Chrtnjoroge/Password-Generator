from tkinter import *
from tkinter import messagebox
import secrets
import string

# Making the Graphical user interface.
root = Tk()
root.title("WELCOME TO THE PASSWORD GENERATOR.")
root.geometry("500x400")

# Declaring letters, numbers, and symbols as variables.
Characters = string.ascii_letters
Characters += string.digits
Characters += string.punctuation

# List to store the generated passwords.
password_history = []


# Function to estimate password strength.
def estimate_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    strength = 0

    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength


# generate password.
def rand():
    # delete password in the entry box
    pw_entry.delete(0, END)

    # Get password length as an integer.
    length = int(entry.get())

    # Initialising the password to be empty.
    password = "".join(secrets.choice(Characters) for _ in range(length))

    # Add the generated password to the history.
    password_history.append(password)

    # Display the generated password in the entry box.
    pw_entry.insert(0, password)

    # Estimate and display password strength.
    strength = estimate_strength(password)
    strength_label.config(text=f"Password Strength: {strength}/5")


# copy password.
def cp():
    #  clear what is in the clipboard.
    root.clipboard_clear()

    #  copy password to clipboard.
    root.clipboard_append(pw_entry.get())

    # Show a pop-up message with a green tick
    messagebox.showinfo("Password Copied", "Password copied successfully! ✔")


# Open the password history window.
def open_history():
    history_window = Toplevel(root)
    history_window.title("Password History")

    # Password history area with scrollbar.
    history_scrollbar = Scrollbar(history_window, orient=VERTICAL)
    history_text = Text(history_window, height=15, width=50, font=("Helvetica", 12),
                        yscrollcommand=history_scrollbar.set, state=DISABLED)

    history_scrollbar.config(command=history_text.yview)
    history_scrollbar.pack(side=RIGHT, fill=Y)

    history_text.pack()

    # Update the password history area.
    history_text.config(state=NORMAL)
    for password in password_history:
        history_text.insert(END, f"{password}\n")
    history_text.config(state=DISABLED)


# Requesting user to input password length.
label_frame = LabelFrame(root, text="Enter the length you want for the password: ")
label_frame.pack(pady=20)

# Entry box for characters.
entry = Entry(label_frame, font=("Helvetica", 20))
entry.pack(pady=20, padx=20)

# Label for the password entry area.
pw_label = Label(root, text="Your password is:", font=("Helvetica", 18))
pw_label.pack()

# Entry box for password.
pw_entry = Entry(root, text="", font=("Helvetica", 16))
pw_entry.pack(pady=20)

# Password strength label.
strength_label = Label(root, text="Password Strength: 0/5", font=("Helvetica", 14))
strength_label.pack()

# Create button frames.
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create buttons.
pw_button = Button(my_frame, text="Generate password", command=rand)
pw_button.grid(row=0, column=0, padx=8)

cp_button = Button(my_frame, text="Copy the password", command=cp)
cp_button.grid(row=0, column=1, padx=8)

history_button = Button(my_frame, text="View Password History", command=open_history)
history_button.grid(row=0, column=2, padx=8)

root.mainloop()
