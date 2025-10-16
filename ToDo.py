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


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, title, description="", deadline=None):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added to project '{self.name}' successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in this project.")
            return
        print(f"\nTasks in project: {self.name}")
        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. {t}")

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


class ToDoManager:
    def __init__(self):
        self.projects = []

    def add_project(self, name):
        self.projects.append(Project(name))
        print(f"Project '{name}' created successfully!")

    def view_projects(self):
        if not self.projects:
            print("No projects yet.")
            return
        print("\nList of Projects:")
        for i, p in enumerate(self.projects, 1):
            print(f"{i}. {p.name}")

    def select_project(self, index):
        if 0 <= index < len(self.projects):
            return self.projects[index]
        print("Invalid project number.")
        return None

    def delete_project(self, index):
        if 0 <= index < len(self.projects):
            removed = self.projects.pop(index)
            print(f"Deleted project: '{removed.name}'")
        else:
            print("Invalid project number.")


def main():
    manager = ToDoManager()

    while True:
        print("\n===== To-Do List (Projects Mode) =====")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Select Project")
        print("4. Delete Project")
        print("5. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter new project name: ").strip()
            manager.add_project(name)

        elif choice == "2":
            manager.view_projects()

        elif choice == "3":
            manager.view_projects()
            try:
                index = int(input("Enter project number: ")) - 1
                project = manager.select_project(index)
                if project:
                    project_menu(project)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            manager.view_projects()
            try:
                index = int(input("Enter project number to delete: ")) - 1
                manager.delete_project(index)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


def project_menu(project):
    while True:
        print(f"\n===== Project: {project.name} =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Change Task Status")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description (optional): ")
            deadline = input(f"Enter deadline ({DATE_FORMAT}) or leave blank: ").strip() or None
            project.add_task(title, description, deadline)

        elif choice == "2":
            project.view_tasks()

        elif choice == "3":
            project.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                project.delete_task(index)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            project.view_tasks()
            try:
                index = int(input("Enter task number to change status: ")) - 1
                status = input("Enter new status (todo/doing/done): ").strip().lower()
                project.change_status(index, status)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
