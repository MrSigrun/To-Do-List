from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
PROJECT_OF_NUMBER_MAX = 10
TASK_OF_NUMBER_MAX = 50

class Task:
    def __init__(self, title, description="", deadline=None):
        if len(title) > 30:
            raise ValueError("Task title must not exceed 30 characters!")
        if len(description) > 150:
            raise ValueError("Task description must not exceed 150 characters!")
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
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, title, description="", deadline=None):
        if len(self.tasks) >= TASK_OF_NUMBER_MAX:
            print(f"Maximum number of tasks ({TASK_OF_NUMBER_MAX}) reached! Cannot add more tasks.")
            return
        try:
            task = Task(title, description, deadline)
            self.tasks.append(task)
            print(f"Task '{title}' added to project '{self.name}' successfully!")
        except ValueError as ve:
            print(f"Error adding task: {ve}")

    def edit_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            new_title = input("Enter new task title (max 30 characters): ").strip()
            if len(new_title) > 30:
                print("Task title must not exceed 30 characters! Returning to project menu.")
                return

            new_description = input("Enter new task description (max 150 characters): ").strip()
            if len(new_description) > 150:
                print("Task description must not exceed 150 characters! Returning to project menu.")
                return

            new_deadline = input(f"Enter new deadline ({DATE_FORMAT}) or leave blank: ").strip() or None
            if new_deadline:
                try:
                    datetime.strptime(new_deadline, DATE_FORMAT)
                except ValueError:
                    print(f"Invalid date format! Please use {DATE_FORMAT}. Returning to project menu.")
                    return

            new_status = input("Enter new status (todo/doing/done): ").strip().lower()
            if new_status not in ["todo", "doing", "done"]:
                print("Invalid status. Choose from: todo, doing, done. Returning to project menu.")
                return

            task.title = new_title
            task.description = new_description
            task.deadline = datetime.strptime(new_deadline, DATE_FORMAT) if new_deadline else None
            task.status = new_status
            print(f"Task '{task.title}' updated successfully!")
        else:
            print("Invalid task number.")

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

    def edit_project(self, projects):
        new_name = input("Enter new project name (max 30 characters): ").strip()
        if len(new_name) > 30:
            print("Project name must not exceed 30 characters! Returning to project menu.")
            return
        if any(p.name == new_name for p in projects if p != self):
            print("A project with this name already exists! Returning to project menu.")
            return

        new_description = input("Enter new project description (max 150 characters): ").strip()
        if len(new_description) > 150:
            print("Project description must not exceed 150 characters! Returning to project menu.")
            return

        self.name = new_name
        self.description = new_description
        print(f"Project '{self.name}' updated successfully!")

class ToDoManager:
    def __init__(self):
        self.projects = []

    def add_project(self, name, description):
        if len(name) > 30:
            print("Project name must not exceed 30 characters! Returning to main menu.")
            return
        if any(p.name == name for p in self.projects):
            print("A project with this name already exists! Returning to main menu.")
            return
        if len(description) > 150:
            print("Project description must not exceed 150 characters! Returning to main menu.")
            return
        if len(self.projects) >= PROJECT_OF_NUMBER_MAX:
            print("Maximum number of projects reached! Cannot add more projects.")
            return
        self.projects.append(Project(name, description))
        print(f"Project '{name}' created successfully!")

    def view_projects(self):
        if not self.projects:
            print("No projects yet. Returning to main menu.")
            return
        print("\nList of Projects:")
        for i, p in enumerate(self.projects, 1):
            print(f"{i}. {p.name} | Description: {p.description[:50]}")

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
        print("\n===== To-Do List =====")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Select Project")
        print("4. Delete Project")
        print("5. Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter new project name (max 30 characters): ").strip()
            if len(name) > 30:
                print("Project name must not exceed 30 characters! Returning to main menu.")
                continue
            if any(p.name == name for p in manager.projects):
                print("A project with this name already exists! Returning to main menu.")
                continue

            description = input("Enter project description (max 150 characters): ").strip()
            if len(description) > 150:
                print("Project description must not exceed 150 characters! Returning to main menu.")
                continue

            manager.add_project(name, description)

        elif choice == "2":
            manager.view_projects()

        elif choice == "3":
            if not manager.projects:
                print("No projects yet. Returning to main menu.")
                continue
            manager.view_projects()
            try:
                index = int(input("Enter project number: ")) - 1
                project = manager.select_project(index)
                if project:
                    project_menu(project, manager)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            if not manager.projects:
                print("No projects yet. Returning to main menu.")
                continue
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

def project_menu(project, manager):
    while True:
        print(f"\n===== Project: {project.name} =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Change Task Status")
        print("5. Edit Project")
        print("6. Edit Task")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title (max 30 characters): ").strip()
            if len(title) > 30:
                print("Task title must not exceed 30 characters! Returning to project menu.")
                continue

            description = input("Enter description (max 150 characters): ").strip()
            if len(description) > 150:
                print("Task description must not exceed 150 characters! Returning to project menu.")
                continue

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
            project.edit_project(manager.projects)

        elif choice == "6":
            project.view_tasks()
            try:
                index = int(input("Enter task number to edit: ")) - 1
                project.edit_task(index)
            except ValueError:
                print("Invalid input.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
