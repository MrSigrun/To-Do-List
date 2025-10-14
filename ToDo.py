from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

class Task:
    def __init__(self, title, description="", deadline=None):
        self.title = title
        self.description = description
        self.status = "todo"
        self.deadline = None
        if deadline:
            self.set_deadline(deadline)

    def set_deadline(self, value):
        try:
            self.deadline = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            print(f"Invalid date format! Please use {DATE_FORMAT}.")
            self.deadline = None

    def __str__(self):
        deadline_str = self.deadline.strftime(DATE_FORMAT) if self.deadline else "-"
        desc_str = f" | {self.description}" if self.description else ""
        return f"{self.title} ({self.status}){desc_str} | Deadline: {deadline_str}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", deadline=None):
        if not title.strip():
            print("Error: Task title cannot be empty.")
            return
        task = Task(title.strip(), description.strip(), deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("\nList of Tasks:")
        for i, t in enumerate(self.tasks):
            print(f"{i + 1}. {t}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted task: '{removed.title}'")
        else:
            print("Invalid task number.")

    def change_status(self, index, new_status):
        valid_statuses = ["todo", "doing", "done"]
        if new_status not in valid_statuses:
            print("Invalid status. Choose from: todo, doing, done")
            return
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = new_status
            print(f"Task '{self.tasks[index].title}' status changed to '{new_status}'.")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Change Task Status")
        print("5. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            deadline = input(f"Enter deadline ({DATE_FORMAT}) or leave blank: ").strip()
            deadline = deadline if deadline else None
            todo.add_task(title, description, deadline)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            if not todo.tasks:
                print("No tasks to delete.")
                continue
            todo.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            if not todo.tasks:
                print("No tasks available.")
                continue
            todo.view_tasks()
            try:
                index = int(input("Enter task number to change status: ")) - 1
                new_status = input("Enter new status (todo/doing/done): ").strip().lower()
                todo.change_status(index, new_status)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            print("Thank you for using the To-Do List Application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
