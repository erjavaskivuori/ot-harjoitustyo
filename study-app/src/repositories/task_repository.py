from database_connection import form_database_connection
from entities.task import Task
from entities.course import Course


class TaskRepository:

    def __init__(self, connection: form_database_connection):

        self._connection = connection

    def create_task(self, course: Course, title, description, deadline):

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO courseTasks (course_id, title, description,
                        deadline, state) VALUES (?, ?, ?, ?, ?)""",
                       [course.id, title, description, deadline, 1])
        self._connection.commit()

    def get_tasks_by_course(self, course: Course):

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM courseTasks WHERE course_id=?", [course.id])
        rows = cursor.fetchall()

        return [Task(row[0], course, row[2], row[3], row[4], row[5]) for row in rows]

    def remove_task(self, task: Task):

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE courseTasks SET state=0 WHERE id=?", [task.id])
        self._connection.commit()

    def remove_all_tasks(self):
        cursor = self._connection.cursor()
        cursor.execute("""DELETE FROM courseTasks""")
        self._connection.commit()


task_repository = TaskRepository(form_database_connection())
