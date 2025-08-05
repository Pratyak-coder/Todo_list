Simple To-Do List Manager
Overview
This is a command-line interface (CLI) to-do list application written in Python. It allows users to manage tasks by adding, removing, and viewing them. Tasks are persistently stored in a text file (tasks.txt) for retrieval across sessions.
Features

Add new tasks to the list.
Remove tasks by specifying their index.
View all tasks with numbered indices.
Save tasks to a file (tasks.txt) automatically after modifications.
Load tasks from the file on startup.
Simple command-based interface (add, remove, view, exit).

Requirements

Python 3.x

How to Run

Save the script as todo.py.
Open a terminal and navigate to the directory containing the script.
Run the script using:python todo.py


Follow the prompts:
Enter add to add a task.
Enter remove to delete a task by its number.
Enter view to see all tasks.
Enter exit to save tasks and quit.



Example Usage
Simple To-Do List Manager
Commands: add, remove, view, exit

Enter command (add/remove/view/exit): add
Enter task: Buy groceries
Task 'Buy groceries' added.

Enter command (add/remove/view/exit): view
To-Do List:
1. Buy groceries

Enter command (add/remove/view/exit): exit
Tasks saved. Goodbye!

Notes

Tasks are stored in tasks.txt in the same directory as the script.
Empty tasks are not allowed and will prompt an error.
Invalid commands or inputs (e.g., non-numeric input for remove) trigger error messages.
The application ensures tasks persist between sessions by saving to the file after each change.
