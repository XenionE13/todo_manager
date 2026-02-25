import json
tasks = []

try:
    with open("todo.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    print("No existing todo list found. Starting a new one.")

while True:
    print("\nTodo List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("4. Delete Task")
    print("3. Save Tasks")

    try:
        choice = int(input("Choose an option (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        print("Viewing tasks...")

    elif choice == 2:
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print("Adding a task...")

    elif choice == 3:
        if not tasks:
            print("No tasks to delete.")
        else:
            try:
                tasks_number = int(input("Enter the task number to delete: "))
                deleted_task = tasks.pop(tasks_number - 1)
                print(f"Deleted task: {deleted_task}")
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

    elif choice == 4:
        print("Saving tasks...")
        with open("todo.json", "w") as file:
            json.dump(tasks, file, indent=4)
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")