from database_connection import form_database_connection
from entities.user import User
from entities.course import Course


class CourseRepository:
    """Luokka, joka vastaa kursseihin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection: form_database_connection):
        """Luokan kontruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_course(self, owner: User, name: str):
        """Tallentaa kurssin tietokantaan.

        Args:
            owner: Kurssin omistaja User-oliona.
            name: Merkkijonoarvo, joka kuvaa kurssin nimeä.

        Returns:
            Tallennettu kurssi Course-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO courses (user_id, name, visibility)
                        VALUES (?, ?, ?)""", [owner.id, name, 1])
        self._connection.commit()

        return Course(cursor.lastrowid, owner, name, 1)

    def get_users_courses(self, user: User):
        """Palauttaa käyttäjän kurssit.

        Args:
            user: User-oliona käyttäjä, jonka kurssit palautetaan.

        Returns:
            Palauttaa listan Course-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM courses WHERE visibility=1 AND user_id=?", [user.id])
        rows = cursor.fetchall()

        return [Course(row[0], user, row[2], row[3]) for row in rows]

    def remove_course(self, course: Course):
        """Poistaa tietyn kurssin näkyvistä.

        Args:
            course: Poistettava kurssi Course-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE courses SET visibility=0 WHERE id=?", [course.id])
        self._connection.commit()

    def remove_all_courses(self):
        """Poistaa kaikki kurssit tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM courses""")
        self._connection.commit()


course_repository = CourseRepository(form_database_connection())
