from database_connection import form_database_connection
from entities.task import Task
from entities.course import Course
from entities.user import User


class TaskRepository:
    """Luokka, joka vastaa tehtäviin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection: form_database_connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def create_task(self, course: Course, title, description, deadline):
        """Tallentaa tehtävän tietokantaan.

        Args:
            course: Kurssi, johon tehtävä liittyy, Course-oliona.
            title: Tehtävän otsikko merkkijonoarvona.
            description: Tehtävän tarkempi kuvaus merkkijonoarvona.
            deadline: Tehtävän määräpäivä päivämääräoliona.

        Returns:
            Palauttaa tallennetun tehtävän Task-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO courseTasks (course_id, title, description,
                        deadline, state) VALUES (?, ?, ?, ?, ?)""",
                       [course.id, title, description, deadline, 1])
        self._connection.commit()

        return Task(cursor.lastrowid, course, title, description, deadline, 1)

    def get_tasks_by_course(self, course: Course):
        """Palauttaa kaikki kurssiin liittyvät tehtävät.

        Args:
            course: Course-oliona kurssi, johon liittyvät tehtävät palautetaan.

        Returns:
            Palauttaa listan Task-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM courseTasks WHERE course_id=?", [course.id])
        rows = cursor.fetchall()

        return [Task(row[0], course, row[2], row[3], row[4], row[5]) for row in rows]

    def get_all_users_tasks(self, user: User):
        """Palauttaa kaikki käyttäjän tehtävät.

        Args:
            user: User-oliona käyttäjä, johon liittyvät tehtävät palautetaan.

        Returns:
            Palauttaa listan, joka sisältää tehtävän tiedot sisältäviä listoja.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            """SELECT T.title, C.name, T.deadline, T.state
            FROM courses C, courseTasks T 
            WHERE C.visibility = 1 AND T.course_id = C.id AND C.user_id=?
            ORDER BY T.deadline""", [user.id])
        rows = cursor.fetchall()

        return [[row[0], row[1], row[2], row[3]] for row in rows]

    def change_state(self, task: Task, state):
        """Muuttaa yksittäisen tehtävän tilaa tehdyksi tai tekemättömäksi.

        Args:
            task: Muutettava tehtävä Task-oliona.
            state:
                Kokonaislukuarvo, joka kuvaa tilaa, johon tehtävä halutaan muuttaa.
                Arvo on 0 eli tehty tai 1 eli tekemätön.
        """

        cursor = self._connection.cursor()
        if state == 0:
            cursor.execute(
                "UPDATE courseTasks SET state=0 WHERE id=?", [task.id])
        else:
            cursor.execute(
                "UPDATE courseTasks SET state=1 WHERE id=?", [task.id])
        self._connection.commit()

    def remove_all_tasks(self):
        """Poistaa kaikki tehtävät tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM courseTasks""")
        self._connection.commit()


task_repository = TaskRepository(form_database_connection())
