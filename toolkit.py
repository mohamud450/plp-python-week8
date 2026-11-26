"""
Personal Mini-Toolkit
A beginner-friendly menu program with a calculator, a to-do list,
and a number guessing game.
"""

import random


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number, such as 12 or 4.5.")


# Tool 1: Perform a basic calculation using two numbers and an operation.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    print("Choose an operation: +  -  *  /")
    operation = input("Operation: ").strip()

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("That operation is not supported. Please choose +, -, * or /.")
        return

    print(f"Result: {first_number:g} {operation} {second_number:g} = {answer:g}")


# Tool 2: Store tasks in a list and allow the user to add, view, and remove them.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("0. Return to the main menu")
        choice = input("Choose an option (0-3): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                selected = input("Enter the task number to remove: ").strip()
                if selected.isdigit():
                    task_number = int(selected)
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed: {removed_task}")
                    else:
                        print("That task number is not on the list.")
                else:
                    print("Please enter a whole-number task position.")
        elif choice == "0":
            print("Returning to the main menu...")
            break
        else:
            print("Please choose 0, 1, 2 or 3.")


# Tool 3: Give the player three chances to guess a randomly selected number.
def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    print("I am thinking of a number from 1 to 10.")
    secret_number = random.randint(1, 10)

    for attempt in range(1, 4):
        guess_text = input(f"Attempt {attempt} of 3 — your guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a whole number from 1 to 10.")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
        elif guess == secret_number:
            print(f"Correct! You guessed it in {attempt} attempt(s).")
            break
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")
    else:
        print(f"Good try! The number was {secret_number}.")


def show_menu():
    """Display the main menu."""
    print("\n========================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("0. Quit")
    print("----------------------------------------")


def main():
    """Run the toolkit until the user chooses to quit."""
    print("Welcome to your Personal Mini-Toolkit!")
    print("Choose a tool and have fun.")

    while True:
        show_menu()
        choice = input("Choose an option (0-3): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            number_guessing_game()
        elif choice == "0":
            print("\nThank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Sorry, that is not a menu option. Please choose 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()
