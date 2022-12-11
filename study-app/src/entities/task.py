from datetime import date
from entities.course import Course


class Task:
    def __init__(self, id: int, course: Course, title: str,
        description: str, deadline: date, state: int):
        self.id = id
        self.course = course
        self.title = title
        self.description = description
        self.deadline = deadline
        self.state = state
