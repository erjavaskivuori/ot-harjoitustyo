from repositories.user_repository import user_repository
from repositories.course_repository import course_repository
from repositories.task_repository import task_repository
from entities.user import User
from entities.course import Course
from entities.task import Task

class UsernameExistsError(Exception):
    def __init__(self, message="Username is taken"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ShortPasswordError(Exception):
    def __init__(self, message="Password must have at least 6 characters"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class InvalidCredentialsError(Exception):
    def __init__(self, message="Username and password don't match"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class StudyAppServices:
    def __init__(self, user_repo=user_repository, 
                course_repo=course_repository, 
                task_repo=task_repository):

        self._user_repo = user_repo
        self._course_repo = course_repo
        self._task_repo = task_repo
        self._user = None

    def create_user(self, username, password):

        if self._user_repo.find_by_username(username):
            raise UsernameExistsError()
        
        if len(password) < 6:
            raise ShortPasswordError()

        self._user = self._user_repo.create_user(username, password)

    def login(self, username, password):

        if self._user_repo.find_password(username, password):
            raise InvalidCredentialsError
        else:
            self._user = self._user_repo.find_password(username, password)

    def logout(self):
        if self._user != None:
            self._user = None
        else:
            return False