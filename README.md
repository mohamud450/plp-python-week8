# Personal Mini-Toolkit

## What this project does

The Personal Mini-Toolkit is a menu-driven Python program with three beginner-friendly tools:

1. **Simple Calculator** — adds, subtracts, multiplies, and divides two numbers.
2. **To-Do List** — lets the user add, view, and remove tasks during the program session.
3. **Number Guessing Game** — asks the user to guess a random number from 1 to 10 in three attempts.

The main menu keeps running until the user selects **0. Quit**. Invalid choices are handled with friendly messages instead of crashing.

## Files

- `toolkit.py` — the working Python program.
- `toolkit_plan.txt` — the plan written before building the program.
- `screenshots/` — example program runs, including invalid input and each tool.

## How to run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal or command prompt in the project folder.
4. Run:

   ```bash
   python toolkit.py
   ```

   On some computers, use `python3 toolkit.py` instead.

No extra Python packages are required.

## Concepts demonstrated

- **Variables:** store numbers, choices, tasks, and the score/attempt information.
- **Input and output:** `input()` collects choices and `print()` displays instructions and results.
- **Conditionals:** `if`, `elif`, and `else` select actions and validate choices.
- **Loops:** `while` keeps the menu and to-do list active; `for` processes tasks and game attempts.
- **Lists:** the to-do list stores tasks and changes as tasks are added or removed.
- **Functions:** each tool is separated into a function to make the program easier to read.
- **Error handling:** `try/except` prevents invalid calculator numbers from crashing the program.

## Testing

The program was tested with normal and unexpected input. Example runs are saved in the `screenshots` folder. Try the menu options, invalid menu choices, invalid calculator input, adding and removing tasks, and quitting.

## Reflection

The hardest part was making the menu return after each tool without ending the whole program. The to-do list also needed careful checking so that a user could not remove a task number that did not exist. The longest bug to think through was validating task positions before using `pop()`, because Python list positions start at zero while the menu displays task numbers starting at one. I tested the calculator with valid numbers and invalid text, and checked that division by zero gives a friendly message. I also tested the guessing game with text and numbers outside the allowed range. The project helped me understand how functions, loops, conditionals, and lists work together in one program. With one more week, I would add a feature to save to-do tasks in a file so they remain available after the program closes.
