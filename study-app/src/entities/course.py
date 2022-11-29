from entities.user import User


class Course:
    def __init__(self, id: int, owner: User, name: str, visibility: int):
        self.id = id
        self.owner = owner
        self.name = name
        self.visibility = visibility
        self.tasks = []  # list of task-entities
