from database_connection import form_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")

    cursor.execute("DROP TABLE IF EXISTS courses;")

    cursor.execute("DROP TABLE IF EXISTS courseTasks;")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT, 
        password TEXT);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        user_id INTEGER REFERENCES users, 
        name TEXT,
        visibility INTEGER);""")  # 0 or 1, 1 = visible

    cursor.execute("""CREATE TABLE IF NOT EXISTS courseTasks (
        id INTEGER PRIMARY KEY,
        course_id INTEGER REFERENCES courses,
        title TEXT,
        description TEXT,
        deadline TEXT,
        state INTEGER);""")  # 0 or 1, 0 = done, 1 = undone

    connection.commit()


def initialize_database():
    connection = form_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
