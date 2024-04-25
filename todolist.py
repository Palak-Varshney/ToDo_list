import os
import json

class TodoList:
    def __init__(self, filename="todo.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print("Task added successfully!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task index")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['task']} [{status}]")
        else:
            print("No tasks found")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            self.save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task index")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task index")


def print_menu():
    print("\nTODO LIST MENU")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Update Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


def main():
    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "5":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()
