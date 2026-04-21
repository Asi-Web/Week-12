## Asiwome Agbleze
## CMSC 111/1
## Assignment 6 - dice_roll_simulator.py

# Import the random library to generate random dice values.
import random

# Import the math library as required by the assignment.
import math

# Try to import tkinter for the GUI and image display.
# If tkinter is not available, print an error and stop the program.
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: tkinter is not installed or not available on this system.")
    exit()

# Try to import PIL so JPG images can be opened and displayed.
# Pillow is needed because tkinter alone does not reliably display JPG files.
try:
    from PIL import Image, ImageTk
except ImportError:
    print("Error: Pillow is not installed.")
    print("Install it by running: pip install pillow")
    exit()


# Create a dictionary that maps each dice number to its image file.
dice_images = {
    1: "dice_1.jpg",
    2: "dice_2-2.jpg",
    3: "dice_3-3.jpg",
    4: "dice_4-4.jpg",
    5: "dice_5-5.jpg",
    6: "dice_6-6.jpg"
}


# Create a function to load and resize a dice image.
# This function also handles file and image errors.
def load_dice_image(file_name, size=(150, 150)):
    try:
        image = Image.open(file_name)

        # Resize the image so both dice appear neatly in the window.
        image = image.resize(size)

        # Convert the image into a format tkinter can display.
        return ImageTk.PhotoImage(image)

    except FileNotFoundError:
        messagebox.showerror("File Error", f"Image file not found: {file_name}")
        return None

    except OSError:
        messagebox.showerror("Image Error", f"Could not open image file: {file_name}")
        return None

    except Exception as error:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred:\n{error}")
        return None


# Create a function to simulate rolling two dice.
def roll_dice():
    try:
        # Generate two random integers between 1 and 6.
        die1_value = random.randint(1, 6)
        die2_value = random.randint(1, 6)

        # Use the math library to calculate the total.
        # math.fsum is used here to show appropriate math-library usage.
        total = math.fsum([die1_value, die2_value])

        # Get the correct image file names from the dictionary.
        die1_file = dice_images.get(die1_value)
        die2_file = dice_images.get(die2_value)

        # Make sure the correct file names were found.
        if die1_file is None or die2_file is None:
            raise ValueError("A dice image mapping is missing.")

        # Load both dice images.
        die1_photo = load_dice_image(die1_file)
        die2_photo = load_dice_image(die2_file)

        # Stop if one of the images could not be loaded.
        if die1_photo is None or die2_photo is None:
            return

        # Update the labels with the new dice images.
        die1_label.config(image=die1_photo)
        die1_label.image = die1_photo

        die2_label.config(image=die2_photo)
        die2_label.image = die2_photo

        # Show the dice values and total.
        result_label.config(
            text=f"Die 1: {die1_value}   Die 2: {die2_value}   Total: {int(total)}"
        )

    except ValueError as error:
        messagebox.showerror("Value Error", str(error))

    except Exception as error:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred:\n{error}")


# Try to create the main program window.
try:
    root = tk.Tk()
    root.title("Dice Roll Simulator")
    root.geometry("400x350")
    root.resizable(False, False)
except Exception as error:
    print(f"Error creating the application window: {error}")
    exit()


# Create a title label for the window.
title_label = tk.Label(root, text="Roll Two Dice", font=("Arial", 18, "bold"))
title_label.pack(pady=10)


# Create a frame to hold both dice images side by side.
dice_frame = tk.Frame(root)
dice_frame.pack(pady=10)


# Create labels that will display the two dice images.
die1_label = tk.Label(dice_frame)
die1_label.pack(side="left", padx=10)

die2_label = tk.Label(dice_frame)
die2_label.pack(side="left", padx=10)


# Create a label to show the numeric results.
result_label = tk.Label(root, text="Click the button to roll the dice.", font=("Arial", 12))
result_label.pack(pady=15)


# Create a button that rolls the dice when clicked.
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12, "bold"), command=roll_dice)
roll_button.pack(pady=10)


# Roll the dice once when the program starts so images appear immediately.
roll_dice()


# Start the tkinter event loop.
root.mainloop()
