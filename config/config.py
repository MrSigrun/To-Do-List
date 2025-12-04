from typing import Final
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_OF_NUMBER_MAX: Final[int] = int(os.getenv("PROJECT_OF_NUMBER_MAX", 10))
TASK_OF_NUMBER_MAX: Final[int] = int(os.getenv("TASK_OF_NUMBER_MAX", 50))
DATE_FORMAT: Final[str] = "%Y-%m-%d"
