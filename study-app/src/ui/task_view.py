import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, constants, StringVar, font
from services.study_app_service import study_app_service
from ui.navigation import Navigation


class CreateTaskView:
    """Tehtävän luomisnäkymästä vastaava luokka."""

    def __init__(self, root, course_view, logout):
        """Luokan konstruktori. Luo uuden luomisnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            course_view :
                Kutsuttava arvo, jota kutsutaan, kun luodaan kurssi tai
                palataan takaisin kurssinäkymään.
            logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
        """

        self._root = root
        self._frame = None
        self._course_view = course_view
        self._logout = logout
        self._title_entry = None
        self._description_entry = None
        self._deadline_entry = None
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _title_field(self):
        """Alustaa kentän, johon annetaan tehtävän otsikko."""

        title_label = ttk.Label(
            master=self._frame,
            text="Title"
        )
        self._title_entry = ttk.Entry(master=self._frame)

        title_label.grid(padx=5, pady=5, sticky=constants.W)
        self._title_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _description_field(self):
        """Alustaa kentän, johon annetaan tehtävän kuvaus."""

        title_label = ttk.Label(
            master=self._frame,
            text="Description (optional)"
        )

        self._description_entry = tk.Text(
            master=self._frame,
            height=4,
            background="white",
            relief="solid"
        )

        title_label.grid(padx=5, pady=5, sticky=constants.W)
        self._description_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _deadline_field(self):
        """Alustaa kalenteri-ikkunan, josta valitaan määräpäivä."""

        label = ttk.Label(
            master=self._frame,
            text="Select due date"
        )

        self._deadline_entry = DateEntry(
            master=self._frame,
            selectmode="day",
            textvariable=StringVar()
        )

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._deadline_entry.grid(padx=5, pady=5, sticky=constants.W)

    def _create_task_handler(self):
        """Vastaa tehtävän luomisesta."""

        title = self._title_entry.get()
        description = self._description_entry.get("1.0", 'end-1c')
        deadline = self._deadline_entry.get_date()
        deadline = deadline.strftime("%d.%m.%Y")

        if title == "" or title.isspace():
            self._show_error("Title must have at least one character")
        elif len(title) > 30:
            self._show_error("Title is too long")
        else:
            study_app_service.add_task(title, description, deadline)
            self._course_view()

    def _show_error(self, error):
        if self._error is not None:
            self._error.set(error)
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        navigation = Navigation(self._frame, self._course_view, self._logout)
        navigation.initialize(1)

        label = ttk.Label(
            master=self._frame,
            text="Create new task",
            font=font.Font(weight='bold')
        )

        label.grid(row=1, padx=5, pady=5, sticky=constants.W)

        self._title_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._description_field()
        self._deadline_field()

        add_task_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._create_task_handler
        )

        add_task_button.grid(padx=5, pady=5, sticky=constants.S)

        self._hide_error()


class TaskView:
    """Tehtävänäkymästä vastaava luokka. Näyttää yksittäisen
        tehtävän tarkemmat tiedot."""

    def __init__(self, root, previous_view, logout):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            previous_view:
                Kutsuttava arvo, jota kutsutaan, kun palataan kurssinäkymään.
        """

        self._root = root
        self._previous_view = previous_view
        self._logout = logout
        self._task = study_app_service.get_current_task()
        self._task_state = self._task.state
        self._frame = None

        self.initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        navigation = Navigation(self._frame, self._previous_view, self._logout)
        navigation.initialize(1)

        title = ttk.Label(
            master=self._frame,
            text=f"{self._task.title}",
            font=font.Font(weight='bold')
        )

        description = ttk.Label(
            master=self._frame,
            text=f"Description:\n{self._task.description}"
        )

        deadline = ttk.Label(
            master=self._frame,
            text=f"Deadline: {self._task.deadline}"
        )

        set_done = ttk.Button(
            master=self._frame,
            text="Set done",
            command=lambda: [
                study_app_service.change_task_state(self._task, 0),
                self._previous_view()
            ]
        )

        set_undone = ttk.Button(
            master=self._frame,
            text="Return task to To-do-list",
            command=lambda: [
                study_app_service.change_task_state(self._task, 1),
                self._previous_view()
            ]
        )

        title.grid(row=1, padx=5, pady=5, sticky=constants.W)
        description.grid(row=3, padx=5, pady=5, sticky=constants.W)
        deadline.grid(row=9, padx=5, pady=5, sticky=constants.W)

        if self._task.state == 1:
            set_done.grid(row=11, padx=5, pady=10, sticky=constants.W)
        if self._task.state == 0:
            set_undone.grid(row=11, padx=5, pady=10, sticky=constants.W)
