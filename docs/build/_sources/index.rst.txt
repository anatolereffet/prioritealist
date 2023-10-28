.. PrioriTeaList documentation master file, created by
   sphinx-quickstart on Mon Oct 16 15:17:44 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#####################################
PrioriTeaList |release| documentation
#####################################

PrioriTeaList is a general mock-up python project made for the course BGDIA700 Télécom Paris 
to create a python to-do list library that can handle basic functionality, 
while holding general development standards.

Install
=======
.. code-block:: bash

   pip install prioritealist


Quickstart
==========
This is a simple example to showcase how PrioriTeaList works after being installed within your environment

.. code-block:: python

   from prioritealist import PrioriTeaList, Task

   task_list = PrioriTeaList()
   task_instance = Task(task_name='Complete homework',
                        task_category='school',
                        due_date='31-10-2023')

   #Adding your task directly to the lists of tasks.
   task_list.add_task(task_instance)

If you ever need to show your lists of tasks, simply call

.. autofunction:: prioritealist.task_manager.PrioriTeaList.show_tasks

.. code-block:: python

   print(task_list.show_tasks())
   >>>[{'task': 'Complete homework', 'category': 'school', 'due_date': '31-10-2023', 'status': False}]

If you finally completed your task, simply call

.. autofunction:: prioritealist.task_manager.PrioriTeaList.complete_task

.. code-block:: python

   task_list.complete_task('Complete homework')

If you need to remove this task, simply call

.. autofunction:: prioritealist.task_manager.PrioriTeaList.remove_task

.. code-block:: python

   task_list.remove_task('Complete homework')

Main functions
==============
The main classes are **PrioriTeaList** and **Task**, they'll help you go through your daily to-do list.

.. autofunction:: prioritealist.task_manager.PrioriTeaList

.. autofunction:: prioritealist.task_manager.Task

