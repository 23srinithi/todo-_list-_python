# Simple To-Do List Application2

tasks = []

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
