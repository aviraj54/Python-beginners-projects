tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
