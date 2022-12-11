from database_connection import form_database_connection
from entities.user import User


class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def find_all_users(self):
        """Palauttaa kaikki tietokannassa olevat käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [User(row[0], row[1], row[2]) for row in rows]

    def find_by_username(self, username: str):
        """Palauttaa käyttäjän käyttäjänimen perusteella.

        Args:
            username: Merkkijonoarvo, joka kuvaa palautettavan käyttäjän käyttäjänimeä.

        Returns:
            Palauttaa User-olion, jos haettu käyttäjänimi löytyy tietokannasta.
            Muussa tapauksessa palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, username, password FROM users WHERE username=?", [username])
        row = cursor.fetchone()

        if row is not None:
            return User(row[0], row[1], row[2])

        return None

    def create_user(self, username: str, password: str):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            username: Käyttäjänimi merkkijonoarvona.
            password: Käyttäjän salasana merkkijonoarvona.

        Returns:
            Palauttaa User-olion.
        """

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO users (username, password)
                        VALUES (?, ?)""", [username, password])
        self._connection.commit()

        return User(cursor.lastrowid, username, password)

    def delete_all_users(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM users""")
        self._connection.commit()


user_repository = UserRepository(form_database_connection())
