import os
import pickle

# Get the terminal width to print horizontal line
term_size: int = os.get_terminal_size()
file_name: str = "tasks.pkl"

# Initialize an empty list to store tasks
tasks: list = []

# load the existing tasks
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        tasks = pickle.load(file)

# Function to save tasks
def save_tasks():
    with open(file_name, "wb") as file:
        pickle.dump(tasks, file)

# Function to add a task
def add_task(task: str):
    tasks.append({"name":task, "status":"to-do"})
    save_tasks()
    print("Task added!")
    print('=' * term_size.columns)

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks to show!")
    else:    
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            if 'to-do' == task.get('status'):
                print(f"{idx}. TODO: {task.get('name')} <<<<<<<")
            if 'done' == task.get('status'):
                print(f"{idx}. DONE: {task.get('name')}")
    print('=' * term_size.columns)

# Function to complete the task
def complete_tasks(task_no: int):
    if not task_no or task_no < 1:
        print("Task number not valid!")
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            if idx == task_no:
                task['status'] = 'done'
        save_tasks()
        print("Task completed!")
    else:
        print("No task to complete!")
    print('=' * term_size.columns)

# Function to delete the task
def delete_tasks(task_no: int):
    if not task_no or task_no < 1:
        print("Task number not valid!")
    if tasks:
        del tasks[int(task_no) - 1]
        save_tasks()
        print("Task deleted!")
    else:    
        print("No task to delete!")
    print('=' * term_size.columns)

if '__main__' == __name__:
    # Main loop
    while True:
        print("1. Add Task        2. View Tasks")
        print("3. Mark Completed  4. Delete Task")
        print("5. Quit ")
        print('=' * term_size.columns)

        choice: str = input("Select an option: ")
        
        if choice == "1":
            task_name: str = input("Enter task: ")
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_no: int = int(input("Enter task number: "))
            complete_tasks(task_no)
        elif choice == "4":
            task_no: int = int(input("Enter task number: "))
            delete_tasks(task_no)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
