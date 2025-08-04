# Import the tkinter library for creating the GUI
import tkinter

# Function that handles player moves
def set_tile(row, column):
    global curr_player  # Access the global variable to track current player

    if game_over:  # If the game has ended, ignore further moves
        return

    if board[row][column]["text"] != "":  # If the tile is already marked, do nothing
        return

    board[row][column]["text"] = curr_player  # Mark the tile with current player's symbol

    # Switch turns to the other player
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player + "'s turn"  # Update label to show who's turn it is

    check_winner()  # Check if the move resulted in a win or tie

# Function to check for win conditions or a tie
def check_winner():
    global turns, game_over  # Access global game state variables
    turns += 1  # Increment the turn count

    # Check all 3 rows for a win
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):  # Highlight the winning row
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True  # End the game
            return

    # Check all 3 columns for a win
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):  # Highlight the winning column
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    # Check the main diagonal for a win
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):  # Highlight the diagonal
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    # Check the anti-diagonal for a win
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    # If all tiles are filled and no winner, it's a tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

# Function to reset the board for a new game
def new_game():
    global turns, game_over

    turns = 0  # Reset turn counter
    game_over = False  # Reset game state

    label.config(text=curr_player + "'s turn", foreground="white")  # Reset label

    # Reset each tile to empty and restore original colors
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

# Initialize game variables
playerX = "X"  # Player X symbol
playerO = "O"  # Player O symbol
curr_player = playerX  # Player X goes first
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 3x3 board setup with placeholders

# Define color codes for theme
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0  # Total number of turns taken
game_over = False  # Whether the game has ended

# Create the main game window
window = tkinter.Tk()
window.title("Tic Tac Toe")  # Set the window title
window.resizable(False, False)  # Disable resizing of the window

frame = tkinter.Frame(window)  # Create a frame to hold widgets

# Label to show the current player's turn
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")  # Span the label across the top 3 columns

# Create the 3x3 grid of buttons (tiles)
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue,
                                            width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)  # Place button in the grid

# Add a restart button below the grid
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20),
                        background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")  # Span the restart button across the width

frame.pack()  # Pack the frame into the window

# Center the window on the screen
window.update()  # Update the window to get proper dimensions
window_width = window.winfo_width()  # Get current window width
window_height = window.winfo_height()  # Get current window height
screen_width = window.winfo_screenwidth()  # Get screen width
screen_height = window.winfo_screenheight()  # Get screen height
window_x = int((screen_width / 2) - (window_width / 2))  # Center X coordinate
window_y = int((screen_height / 2) - (window_height / 2))  # Center Y coordinate
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")  # Apply centering

window.mainloop()  # Start the GUI event loop (keep window running)
