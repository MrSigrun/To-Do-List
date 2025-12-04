from repository import InMemoryProjectRepository
from service import ToDoService
from cli import CLI, ConsoleIO


def main() -> None:
    repo = InMemoryProjectRepository() 
    service = ToDoService(repo)           
    io = ConsoleIO()
    cli = CLI(service, io)
    cli.run()


if __name__ == "__main__":
    main()
