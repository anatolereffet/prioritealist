"""
Task Manager Module (task_manager.py)

This module provides a simple task management system.
It allows you to create, manage, and track tasks within your application.

Usage:
    
Import this module to use the task manager functionality.
You can create, update, and delete tasks.
Tasks can have a title, description, due date, and status.
Use the functions and classes provided in this module to interact with the task manager.
"""
from .task_manager import Task, PrioriTeaList

__all__ = ["Task", "PrioriTeaList"]
__version__= "0.2.4"
