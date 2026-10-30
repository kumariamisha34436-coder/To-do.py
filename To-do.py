import os

FILENAME = "todo.txt"

# Function to load tasks from file into a list of dictionaries/lists
def load_tasks():
    tasks = []
    if not os.path.exists(FILENAME):
        return tasks
    
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Format in file: title|status
                    parts = line.split("|")
                    if len(parts) == 2:
                        tasks.append({"title": parts[0], "status": parts[1]})
    except Exception as e:
        print(f"Error loading file: {e}")
    return tasks

# Function to save tasks to file after every modification
def save_tasks(tasks):
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(f"{task['title']}|{task['status']}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Function to add a task (Option 1)
def add_task(tasks):
    title = input("Task: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    
    tasks.append({"title": title, "status": "Pending"})
    save_tasks(tasks)
    print(f"Task added. {len(tasks)} | {title} | Pending")

# Function to view all tasks (Option 2)
def view_tasks(tasks):
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return
    
    for idx, task in enumerate(tasks, 1):
        # Format status string display
        status = "Done" if task["status"] == "Done" else "Pending"
        print(f"{idx} | {task['title']} | {status}")

# Function to mark a task as completed (Option 3)
def complete_task(tasks):
    try:
        task_num = int(input("Enter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Done"
            save_tasks(tasks)
            print(f"Task {task_num} marked as completed.")
        else:
            print(f"Task number {task_num} not found.")
    except ValueError:
        print("Invalid input! Please enter a valid numerical task number.")

# Function to delete a task (Option 4)
def delete_task(tasks):
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task {task_num} deleted. Tasks left: {len(tasks)}")
        else:
            print(f"Task number {task_num} not found.")
    except ValueError:
        print("Invalid input! Please enter a valid numerical task number.")

# Main menu loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from 1 to 5.")

if __name__ == "__main__":
    main()