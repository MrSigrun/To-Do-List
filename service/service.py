from typing import List
from models import Project, Task
from repository import IProjectRepository
from config import PROJECT_OF_NUMBER_MAX, TASK_OF_NUMBER_MAX


class ToDoService:

    def __init__(self, repo: IProjectRepository) -> None:
        self.repo = repo

    def create_project(self, name: str, description: str) -> None:
        if len(self.repo.list()) >= PROJECT_OF_NUMBER_MAX:
            raise RuntimeError("Project limit reached")
        if any(p.name == name for p in self.repo.list()):
            raise ValueError("Project name already exists")

        self.repo.add(Project(name=name, description=description))

    def list_projects(self) -> List[Project]:
        return self.repo.list()

    def delete_project(self, index: int) -> None:
        self.repo.delete(index)

    def add_task_to_project(
        self, project_index: int, title: str, description: str, deadline: str | None
    ) -> None:

        project = self.repo.get(project_index)
        if project is None:
            raise ValueError("Project not found")

        if len(project.tasks) >= TASK_OF_NUMBER_MAX:
            raise RuntimeError("Task limit reached")

        task = Task(title=title, description=description)
        task.set_deadline(deadline)
        project.add_task(task, TASK_OF_NUMBER_MAX)

    def change_task_status(self, project_index: int, task_index: int, status: str) -> None:
        project = self.repo.get(project_index)
        if project is None:
            raise ValueError("Project not found")

        if status not in ("todo", "doing", "done"):
            raise ValueError("Invalid status")

        project.tasks[task_index].status = status
