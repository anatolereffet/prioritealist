import uuid
from typing import List


class Task:
    def __init__(self, task_name: str, task_category: str, due_date: str) -> None:
        self.task_name = task_name
        self.task_category = task_category
        self.due_date = due_date
        self.status = False


class PrioriTeaList:
    def __init__(self) -> None:
        self.task_list: dict = {}
        self.task_mapper: dict = {}

    def add_task(self, task: Task) -> None:
        unique_id = str(uuid.uuid4())
        self.task_list[unique_id] = {
            "task": task.task_name,
            "category": task.task_category,
            "due_date": task.due_date,
            "status": task.status,
        }
        self.task_mapper[task.task_name] = unique_id

    def complete_task(self, task_name: str) -> None:
        active_unique_id = self.task_mapper.get(task_name)
        self.task_list[active_unique_id]["status"] = True

    def remove_task(self, task_name: str) -> None:
        active_unique_id = self.task_mapper.get(task_name)
        del self.task_list[active_unique_id]

    def show_tasks(self) -> List:
        return list(self.task_list.values())


# x = Task('allerboulangerie', task_category='nourriture', due_date='04-12-2023')
