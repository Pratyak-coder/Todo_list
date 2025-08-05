def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_list():
    print("Simple To-Do List Manager")
    print("Commands: add, remove, view, exit")
    tasks = load_tasks()
    
    while True:
        command = input("\nEnter command (add/remove/view/exit): ").lower().strip()
        
        if command == 'exit':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        elif command == 'add':
            add_task(tasks)
            save_tasks(tasks)
        elif command == 'remove':
            remove_task(tasks)
            save_tasks(tasks)
        elif command == 'view':
            view_tasks(tasks)
        else:
            print("Invalid command! Use add, remove, view, or exit.")

if __name__ == "__main__":
    todo_list()