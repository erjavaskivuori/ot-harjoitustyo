from tkinter import ttk, constants, StringVar, font
from services.study_app_service import study_app_service
from ui.navigation import Navigation


class AllCoursesView:
    """Kaikkien käyttäjän kurssien näkymästä vastaava luokka."""

    def __init__(self, root, show_course, show_all_tasks, logout):
        """Luokan konstruktori. Luo uuden kaikkien kurssien näkymän.

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan.
            show_course:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään kurssinäkymään.
            show_all_tasks:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään kaikkien tehtävien näkymään.
            logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
        """

        self._root = root
        self._show_course = show_course
        self._show_all_tasks = show_all_tasks
        self._logout = logout
        self._user = study_app_service.get_current_user()
        self._courses = study_app_service.get_undone_courses()
        self._frame = None
        self._course_name_entry = None
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        """Vastaa käyttäjän kirjaamisesta ulos."""

        study_app_service.logout()
        self._show_welcome_view()

    def _create_course_field(self):
        """Alustaa kentän, johon annetaan uuden kurssin nimi."""

        create_label = ttk.Label(
            master=self._frame,
            text="Create new course"
        )

        self._course_name_entry = ttk.Entry(master=self._frame)

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_course_handler
        )

        create_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)
        self._course_name_entry.grid(
            row=5, padx=5, pady=5, sticky=constants.EW)
        create_button.grid(row=5, padx=5, pady=5, sticky=constants.E)

    def _create_course_handler(self):
        """Vastaa uuden kurssin luomisesta."""

        name = self._course_name_entry.get()

        if name == "" or name.isspace():
            self._show_error("Give at least one character")
        else:
            study_app_service.create_course(name)
            self._show_course()

    def _initialize_course_entity(self, course):
        """Alustaa painikkeen yksittäiselle kurssille.

        Args:
            course: Kurssi Course-oliona.
        """

        course_button = ttk.Button(
            master=self._frame,
            text=f"{course.name}",
            command=lambda: [study_app_service.set_current_course(
                course), self._show_course()]
        )

        course_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _show_error(self, error):
        if self._error is not None:
            self._error.set(error)
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        navigation = Navigation(self._frame, None, self._logout)
        navigation.initialize(0)

        label = ttk.Label(
            master=self._frame,
            text=f"Welcome {self._user.username}!",
            font=font.Font(weight='bold')
        )

        label.grid(row=2, padx=5, pady=5, sticky=constants.W)

        self._create_course_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        if self._courses:
            courses_label = ttk.Label(
                master=self._frame,
                text="Your courses:",
                font=font.Font(weight='bold')
            )

            courses_label.grid(padx=5, pady=5, sticky=constants.W)

            for course in self._courses:
                self._initialize_course_entity(course)

        tasks_view_button = ttk.Button(
            master=self._frame,
            text="See all tasks",
            command=self._show_all_tasks
        )

        tasks_view_button.grid(padx=5, pady=20, sticky=constants.N)

        self._hide_error()
