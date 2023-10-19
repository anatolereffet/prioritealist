"""
Test file for the main file of Prioritealist
"""

from prioritealist.main import Task, PrioriTeaList

desired_result = {
    "task": "going to the bakery",
    "category": "food",
    "due_date": "04-12-2023",
    "status": False,
}


def test_extract_task_list():
    """Check if we can extract the task list
    """
    class_instance = PrioriTeaList()
    class_instance.add_task(
        Task("going to the bakery", task_category="food", due_date="04-12-2023")
    )
    class_output = class_instance.show_tasks()

    assert len(class_output[0]) == 4
    assert class_output[0] == desired_result


def test_add_task():
    """Check if we can add a task to the task list
    """
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    class_instance.add_task(task_instance)

    assert len(class_instance.task_list.keys()) == 1
    assert task_instance.task_name in class_instance.task_mapper


def test_complete_task():
    """Check if we can complete a task from the task list
    """
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    class_instance.add_task(task_instance)
    task_id = class_instance.task_mapper[task_instance.task_name]

    assert class_instance.task_list[task_id]["status"] is False
    class_instance.complete_task(task_instance.task_name)
    assert class_instance.task_list[task_id]["status"] is True


def test_remove_task():
    """Check if we can remove a task from the task list
    """
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    class_instance.add_task(task_instance)
    class_instance.remove_task(task_instance.task_name)

    assert len(class_instance.task_list) == 0
    assert task_instance.task_name not in class_instance.task_mapper
