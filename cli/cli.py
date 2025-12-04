from typing import Callable
from service import ToDoService
from config import DATE_FORMAT
from models import Project


class ConsoleIO:
    def __init__(
        self,
        inp: Callable[[str], str] = input,
        out: Callable[[str], None] = print
    ) -> None:
        self.inp = inp
        self.out = out


class CLI:
    def __init__(self, service: ToDoService, io: ConsoleIO) -> None:
        self.service = service
        self.io = io

    def run(self) -> None:
        while True:
            self.io.out("\n===== TODO MENU =====")
            self.io.out("1. Add Project")
            self.io.out("2. View Projects")
            self.io.out("3. Delete Project")
            self.io.out("4. Select Project")
            self.io.out("5. Exit")

            choice = self.io.inp("Enter choice: ")

            try:
                if choice == "1":
                    name = self.io.inp("Project name: ")
                    desc = self.io.inp("Description: ")
                    self.service.create_project(name, desc)

                elif choice == "2":
                    for i, p in enumerate(self.service.list_projects(), 1):
                        self.io.out(f"{i}. {p.name}")

                elif choice == "3":
                    idx = int(self.io.inp("Project number: ")) - 1
                    self.service.delete_project(idx)

                elif choice == "4":
                    projects = self.service.list_projects()
                    for i, p in enumerate(projects, 1):
                        self.io.out(f"{i}. {p.name}")
                    idx = int(self.io.inp("Select: ")) - 1
                    self.project_menu(idx, projects[idx])

                elif choice == "5":
                    break

                else:
                    self.io.out("Invalid option")

            except Exception as e:
                self.io.out(f"Error: {e}")

    def project_menu(self, project_index: int, project: Project) -> None:
        while True:
            self.io.out(f"\n--- {project.name} ---")
            self.io.out("1. Add Task")
            self.io.out("2. View Tasks")
            self.io.out("3. Change Status")
            self.io.out("4. Back")

            choice = self.io.inp("Choose: ")

            try:
                if choice == "1":
                    title = self.io.inp("Title: ")
                    desc = self.io.inp("Description: ")
                    dl = self.io.inp(f"Deadline ({DATE_FORMAT}) or blank: ") or None
                    self.service.add_task_to_project(project_index, title, desc, dl)

                elif choice == "2":
                    for i, t in enumerate(project.tasks, 1):
                        self.io.out(f"{i}. {t}")

                elif choice == "3":
                    i = int(self.io.inp("Task number: ")) - 1
                    s = self.io.inp("New status: ")
                    self.service.change_task_status(project_index, i, s)

                elif choice == "4":
                    break

                else:
                    self.io.out("Invalid")

            except Exception as e:
                self.io.out(f"Error: {e}")
