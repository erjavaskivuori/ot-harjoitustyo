import unittest
from repositories.course_repository import course_repository
from entities.course import Course
from entities.user import User


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.remove_all_courses()
        self.test_user = User(1, "test_user", "password")
        self.test_course = Course(1, self.test_user, "test", 1)

    def test_create_course(self):
        course_repository.create_course(self.test_user, "test")
        courses = course_repository.get_users_courses(self.test_user)

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, self.test_course.name)

    def test_get_users_courses(self):
        course1 = course_repository.create_course(self.test_user, "course1")
        course2 = course_repository.create_course(self.test_user, "course2")

        courses = course_repository.get_users_courses(self.test_user)

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].name, course1.name)
        self.assertEqual(courses[1].name, course2.name)

    def test_remove_course(self):
        course = course_repository.create_course(self.test_user, "course")
        course_repository.remove_course(course)
        courses = course_repository.get_users_courses(self.test_user)

        self.assertEqual(len(courses), 0)
