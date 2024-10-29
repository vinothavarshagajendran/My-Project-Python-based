# Initialize an empty list to store tasks
tasks = []

# Function to display the main menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
