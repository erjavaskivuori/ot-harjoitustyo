from ui.welcome_view import WelcomeView
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.all_courses_view import AllCoursesView
from ui.course_view import CourseView
from ui.task_view import CreateTaskView, TaskView
from ui.all_tasks_view import AllTasksView


class UI:
    """Luokka, joka vastaa sovelluksen käyttöliittymästä.
    """

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root: TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""

        self._show_welcome_view()

    def _hide_current_view(self):
        """Piilotttaa nykyisen näkymän."""

        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_welcome_view(self):
        """Näyttää sovelluksen ensimmäisen näkymän."""

        self._hide_current_view()

        self._current_view = WelcomeView(
            self._root,
            self._show_login_view,
            self._show_register_view
        )

        self._current_view.pack()

    def _show_login_view(self):
        """Näyttää sovelluksen kirjautumisnäkymän."""

        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_all_courses_view,
            self._show_welcome_view
        )

        self._current_view.pack()

    def _show_register_view(self):
        """Näyttää rekisteröitymisnäkymän."""

        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._show_all_courses_view,
            self._show_welcome_view
        )

        self._current_view.pack()

    def _show_all_courses_view(self):
        """Näyttää näkymän, jossa on kaikki käyttäjän kurssit."""

        self._hide_current_view()

        self._current_view = AllCoursesView(
            self._root,
            self._show_welcome_view,
            self._show_course_view,
            self._show_all_tasks_view
        )

        self._current_view.pack()

    def _show_course_view(self):
        """Näyttää yksittäisen kurssin."""

        self._hide_current_view()

        self._current_view = CourseView(
            self._root,
            self._show_all_courses_view,
            self._show_create_task_view,
            self._show_task_view
        )

        self._current_view.pack()

    def _show_create_task_view(self):
        """Näyttää näkymän, jossa voi luoda uuden tehtävän."""

        self._hide_current_view()

        self._current_view = CreateTaskView(
            self._root,
            self._show_course_view
        )

        self._current_view.pack()

    def _show_task_view(self):
        """Näyttää yksittäisen tehtävän."""

        self._hide_current_view()

        self._current_view = TaskView(
            self._root,
            self._show_course_view
        )

        self._current_view.pack()

    def _show_all_tasks_view(self):
        """Näyttää kaikki käyttäjän tehtävät järjestettynä määräpäivän mukaan."""

        self._hide_current_view()

        self._current_view = AllTasksView(
            self._root,
            self._show_all_courses_view,
            self._show_task_view
        )

        self._current_view.pack()
