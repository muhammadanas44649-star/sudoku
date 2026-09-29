# Sudoku Game

A desktop Sudoku application featuring an interactive graphical user interface (GUI) built in Python using **Tkinter**. This application comes with built-in puzzles, an automatic backtracking solver, input validation, and helpful game controls like hint and solution-checking features.

---

## Features

* **Interactive 9x9 Grid:** Clearly formatted layout with $3 \times 3$ sub-grid separation.
* **Input Validation:** Restricts input to single digits `1` through `9`.
* **Pre-loaded Puzzles:** Randomly chooses a puzzle configuration each time you start a new game.
* **Backtracking Sudoku Solver:** Automatically calculates valid solutions using recursion.
* **Solution Verification:** Highlights correct entries in green and incorrect entries in red upon request.
* **Hint System:** Fills in a random empty cell with its correct number and highlights it in yellow.
* **Board Controls:** Easily clear player inputs or start a brand-new game at any point.

---

## Prerequisites

* **Python 3.x**
* **Tkinter** (usually included with standard Python installations)

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/muhammadanas44649-star/sudoku.git
cd sudoku

```


2. **Verify Python installation:**
```bash
python --version

```



---

## How to Run

Run the script directly using Python:

```bash
python sudoku.py

```

---

## How to Play

1. **Start a Game:** Launching the game loads a random puzzle. Preset numbers are locked in place.
2. **Fill Cells:** Click any blank cell and type a number from `1` to `9`.
3. **Controls:**
* **🔄 New Game:** Loads a new puzzle setup.
* **✅ Check:** Checks your current entries. Correct cells turn green; incorrect cells turn red.
* **💡 Hint:** Automatically fills in one missing number for you.
* **🧹 Clear:** Clears all your entered answers while preserving the original puzzle numbers.



---

## Code Architecture

* **`solve()` & `is_valid()`:** Core solver algorithm using dynamic recursive backtracking to validate rows, columns, and $3 \times 3$ boxes.
* **`SudokuGame` Class:** Manages the Tkinter interface, handles window events, tracks cell states, and updates tile colors dynamically based on user interaction.
