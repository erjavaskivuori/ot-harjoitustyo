from tkinter import ttk, constants, font
from services.study_app_service import study_app_service
from ui.navigation import Navigation

class AllTasksView():
    def __init__(self, root, previous_view, logout):
        """Luokan konstruktori. Luo uuden näkymän kaikille käyttäjän tehtäville.

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan.
            previous_view:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään takaisin kaikkien 
                kurssien näkymään.
            logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
        """

        self._root = root
        self._frame = None
        self._previous_view = previous_view
        self._logout = logout
        self._tasks = study_app_service.get_all_users_tasks()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_task_entity(self, task):
        """Alustaa kuvauksen yksittäiselle tehtävälle.

        Args:
            task: Lista tehtävän tiedoista.
        """

        title = task[0]
        course = task[1]
        deadline = task[2]
        state = task[3]

        title_label = ttk.Label(
            master=self._frame,
            text=f"{title}",
            font=font.Font(weight='bold')
        )

        if state == 1:
            state = "Not done"
        else:
            state = "Done"

        info_label = ttk.Label(
            master=self._frame,
            text=f"Course: {course}\nDeadline: {deadline}\nCurrent state: {state}\n"
        )

        title_label.grid(padx=5, pady=5, sticky=constants.W)
        info_label.grid(padx=5, pady=5, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        navigation = Navigation(self._frame, self._previous_view, self._logout)
        navigation.initialize(1)

        label = ttk.Label(
            master=self._frame,
            text=f"All your tasks",
            font=font.Font(weight='bold')
        )

        label.grid(padx=5, pady=5, sticky=constants.W)

        for task in self._tasks:
            self._initialize_task_entity(task)

        if len(self._tasks) < 1:
            no_tasks = ttk.Label(
                master=self._frame,
                text="You don't have any tasks.\nCreate tasks to make them appear here!",
                justify="center"
            )

            no_tasks.grid(row=3, padx=5, pady=5, sticky=constants.N)
