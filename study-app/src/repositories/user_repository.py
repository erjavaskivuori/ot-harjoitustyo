from database_connection import form_database_connection
from entities.user import User


class UserRepository:

    def __init__(self, connection: form_database_connection):

        self._connection = connection

    def find_all_users(self):

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row[0], row[1], row[2]) for row in rows]

    def find_by_username(self, username: str):

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, username, password FROM users WHERE username=?", [username])
        row = cursor.fetchone()

        return User(row[0], row[1], row[2])


    def create_user(self, username: str, password: str):

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO users (username, password)
                        VALUES (?, ?)""", [username, password])
        self._connection.commit()

        return User(cursor.lastrowid, username, password)

    def delete_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM users""")
        self._connection.commit()


user_repository = UserRepository(form_database_connection())
