from prioritealist.main import Task, PrioriTeaList

desired_result = {
    "task": "going to the bakery",
    "category": "food",
    "due_date": "04-12-2023",
    "status": False,
}


def test_extract_task_list():
    class_instance = PrioriTeaList()
    class_instance.add_task(
        Task("going to the bakery", task_category="food", due_date="04-12-2023")
    )
    class_output = class_instance.show_tasks()
    assert len(class_output[0]) == 4
    assert class_output[0] == desired_result
