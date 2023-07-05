import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create a list to store the buttons
buttons = []

# Create a variable to keep track of the current player
current_player = "X"
game_over = False


# Create a 3x3 grid of buttons
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font="Helvetica 20", width=6, height=3,
                           command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)


# Function to handle button click event
def button_click(row, col):
    global current_player, game_over

    button = buttons[row][col]
    if button["text"] == "" and not game_over:
        button["text"] = current_player
        if check_win(current_player):
            game_over = True
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        else:
            if check_draw():
                game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_game()
            else:
                change_player()
                if one_player_var.get() == 1 and current_player == "O" and not game_over:
                    play_computer()


# Function to check if any player has won
def check_win(player):
    board = [[button["text"] for button in row] for row in buttons]
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Function to check if it's a draw
def check_draw():
    board = [[button["text"] for button in row] for row in buttons]
    for row in board:
        if "" in row:
            return False
    return True


# Function to change the current player
def change_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"


# Function to reset the game
def reset_game():
    global current_player, game_over
    for row in buttons:
        for button in row:
            button["text"] = ""
    current_player = "X"
    game_over = False


# Function to make a random move for the computer player
def play_computer():
    available_buttons = []
    for row in buttons:
        for button in row:
            if button["text"] == "":
                available_buttons.append(button)
    if available_buttons:
        button = random.choice(available_buttons)
        button["text"] = current_player
        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        else:
            if check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_game()
            else:
                change_player()


# Function to start a new game
def start_new_game():
    reset_game()
    if one_player_var.get() == 1 and current_player == "O":
        play_computer()


# Create a variable to store the game mode (1 player or 2 players)
one_player_var = tk.IntVar(value=1)

# Create a radio button for selecting game mode
radio_button_1 = tk.Radiobutton(root, text="1 Player", variable=one_player_var, value=1)
radio_button_1.grid(row=3, column=0)
radio_button_2 = tk.Radiobutton(root, text="2 Players", variable=one_player_var, value=2)
radio_button_2.grid(row=3, column=1)

# Create a button to start a new game
new_game_button = tk.Button(root, text="New Game", command=start_new_game)
new_game_button.grid(row=3, column=2)

# Run the main event loop
root.mainloop()
