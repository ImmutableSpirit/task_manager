import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip() for line in file]
    return tasks

def save_tasks(tasks):
    """Save tasks to a file."""    
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    """Display the current list of tasks."""
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks, task):
    """Add a new task to the list."""    
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks, task_num):
    """Delete a task from the list."""    
    try:        
        task_num = int(task_num)
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted!")
        return True
    except (ValueError, IndexError):
        print("Invalid task number.")
        return False

def complete_task(tasks, task_num):
    """Mark a task as complete."""    
    try:        
        tasks[task_num - 1] += " [COMPLETED]"
        save_tasks(tasks)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    """Main function to run the task manager."""
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter the number of the task to complete: "))
            complete_task(tasks, task_num)
        elif choice == '4':
            display_tasks(tasks)
            task_num = int(input("Enter the number of the task to delete: "))
            delete_task(tasks, task_num)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
