from repositories.user_repository import user_repository
from repositories.course_repository import course_repository
from repositories.task_repository import task_repository


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class StudyAppService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, user_repo=user_repository,
                 course_repo=course_repository,
                 task_repo=task_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        Args:
            user_repo:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
            course_repo:
                Vapaaehtoinen, oletusarvoltaan CourseRepository-olio.
                Olio, jolla on CourseRepository-luokkaa vastaavat metodit.
            task_repo:
                Vapaaetoinen, oletusarvoltaan TaskRepository-olio.
                Olio, jolla on TaskRepository-luokkaa vastaavat metodit.
        """

        self._user_repo = user_repo
        self._course_repo = course_repo
        self._task_repo = task_repo
        self._user = None
        self._course = None
        self._task = None

    def create_user(self, username, password):
        """Luo uuden käyttäjän ja kirjaa tämän sisään.

        Args:
            username: Käyttäjänimi merkkijonoarvona.
            password: Käyttäjän salasana merkkijonoarvona.

        Raises:
            UsernameExistsError: Virhe joka tapahtuu, kun käyttäjänimi on jo käytössä.
        """

        if self._user_repo.find_by_username(username):
            raise UsernameExistsError()

        self._user = self._user_repo.create_user(username, password)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Käyttäjänimi merkkijonoarvona.
            password: Käyttäjän salasana merkkijonoarvona.

        Raises:
            InvalidCredentialsError: Virhe, joka tapahtuu,
                kun käyttäjänimi ja salasana eivät täsmää.

        Returns:
            Palauttaa kirjautuneen käyttäjän User-oliona.
        """

        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError

        self._user = user

        return user

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """

        self._user = None

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            Palauttaa User-olion.
        """

        return self._user

    def create_course(self, name):
        """Luo uuden kurssin.

        Args:
            name: Kurssin nimi merkkijonoarvona.
        """

        course = self._course_repo.create_course(self._user, name)
        self._course = course

    def get_undone_courses(self):
        """Palauttaa käyttäjän tekemättömät kurssit.

        Returns:
            Palauttaa listan Course-olioita, jos sovelluksessa on kirjautunut käyttäjä.
            Muutoin palauttaa None.
        """

        if self._user is not None:
            courses = self._course_repo.get_users_courses(self._user)
            return courses
        return None

    def set_current_course(self, course):
        """Asettaa tietyn kurssin sovelluksessa näkyviin.

        Args:
            course: Kurssi Course-oliona.
        """

        self._course = course

    def get_current_course(self):
        """Palauttaa nykyisen kurssin.

        Returns:
            Palauttaa Course-olion.
        """

        return self._course

    def remove_course(self, course):
        """Poistaa kurssin.

        Args:
            course: Kurssi Course-oliona.
        """

        self._course_repo.remove_course(course)

    def add_task(self, title, description, deadline):
        """Lisää kurssille tehtävän.

        Args:
            title: Tehtävän otsikko merkkijonoarvona.
            description: Tehtävän kuvaus merkkijonoarvona.
            deadline: Tehtävän määräpäivä päivämääräoliona.
        """

        if self._course is not None:
            task = self._task_repo.create_task(
                self._course, title, description, deadline)
            self._course.tasks.append(task)

    def get_tasks_by_course(self, course):
        """Palauttaa tietyn kurssin tehtävät.

        Args:
            course: Kurssi Course-oliona.

        Returns:
            Palauttaa listan Task-olioita.
        """

        tasks = task_repository.get_tasks_by_course(course)
        return tasks

    def change_task_state(self, task, state):
        """Muuttaa tietyn tehtävän tilaa tehdyksi tai tekemättömäksi.

        Args:
            task: Tehtävä Task-oliona.
            state:
                Kokonaislukuarvo, joka kuvaa tilaa, johon tehtävä halutaan muuttaa.
                Arvo on 0 eli tehty tai 1 eli tekemätön.
        """

        self._task_repo.change_state(task, state)

    def set_current_task(self, task):
        """Asettaa tietyn tehtävän sovelluksessa näkyviin.

        Args:
            task: Tehtävä Task-oliona.
        """

        self._task = task

    def get_current_task(self):
        """Palauttaa nykyisen tehtävän.

        Returns:
            Palauttaa Task-olion.
        """

        return self._task

    def get_all_users_tasks(self):
        """Palauttaa kaikki käyttäjän tehtävät.

        Returns:
            Palauttaa listan tehtävän tiedot sisältäviä listoja.
        """
        return self._task_repo.get_all_users_tasks(self._user)


study_app_service = StudyAppService()
