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
        self.test_task = Task(1, self.test_course, "test", 1)

    def test_create_task(self):
        task_repository.create_task(self.test_course, "test")
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, self.test_task.description)

    def test_removing_task_works(self):
        task = task_repository.create_task(self.test_course, "test")
        task_repository.remove_task(task)
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(len(tasks), 0)

    def test_find_all_tasks_by_course(self):
        task = task_repository.create_task(self.test_course, "test")
        tasks = task_repository.get_tasks_by_course(self.test_course)

        self.assertEqual(tasks[0].description, task.description)