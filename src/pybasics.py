import os

# Get the terminal width to print horizontal line
term_size = os.get_terminal_size()

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added!")

# Function to view tasks
def view_tasks():
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print('=' * term_size.columns)

# Main loop
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        task_name = input("Enter task: ")
        add_task(task_name)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
