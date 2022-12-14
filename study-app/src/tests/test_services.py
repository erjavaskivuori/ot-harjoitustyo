import unittest
from entities.user import User
from entities.course import Course
from services.study_app_service import StudyAppService, InvalidCredentialsError, UsernameExistsError


class FakeUserRepository:

    def __init__(self, users=None):
        self.users = users or []

    def find_all_users(self):
        return self.users

    def find_by_username(self, username):
        matching_users = list(
            filter(lambda user: user.username == username, self.users))

        if len(matching_users) > 0:
            return matching_users[0]

        return None

    def create_user(self, username, password):
        user = User(1, username, password)
        self.users.append(user)
        return user

    def delete_all_users(self):
        self.users = []


class FakeCourseRepository:
    def __init__(self, courses=None):
        self.courses = courses or []

    def create_course(self, owner: User, name):
        course = Course(1, owner, name, 1)
        self.courses.append(course)

        return Course

    def get_users_courses(self, user: User):
        user_courses = list(filter(lambda course: course.owner == user and
                                   course.visibility == 1, self.courses))

        return user_courses

    def remove_course(self, course: Course):
        course.visibility = 0

    def remove_all_courses(self):
        self.courses = []


class TestStudyAppServices(unittest.TestCase):
    def setUp(self):
        self.studyapp_service = StudyAppService(
            FakeUserRepository(),
            FakeCourseRepository()
        )

        self.test_user = User(1, "testuser", "password")
        self.course1 = Course(1, self.test_user, "course1", 1)
        self.course2 = Course(2, self.test_user, "course2", 1)

    def login(self, user):
        self.studyapp_service.create_user(user.username, user.password)

    def set_course(self, course):
        self.studyapp_service.create_course(course)

    def test_create_user_with_non_existing_username(self):
        username = self.test_user.username
        password = self.test_user.password

        self.studyapp_service.create_user(username, password)

        user = self.studyapp_service.get_current_user()

        self.assertEqual(user.username, username)

    def test_create_user_with_existing_username(self):
        username = self.test_user.username
        password = self.test_user.password

        self.studyapp_service.create_user(username, password)

        self.assertRaises(
            UsernameExistsError,
            lambda: self.studyapp_service.create_user(username, "password1")
        )

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

    def test_login_with_invalid_credentials(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.studyapp_service.login("test", "wrong")
        )

    def test_create_course(self):
        self.login(self.test_user)

        self.studyapp_service.create_course("testcourse")
        courses = self.studyapp_service.get_undone_courses()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].owner.username, self.test_user.username)
        self.assertEqual(courses[0].name, "testcourse")