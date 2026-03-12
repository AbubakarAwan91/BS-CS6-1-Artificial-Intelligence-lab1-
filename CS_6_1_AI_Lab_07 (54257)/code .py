import tkinter as tk
from tkinter import messagebox

# Board initialization
board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

current_player = 'x'


# Evaluation Function
def evaluate(b):

    # Check rows
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] and b[row][0] != '_':
            if b[row][0] == 'x':
                return 10
            else:
                return -10

    # Check columns
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] and b[0][col] != '_':
            if b[0][col] == 'x':
                return 10
            else:
                return -10

    # Check diagonals
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != '_':
        if b[0][0] == 'x':
            return 10
        else:
            return -10

    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != '_':
        if b[0][2] == 'x':
            return 10
        else:
            return -10

    return 0


# Check if moves left
def is_moves_left(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == '_':
                return True
    return False


# Button click handler
def click(row, col):
    global current_player

    if board[row][col] == '_':

        board[row][col] = current_player
        buttons[row][col]["text"] = current_player

        score = evaluate(board)

        if score == 10:
            messagebox.showinfo("Game Over", "Player X Wins!")
            reset_game()
            return

        elif score == -10:
            messagebox.showinfo("Game Over", "Player O Wins!")
            reset_game()
            return

        elif not is_moves_left(board):
            messagebox.showinfo("Game Over", "Draw!")
            reset_game()
            return

        # Switch player
        if current_player == 'x':
            current_player = 'o'
        else:
            current_player = 'x'


# Reset game
def reset_game():
    global board, current_player

    board = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]

    current_player = 'x'

    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


# GUI
root = tk.Tk()
root.title("Tic Tac Toe - AI Lab")

buttons = []

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root,
                        text="",
                        font=("Arial", 25),
                        width=5,
                        height=2,
                        command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

reset_btn = tk.Button(root, text="Restart Game", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()