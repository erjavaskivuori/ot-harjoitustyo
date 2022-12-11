import unittest
from repositories.task_repository import task_repository
from entities.task import Task
from entities.course import Course
from entities.user import User


class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        task_repository.remove_all_tasks()
        self.test_user = User(1, "test_user", "password")
        self.test_course = Course(1, self.test_user, "test", 1)
        self.test_task = Task(1, self.test_course, "title", "description", 12/12/2022, 1)

    def test_create_task(self):
        task_repository.create_task(self.test_course, "title", "description", 12/12/2022)
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, self.test_task.title)

    def test_changing_task_state_works(self):
        task = task_repository.create_task(self.test_course, "title", "description", 12/12/2022)
        task_repository.change_state(task, 0)
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(tasks[0].state, 0)

    def test_find_all_tasks_by_course(self):
        task = task_repository.create_task(self.test_course, "title", "description", 12/12/2022)
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(tasks[0].description, task.description)
