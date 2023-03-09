import tkinter as tk

board = ["", "", "",
         "", "", "",
         "", "", ""]

current_player = "X"

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=6, height=3, command=lambda pos=i: play_move(pos))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)


turn = tk.Label(root, text="Player " + current_player + "'s turn")
turn.grid(row=3, column=0, columnspan=3)

def play_move(pos):
    global current_player
    if board[pos] == "":
        board[pos] = current_player
        buttons[pos].config(text=current_player)
        winner = check_winner()
        if winner:
            turn.config(text="Player " + current_player + " wins")
            for i in range(9):
                buttons[i].config(state="disabled")
        elif "" not in board:
            turn.config(text="Tie")
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            turn.config(text="Player " + current_player + "'s turn")

def check_winner():
    if (board[0] == board[1] == board[2] != "") or \
       (board[3] == board[4] == board[5] != "") or \
       (board[6] == board[7] == board[8] != "") or \
       (board[0] == board[3] == board[6] != "") or \
       (board[1] == board[4] == board[7] != "") or \
       (board[2] == board[5] == board[8] != "") or \
       (board[0] == board[4] == board[8] != "") or \
       (board[2] == board[4] == board[6] != ""):
        return True
    else:
        return False


root.mainloop()
