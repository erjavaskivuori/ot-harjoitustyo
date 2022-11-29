from database_connection import form_database_connection
from entities.task import Task
from entities.course import Course


class TaskRepository:

    def __init__(self, connection: form_database_connection):

        self._connection = connection

    def create_task(self, course: Course, description):

        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO courseTasks (course_id, description
                        visibility VALUES (?, ?, ?)""",
                       [course.id, description, 1])
        self._connection.commit()

        return Task(cursor.lastrowid, course, description, 1)

    def get_tasks_by_course(self, course: Course):

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM courseTasks WHERE visibility=1 AND course_id=?", [course.id])
        rows = cursor.fetchall()

        return [Task(row(0), course, row[2], row(3)) for row in rows]

    def remove_task(self, task: Task):

        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE courseTasks SET visibility=0 WHERE id=?", [task.id])
        self._connection.commit()


task_repository = TaskRepository(form_database_connection())
