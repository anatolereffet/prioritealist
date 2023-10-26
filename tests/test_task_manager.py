"""
Test file for the main file of Prioritealist
"""
import pytest

from prioritealist.task_manager import Task, PrioriTeaList


def test_add_task():
    """Check if we can add a task to the task list"""
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    class_instance.add_task(task_instance)

    assert len(class_instance.task_list) == 1
    assert len(class_instance.task_mapper) == 1
    assert task_instance.task_name in class_instance.task_mapper


def test_complete_task():
    """Check if we can complete a task from the task list"""
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
    """Check if we can remove a task from the task list"""
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    class_instance.add_task(task_instance)
    class_instance.remove_task(task_instance.task_name)

    assert len(class_instance.task_list) == 0
    assert len(class_instance.task_mapper) == 0
    assert task_instance.task_name not in class_instance.task_mapper


def test_show_task_list():
    """Check if we can extract the task list"""
    class_instance = PrioriTeaList()
    class_instance.add_task(
        Task("going to the bakery", task_category="food", due_date="04-12-2023")
    )
    class_instance.add_task(
        Task("doing homework", task_category="school", due_date="01-11-2023")
    )

    class_output = class_instance.show_tasks()

    assert len(class_output) == 2
    assert len(class_output[0]) == 4
    assert len(class_output[1]) == 4

    assert class_output[0] == {
        "task": "going to the bakery",
        "category": "food",
        "due_date": "04-12-2023",
        "status": False,
    }
    assert class_output[1] == {
        "task": "doing homework",
        "category": "school",
        "due_date": "01-11-2023",
        "status": False,
    }


def test_add_task_exception():
    """Check if the exceptions are raised correclty"""
    class_instance = PrioriTeaList()
    task1_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    task2_instance = Task(
        "going to the bakery", task_category="food", due_date="10-01-2023"
    )
    class_instance.add_task(task1_instance)
    with pytest.raises(KeyError):
        class_instance.add_task(task2_instance)


def test_complete_task_exception():
    """
    Test for the 'complete_task' method when an exception (KeyError) is expected.

    :raises KeyError: If the 'complete_task' method does not raise a KeyError as expected.
    """
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    with pytest.raises(KeyError):
        class_instance.complete_task(task_instance.task_name)


def test_remove_task_exception():
    """
    Test for the 'remove_task' method when an exception (KeyError) is expected.

    :raises KeyError: If the 'remove_task' method does not raise a KeyError as expected.
    """
    class_instance = PrioriTeaList()
    task_instance = Task(
        "going to the bakery", task_category="food", due_date="04-12-2023"
    )
    with pytest.raises(KeyError):
        class_instance.remove_task(task_instance.task_name)
