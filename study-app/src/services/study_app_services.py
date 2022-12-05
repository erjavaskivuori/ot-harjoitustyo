from repositories.user_repository import user_repository
from repositories.course_repository import course_repository
from repositories.task_repository import task_repository


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class StudyAppServices:
    def __init__(self, user_repo=user_repository,
                 course_repo=course_repository,
                 task_repo=task_repository):

        self._user_repo = user_repo
        self._course_repo = course_repo
        self._task_repo = task_repo
        self._user = None
        self._course = None

    def create_user(self, username, password):

        if self._user_repo.find_by_username(username):
            raise UsernameExistsError()

        self._user = self._user_repo.create_user(username, password)

    def login(self, username, password):

        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError

        self._user = user

        return user

    def logout(self):
        if self._user is not None:
            self._user = None

    def get_current_user(self):
        return self._user

    def create_course(self, name):
        self._course_repo.create_course(self._user, name)

    def get_undone_courses(self):
        if self._user is not None:
            courses = self._course_repo.get_users_courses(self._user)
            return courses
        return None

    def get_current_course(self):
        return self._course

    def add_task(self, description):
        if self._course is not None:
            task = self._task_repo.create_task(self._course, description)
            self._course.tasks.append(task)

    def set_task_done(self, task):
        self._task_repo.remove_task(task)


study_app_service = StudyAppServices()
