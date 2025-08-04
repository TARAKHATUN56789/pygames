import random  # Import the random module (though it's unused in this snippet)

# Function to print the current state of the game board in a user-friendly format
def printGameBoard():
    # Print the top row with column letters A-G for player reference
    print("\n     A    B    C    D    E    F    G  ", end="")
    
    # Loop through each row of the board
    for x in range(rows):
        # Print the horizontal border line between rows
        print("\n   +----+----+----+----+----+----+----+")
        
        # Print the row number followed by the contents of each column in that row
        print(x, " |", end="")
        
        # Loop through each column in the current row
        for y in range(cols):
            # If the cell contains a player's disc (red or blue emoji), print it
            if gameBoard[x][y] in ["🔵", "🔴"]:
                print("", gameBoard[x][y], end=" |")
            else:
                # Otherwise, print empty space for an empty cell
                print("  ", end="  |")
    # Print the bottom border line of the board after the last row
    print("\n   +----+----+----+----+----+----+----+")

# Function to ask the player which column they want to drop their disc into
def getColumnInput():
    while True:
        # Ask user for a column letter (A-G), convert to uppercase
        col = input("Choose a column (A-G): ").upper()
        
        # Check if the input letter is valid
        if col in possibleLetters:
            # Convert letter to column index number (0 to 6)
            index = possibleLetters.index(col)
            
            # Check if the top cell in the column is empty (meaning the column is not full)
            if gameBoard[0][index] == "":
                return index  # Valid column chosen, return its index
            
            else:
                # If column is full, notify user and prompt again
                print("Column is full! Try another one.")
        else:
            # If invalid input, notify user and prompt again
            print("Invalid column. Choose between A-G.")

# Function to find the lowest empty row in a given column (where the disc will fall)
def getLowestRow(col):
    # Start checking from bottom row (rows-1) upwards to row 0
    for row in range(rows-1, -1, -1):
        # If the cell is empty, return that row index
        if gameBoard[row][col] == "":
            return row
    # If no empty row found (should not happen due to prior checks), return -1
    return -1  

# Function to place the current player's disc into the chosen column
def modifyTurn(col, turn):
    # Find the lowest available row in the chosen column
    row = getLowestRow(col)
    
    # Place the player's disc (turn) in that cell
    gameBoard[row][col] = turn

# Welcome message at the start of the game
print("Welcome to Connect Four")
print("-----------------------")

# List of valid column letters that players can choose from
possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]

# Create a 6-row by 7-column game board initialized with empty strings (no discs)
gameBoard = [["" for _ in range(7)] for _ in range(6)]

# Define number of rows and columns for easy reference
rows, cols = 6, 7

# Counter to track number of turns played (used to switch players)
turnCounter = 0

# List representing two players using emoji discs (Red and Blue)
players = ["🔴", "🔵"]

# Main game loop that runs indefinitely
while True:
    # Display the current game board on screen
    printGameBoard()
    
    # Determine the current player based on turn count (alternate turns)
    currentPlayer = players[turnCounter % 2]
    
    # Inform whose turn it is
    print(f"Player {currentPlayer}'s turn")
    
    # Ask the player to pick a valid column and return its index
    chosenCol = getColumnInput()
    
    # Place the current player's disc into the chosen column on the board
    modifyTurn(chosenCol, currentPlayer)
    
    # Increment turn counter to switch player on next loop iteration
    turnCounter += 1
