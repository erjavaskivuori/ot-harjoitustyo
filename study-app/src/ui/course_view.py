from tkinter import ttk, constants, messagebox, font
from services.study_app_service import study_app_service
from ui.navigation import Navigation


class CourseView:
    """Kurssinäkymästä vastaava luokka. Näyttää yksittäisen kurssin tehtävät."""

    def __init__(self, root, previous_view, create_task, show_task, logout):
        """Luokan konstruktori. Luo uuden kurssinäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            previous_view:
                Kutsuttava arvo, jota kutsutaan, kun palataan kaikkien kurssien näkymään.
            create_task:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään tehtävän luomisnäkymään.
            show_task:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään tehtävänäkymään.
        """

        self._root = root
        self._frame = None
        self._previous_view = previous_view
        self._create_task = create_task
        self._show_task = show_task
        self._logout = logout
        self._course = study_app_service.get_current_course()
        self._course.tasks = study_app_service.get_tasks_by_course(
            self._course)

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_task_entity(self, task):
        """Alustaa painikkeen yksittäiselle tehtävälle.

        Args:
            task: Tehtävä Task-oliona.
        """

        task_button = ttk.Button(
            master=self._frame,
            text=f"{task.title}",
            command=lambda: [study_app_service.set_current_task(
                task), self._show_task()]
        )

        task_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_remove_course_popup(self):
        """Alustaa viesti-ikkunan kurssin poistamiselle.
        """

        msg_box = messagebox.askyesno(
            title="Remove course",
            message=f"Are you sure you want to remove {self._course.name} from your courses?",
        )

        if msg_box == True:
            study_app_service.remove_course(self._course)
            self._previous_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        navigation = Navigation(self._frame, self._previous_view, self._logout)
        navigation.initialize(1)

        label = ttk.Label(
            master=self._frame,
            text=f"{self._course.name}",
            font=font.Font(weight='bold')
        )

        label.grid(row=1, padx=5, pady=5, sticky=constants.W)

        add_task_button = ttk.Button(
            master=self._frame,
            text="Add task",
            command=self._create_task
        )

        add_task_button.grid(sticky=constants.N)

        todo_label = ttk.Label(
            master=self._frame,
            text="To-do:",
            font=font.Font(weight='bold')
        )

        todo_label.grid(padx=5, pady=5, sticky=constants.W)

        for task in self._course.tasks:
            if task.state == 1:
                self._initialize_task_entity(task)

        done_label = ttk.Label(
            master=self._frame,
            text="\nCompleted tasks:",
            font=font.Font(weight='bold')
        )

        done_label.grid(padx=5, pady=5, sticky=constants.W)

        for task in self._course.tasks:
            if task.state == 0:
                self._initialize_task_entity(task)

        remove_button = ttk.Button(
            master=self._frame,
            text="Remove course",
            command=self._initialize_remove_course_popup
        )

        remove_button.grid(padx=10, pady=10, sticky=constants.E)
