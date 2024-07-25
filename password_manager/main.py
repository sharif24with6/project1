from tkinter import *
from tkinter import ttk, messagebox
import random
import string

# Function to generate password
def generate_password():
    """
    Generate a random 12-character password including letters, digits, and punctuation.
    The generated password is inserted into the password entry field.
    """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# Function to save password
def save_password():
    """
    Save the entered website, email/username, and password to a file.
    If any field is empty, show a warning message.
    Otherwise, confirm with the user before saving the data.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        # Show a warning if any field is empty
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Read the existing data
        try:
            with open("data.txt", "r") as data_file:
                lines = data_file.readlines()
        except FileNotFoundError:
            lines = []

        # Check for existing website or email
        for line in lines:
            existing_website, existing_email, _ = line.strip().split(" | ")
            if website == existing_website or email == existing_email:
                messagebox.showwarning(title="Duplicate Entry", message="The website or email already exists.")
                return

        # Ask for user confirmation before saving
        is_ok = messagebox.askokcancel(title=website, 
                                       message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Save the data to a file and clear the input fields
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a canvas to hold the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Create labels for website, email/username, and password
website_label = ttk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = ttk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = ttk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Create entry fields for website, email/username, and password
website_entry = ttk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Set focus to the website entry field

email_entry = ttk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sharif12@gmail.com")  # Pre-fill the email entry with a default email

password_entry = ttk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Create buttons for generating password and adding the entry
generate_password_button = ttk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = ttk.Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Run the main loop
window.mainloop()
