import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.user_test = User(1, "test", "password")

    def test_create(self):
        user_repository.create_user("test", "password")
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_test.username)

    def test_find_by_username(self):
        user_repository.create_user("test", "password")
        user = user_repository.find_by_username("test")

        self.assertEqual(user.username, self.user_test.username)

    def test_find_all_users(self):
        user1 = user_repository.create_user("test1", "password1")
        user2 = user_repository.create_user("test2", "password2")

        users = user_repository.find_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, user1.username)
        self.assertEqual(users[1].username, user2.username)
