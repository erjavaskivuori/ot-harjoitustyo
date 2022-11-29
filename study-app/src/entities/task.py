from entities.course import Course


class Task:
    def __init__(self, id: int, course: Course, description: str, visibility: int):
        self.id = id
        self.course = course
        self.description = description
        self.visibility = visibility
