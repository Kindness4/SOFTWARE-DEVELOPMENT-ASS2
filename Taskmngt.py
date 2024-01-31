import html
# List to store tasks
tasks = []
# Function to add a task to the tasks list
def add_task(task):
    tasks.append (task)
    print(f'Task "{task}" added successfully. All the best completing it.')
# Function to view all tasks in the tasks list
def view_tasks():
    if not tasks:
         print("No task added.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
# Function to mark a task as completed and remove it from the tasks list
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f'Task "{completed_task}" marked as complete.')
    else:
        print("Invalid task index.")
# Function to delete a task from the tasks list
def delete_task(task_index):
            if 1 <= task_index <= len(tasks):
                 deleted_task = tasks.pop(task_index -1)
                 print(f'Task "{deleted_task}" deleted successfully.')
            else:
                 print("Invalid task index.")
# Main loop for the Task Management System
while True:
    print("\nTask Management System:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task when completed")
    print("4. Delete Task")
    print("5. Exit")
# User input for option selection
    option = input("Select option(1-5): ")
# Handling different options based on user input
    if option == "1":
        new_task = input("Enter task description: ")
        add_task(new_task)
    elif option == "2":
        view_tasks()
    elif option == "3":
        view_tasks()
        task_index = int(input("Enter the task index to mark as completed: "))
        complete_task(task_index)
    elif option == "4":
        view_tasks()
        task_index = int(input("Enter the task index to delete"))
        delete_task(task_index)
    elif option == "5":
        print("Thumbs Up! task completed, Exiting Task Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

