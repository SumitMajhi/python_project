import os
import json

Filename = "to_do_list.json"

def load_tasks():
    if os.path.exists(Filename):
        with open(Filename, 'r') as file:
            return json.load(file)
    return[]

def save_task(tasks):
    with open(Filename, 'w') as file:
        json.dump(tasks,file, indent=2)

def show_task(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\n To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['task']} {status}")
        print()  
    
def add_task(tasks):
    task = input("Enter Task :").strip()
    if task:
        tasks.append({'task': task, 'done': False})
        print("Task added successfully.")
    else:
        print("⚠️ Task cannot be empty.")

def mark_done(tasks):
    show_task(tasks)
    try:
        index= int(input("Enter task number to mark as done:"))
        if 1<= index <= len(tasks):
            tasks[index-1]['done'] = True
            print("Task marked as done.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Enter valid Task number")

def delete_task(tasks):
    show_task(tasks)
    try:
        index = int(input("Enter task number to delete:"))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index-1)
            print(f"Task {removed['task']} deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter valid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n To-do Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")
        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_task(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()