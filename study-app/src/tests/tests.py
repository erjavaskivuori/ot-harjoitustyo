import unittest
from repositories.user_repository import user_repository
from entities.user import User

class testUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_erja = User(1, "erja", "salasana")

    def test_create(self):
        user_repository.create_user("erja", "salasana")
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_erja.username)