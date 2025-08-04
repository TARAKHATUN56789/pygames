# Import necessary modules
from tkinter import *           # Import all basic tkinter GUI components
from tkinter.ttk import *       # Import themed tkinter components (optional, but good practice)
from time import strftime       # Import function to get current time in string format

# Define a class to organize the clock's functionality
class DigitalClock:
    def __init__(self, root):
        # Set window title
        root.title("Digital Clock")

        # Create a label widget to display time
        # font = ("ds-digital", 80) sets a digital-style font (install "ds-digital" on your system if not available)
        # background = "black" sets background color of the label
        # foreground = "cyan" sets the text color
        self.label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
        self.label.pack(anchor='center')  # Center the label in the window

        # Call the function to start updating the time
        self.update_time()

    # Function to update the time every second
    def update_time(self):
        # Get the current time formatted as HH:MM:SS AM/PM
        current_time = strftime('%H:%M:%S %p')

        # Update the label text with the current time
        self.label.config(text=current_time)

        # Schedule this function to be called again after 1000 milliseconds (1 second)
        self.label.after(1000, self.update_time)

# Create the main window
root = Tk()

# Create an instance of the DigitalClock class with the main window as argument
clock = DigitalClock(root)

# Start the Tkinter main loop to run the application window
root.mainloop()
