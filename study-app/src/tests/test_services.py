import unittest
from entities.user import User
from entities.course import Course
from entities.task import Task
from services.study_app_services import StudyAppServices, InvalidCredentialsError, UsernameExistsError

class FakeUserRepository():

    def __init__(self, users=None):
        self.users = users or []

    def find_all_users(self):
        return self.users

    def find_by_username(self, username):
        matching_users = list(filter(lambda user: user.username == username, self.users))

        if len(matching_users) > 0:
            return matching_users[0]

        return None

    def create_user(self, id, username, password):
        user = User(id, username, password)
        self.users.append(user)
        return user

    def delete_all_users(self):
        self.users = []
        
class FakeCourseRepository():
    def __init__(self, courses=None):
        self.courses = courses or []

    def create_course(self, id, owner: User, name: str):
        course = Course(id, owner, name, 1)
        self.courses.append(course)

        return Course # muuta tämä jos muutat oikeaa course-repoa

    def get_users_courses(self, user: User):
        user_courses = list(filter(lambda course: course.owner == user and 
            course.visibility == 1, self.courses))

        return user_courses

    def remove_course(self, course: Course):
        course.visibility = 0

    def remove_all_courses(self):
        self.courses = []

class FakeTaskRepository():
    def __init__(self, tasks=None):
        self.tasks = tasks or []

    def create_task(self, id, course: Course, description):

        task = Task(id, course, description, 1)
        self.tasks.append(task)

    def get_tasks_by_course(self, course: Course):

        course_tasks = list(filter(lambda task: task.course == course and 
            task.visibility == 1, self.tasks))

        return course_tasks

    def remove_task(self, task: Task):
        task.visibility = 0

    def remove_all_tasks(self):
        self.tasks = []

class TestStudyAppServices(unittest.TestCase):
    def setUp(self):
        self.studyapp_service = StudyAppServices(
            FakeUserRepository,
            FakeCourseRepository,
            FakeTaskRepository
        )

        self.test_user = User(1, "test_user", "password")
        self.course1 = Course(1, self.test_user, "course1", 1)
        self.course2 = Course(2, self.test_user, "course2", 1)
        self.task1 = Task(1, self.course1, "test", 1)
        self.task2 = Task(2, self.course2, "test", 1)

    def test_login_with_valid_credentials(self):
        self.studyapp_service.create_user(
            self.test_user.username,
            self.test_user.password
        )
        
        user = self.studyapp_service.login(
            self.test_user.username,
            self.test_user.password
        )

        self.assertEqual(user.username, self.test_user.username)