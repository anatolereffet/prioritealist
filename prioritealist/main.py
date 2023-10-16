import uuid
from typing import List


class Task:
    """Class to define a task
    """
    def __init__(self, task_name: str, task_category: str, due_date: str) -> None:
        """Construct all the necessary attributes for the task object.

        Args:
            task_name (str): name of the task
            task_category (str): category of the task
            due_date (str): the tasks due date
        """
        self.task_name = task_name
        self.task_category = task_category
        self.due_date = due_date
        self.status = False

class PrioriTeaList:
    """Class to define the task list
    """
    def __init__(self) -> None:
        """Construct all the necessary attribute for the task list.
        """
        self.task_list: dict = {}
        self.task_mapper: dict = {}

    def add_task(self, task: Task) -> None:
        """Add a new task to the list.

        Args:
            task (Task): Task object to add
        """
        unique_id = str(uuid.uuid4())
        self.task_list[unique_id] = {
            "task": task.task_name,
            "category": task.task_category,
            "due_date": task.due_date,
            "status": task.status,
        }
        self.task_mapper[task.task_name] = unique_id

    def complete_task(self, task_name: str) -> None:
        """Changes a task's status to completed

        Args:
            task_name (str): Name of the task to complete
        """
        active_unique_id = self.task_mapper.get(task_name)
        self.task_list[active_unique_id]["status"] = True

    def remove_task(self, task_name: str) -> None:
        """Remove a specific task from the task list

        Args:
            task_name (str): Name of the task to remove
        """
        active_unique_id = self.task_mapper.get(task_name)
        del self.task_list[active_unique_id]
        del self.task_mapper[task_name]
        

    def show_tasks(self) -> List:
        """Show the entire tasks and their attributes. Return all the values of the list.

        Returns:
            List: List of tasks to show
        """
        return list(self.task_list.values())