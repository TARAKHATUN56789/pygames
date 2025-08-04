from tkinter import *          # Imports all GUI functions and widgets from the tkinter library
import random                  # Imports random module for generating random positions (for food)

# ---------- Game Constants ----------
GAME_WIDTH = 500              # Width of the game canvas
GAME_HEIGHT = 500             # Height of the game canvas
SPEED = 200                   # Snake speed (lower = faster)
SPACE_SIZE = 25               # Size of each square segment of the snake
BODY_PARTS = 3                # Initial number of snake body parts
SNAKE_COLOR = "#0000FF"       # Snake color (blue)
FOOD_COLOR = "#FF0000"        # Food color (red)
BACKGROUND_COLOR = "#FFFFFF"  # Canvas background color (white)

# ---------- Snake Class ----------
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS                              # Set initial snake body size
        self.coordinates = [[100, 100], [75, 100], [50, 100]]    # Coordinates of snake body segments
        self.squares = []                                        # Store references to square graphics
        self.create_snake()                                      # Call method to draw the snake

    def create_snake(self):
        for x, y in self.coordinates:                            # Loop through each body segment
            square = canvas.create_rectangle(                   # Create a square for each segment
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)                          # Add square to the list

# ---------- Food Class ----------
class Food:
    def __init__(self):
        self.coordinates = []          # Store food coordinates
        self.create_food()             # Create the food on the canvas

    def create_food(self):
        # Generate a random position within the canvas grid
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]      # Save the coordinates
        canvas.create_oval(            # Draw the food as a red circle
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

# ---------- Main Game Loop ----------
def next_turn(snake, food):
    x, y = snake.coordinates[0]       # Get current head position of the snake

    # Move the head in the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head position to the snake coordinates list
    snake.coordinates.insert(0, (x, y))
    # Draw new head square on canvas
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check if snake ate the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1                          # Increase score
        label.config(text="Score: {}".format(score))  # Update score label
        canvas.delete("food")               # Remove old food
        food.create_food()                  # Create new food
    else:
        # If no food eaten, remove tail segment to keep size
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])    # Remove square from canvas
        del snake.squares[-1]               # Remove square from list

    # Check for collisions
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)  # Repeat this function after delay

# ---------- Direction Control ----------
def change_direction(new_direction):
    global direction
    # Prevent snake from reversing directly
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

# ---------- Collision Check ----------
def check_collisions(snake):
    x, y = snake.coordinates[0]    # Get head position

    # Check if snake hits wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if snake hits itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False  # No collision

# ---------- Game Over Screen ----------
def game_over():
    canvas.delete("all")  # Clear canvas
    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2,
        font=('consolas', 50), text="GAME OVER",
        fill="red", tag="gameover"
    )

# ---------- GUI Setup ----------
window = Tk()                          # Create main window
window.title("Snake Game")            # Set window title
window.resizable(False, False)        # Disable resizing

score = 0                              # Initialize score
direction = 'down'                     # Initial direction

# Score label setup
label = Label(window, text="Score: {}".format(score), font=('consolas', 30))
label.pack()

# Canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()  # Force the window to draw

# Center the window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ---------- Keyboard Controls ----------
# Bind arrow keys to change direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# ---------- Start Game ----------
snake = Snake()       # Create snake object
food = Food()         # Create food object
next_turn(snake, food)  # Start game loop

# ---------- Keep window running ----------
window.mainloop()
