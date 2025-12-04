from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from config import DATE_FORMAT


@dataclass
class Task:
    title: str
    description: str = ""
    status: str = "todo"
    deadline: Optional[datetime] = None

    def __post_init__(self) -> None:
        if len(self.title) > 30:
            raise ValueError("Task title must not exceed 30 characters!")
        if len(self.description) > 150:
            raise ValueError("Task description must not exceed 150 characters!")

    def set_deadline(self, value: Optional[str]) -> None:
        if not value:
            self.deadline = None
            return
        try:
            self.deadline = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format! Use {DATE_FORMAT}")

    def __str__(self) -> str:
        deadline_str = self.deadline.strftime(DATE_FORMAT) if self.deadline else "-"
        desc_str = f" | {self.description}" if self.description else ""
        return f"{self.title} ({self.status}){desc_str} | Deadline: {deadline_str}"


@dataclass
class Project:
    name: str
    description: str = ""
    tasks: list[Task] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.name) > 30:
            raise ValueError("Project name must not exceed 30 characters!")
        if len(self.description) > 150:
            raise ValueError("Project description must not exceed 150 characters!")

    def add_task(self, task: Task, max_tasks: int) -> None:
        if len(self.tasks) >= max_tasks:
            raise RuntimeError("Task limit reached")
        self.tasks.append(task)

    def delete_task(self, index: int) -> Task:
        return self.tasks.pop(index)
