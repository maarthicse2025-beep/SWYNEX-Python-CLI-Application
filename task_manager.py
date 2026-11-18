import os

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task():
    task = input("Enter new task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        print("\n1. Add Task | 2. View Tasks | 3. Delete Task | 4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
