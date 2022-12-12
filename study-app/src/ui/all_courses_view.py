from tkinter import ttk, constants, StringVar
from services.study_app_service import study_app_service


class AllCoursesView:
    """Kaikkien käyttäjän kurssien näkymästä vastaava luokka."""

    def __init__(self, root, show_welcome_view, show_course_view):
        """Luokan konstruktori. Luo uuden kaikkien kurssien näkymän.

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan.
            show_welcome_view:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
            show_course_view:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään kurssinäkymään.
        """

        self._root = root
        self._show_welcome_view = show_welcome_view
        self._show_course_view = show_course_view
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

        create_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._course_name_entry.grid(
            row=3, padx=5, pady=5, sticky=constants.EW)
        create_button.grid(row=3, padx=5, pady=5, sticky=constants.E)

    def _create_course_handler(self):
        """Vastaa uuden kurssin luomisesta."""

        name = self._course_name_entry.get()

        if name == "":
            self._show_error("Give at least one character")
        else:
            study_app_service.create_course(name)
            self._show_course_view()

    def _initialize_course_entity(self, course):
        """Alustaa painikkeen yksittäiselle kurssille.

        Args:
            course: Kurssi Course-oliona.
        """

        course_button = ttk.Button(
            master=self._frame,
            text=f"{course.name}",
            command=lambda: [study_app_service.set_current_course(
                course), self._show_course_view()]
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
        label = ttk.Label(
            master=self._frame,
            text=f"Welcome {self._user.username}!"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(row=0, padx=5, pady=5, sticky=constants.W)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._show_welcome_view
        )

        logout_button.grid(row=0, padx=5, pady=5, sticky=constants.E)

        self._create_course_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        if self._courses is not None:
            for course in self._courses:
                self._initialize_course_entity(course)

        self._hide_error()
