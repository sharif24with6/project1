from tkinter import *
import pandas
import random

# Set the background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize variables for the current card and words to learn
current_card = {}
to_learn = {}

# Try to load words to learn from a file, if it exists
try:
    data = pandas.read_csv("data/words_to_learn.csv")
# If the file is not found, load the original French words data
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
# If the file is found, convert it to a list of dictionaries
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    """
    Display the next card with a French word.
    """
    global current_card, flip_timer
    # Cancel the previous flip timer
    window.after_cancel(flip_timer)
    # Choose a random card from the words to learn
    current_card = random.choice(to_learn)
    # Update the card with the French word and set the front image
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """
    Flip the card to show the English translation.
    """
    # Update the card with the English word and set the back image
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    """
    Remove the current card from the list of words to learn
    and save the updated list to a file.
    """
    to_learn.remove(current_card)
    print(len(to_learn))
    # Save the updated list to a CSV file
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # Display the next card
    next_card()

# Set up the main window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create a canvas for displaying the flashcards
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons for known and unknown words
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first card
next_card()

# Start the main event loop
window.mainloop()
