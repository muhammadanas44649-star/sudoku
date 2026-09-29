import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# Sudoku Puzzles
# -----------------------------

PUZZLES = [
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],

    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ]
]


# -----------------------------
# Sudoku Solver
# -----------------------------

def is_valid(board, row, col, num):

    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


# -----------------------------
# Sudoku Game
# -----------------------------

class SudokuGame:

    def __init__(self, root):

        self.root = root
        self.root.title("Sudoku Game")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        self.root.configure(bg="#3057A0")

        self.entries = []

        self.create_title()
        self.create_board()
        self.create_buttons()

        self.new_game()


    # -------------------------
    # Title
    # -------------------------

    def create_title(self):

        title = tk.Label(
            self.root,
            text="🧩 SUDOKU",
            font=("Arial", 28, "bold"),
            bg="#f2f2f2",
            fg="#333333"
        )

        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="Fill the grid with numbers 1 - 9",
            font=("Arial", 12),
            bg="#f2f2f2",
            fg="#666666"
        )

        subtitle.pack(pady=5)


    # -------------------------
    # Create Sudoku Board
    # -------------------------

    def create_board(self):

        board_frame = tk.Frame(
            self.root,
            bg="black",
            padx=3,
            pady=3
        )

        board_frame.pack(pady=15)

        for row in range(9):

            row_entries = []

            for col in range(9):

                entry = tk.Entry(
                    board_frame,
                    width=2,
                    font=("Arial", 22, "bold"),
                    justify="center",
                    relief="solid",
                    bd=1
                )

                entry.grid(
                    row=row,
                    column=col,
                    padx=(1 if col % 3 != 0 else 3),
                    pady=(1 if row % 3 != 0 else 3),
                    ipady=5
                )

                # Allow only numbers 1-9
                entry.bind(
                    "<KeyRelease>",
                    self.validate_input
                )

                row_entries.append(entry)

            self.entries.append(row_entries)


    # -------------------------
    # Buttons
    # -------------------------

    def create_buttons(self):

        button_frame = tk.Frame(
            self.root,
            bg="#2c0a0a"
        )

        button_frame.pack(pady=15)

        new_button = tk.Button(
            button_frame,
            text="🔄 New Game",
            command=self.new_game,
            bg="#667eea",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        new_button.grid(row=0, column=0, padx=5)

        check_button = tk.Button(
            button_frame,
            text="✅ Check",
            command=self.check_solution,
            bg="#28a745",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        check_button.grid(row=0, column=1, padx=5)

        hint_button = tk.Button(
            button_frame,
            text="💡 Hint",
            command=self.give_hint,
            bg="#ff9800",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        hint_button.grid(row=0, column=2, padx=5)

        clear_button = tk.Button(
            button_frame,
            text="🧹 Clear",
            command=self.clear_board,
            bg="#dc3545",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        clear_button.grid(row=0, column=3, padx=5)


    # -------------------------
    # Validate Input
    # -------------------------

    def validate_input(self, event):

        entry = event.widget

        value = entry.get()

        if value and value not in "123456789":
            entry.delete(0, tk.END)


    # -------------------------
    # New Game
    # -------------------------

    def new_game(self):

        self.puzzle = random.choice(PUZZLES)

        self.solution = [
            row[:] for row in self.puzzle
        ]

        solve(self.solution)

        for row in range(9):

            for col in range(9):

                entry = self.entries[row][col]

                entry.config(
                    state="normal",
                    bg="white",
                    fg="#333333"
                )

                entry.delete(0, tk.END)

                if self.puzzle[row][col] != 0:

                    entry.insert(
                        0,
                        str(self.puzzle[row][col])
                    )

                    entry.config(
                        state="disabled",
                        disabledbackground="#dddddd",
                        disabledforeground="#222222"
                    )


    # -------------------------
    # Get Current Board
    # -------------------------

    def get_board(self):

        board = []

        for row in range(9):

            current_row = []

            for col in range(9):

                value = self.entries[row][col].get()

                if value == "":
                    current_row.append(0)
                else:
                    current_row.append(int(value))

            board.append(current_row)

        return board


    # -------------------------
    # Check Solution
    # -------------------------

    def check_solution(self):

        board = self.get_board()

        empty = False
        wrong = False

        for row in range(9):

            for col in range(9):

                if board[row][col] == 0:

                    empty = True

                elif board[row][col] != self.solution[row][col]:

                    wrong = True

                    self.entries[row][col].config(
                        bg="#ffcccc"
                    )

                else:

                    self.entries[row][col].config(
                        bg="#ccffcc"
                    )


        if wrong:

            messagebox.showerror(
                "Incorrect",
                "Some numbers are incorrect.\nKeep trying!"
            )

        elif empty:

            messagebox.showinfo(
                "Almost There",
                "Your answers so far are correct.\nComplete the remaining cells!"
            )

        else:

            messagebox.showinfo(
                "🎉 Congratulations!",
                "You solved the Sudoku!"
            )


    # -------------------------
    # Hint
    # -------------------------

    def give_hint(self):

        empty_cells = []

        for row in range(9):

            for col in range(9):

                entry = self.entries[row][col]

                if entry["state"] != "disabled" and entry.get() == "":

                    empty_cells.append((row, col))


        if not empty_cells:

            messagebox.showinfo(
                "Hint",
                "There are no empty cells!"
            )

            return


        row, col = random.choice(empty_cells)

        entry = self.entries[row][col]

        entry.insert(
            0,
            str(self.solution[row][col])
        )

        entry.config(
            bg="#fff3cd"
        )


    # -------------------------
    # Clear Board
    # -------------------------

    def clear_board(self):

        for row in range(9):

            for col in range(9):

                entry = self.entries[row][col]

                if entry["state"] != "disabled":

                    entry.delete(0, tk.END)

                    entry.config(
                        bg="white"
                    )


# -----------------------------
# Start Game
# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()

    game = SudokuGame(root)

    root.mainloop()
