from typing import Protocol, List, Optional
from models import Project


class IProjectRepository(Protocol):
    def list(self) -> List[Project]: ...
    def add(self, project: Project) -> None: ...
    def get(self, index: int) -> Optional[Project]: ...
    def delete(self, index: int) -> Project: ...


class InMemoryProjectRepository:
    def __init__(self) -> None:
        self._projects: list[Project] = []

    def list(self) -> list[Project]:
        return list(self._projects)

    def add(self, project: Project) -> None:
        self._projects.append(project)

    def get(self, index: int) -> Optional[Project]:
        if 0 <= index < len(self._projects):
            return self._projects[index]
        return None

    def delete(self, index: int) -> Project:
        return self._projects.pop(index)
