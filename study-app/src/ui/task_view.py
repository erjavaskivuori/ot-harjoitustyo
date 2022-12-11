import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, constants, StringVar
from services.study_app_services import study_app_service


class CreateTaskView:
    def __init__(self, root, show_course_view):
        self._root = root
        self._frame = None
        self._show_course_view = show_course_view
        self._title_entry = None
        self._description_entry = None
        self._deadline_entry = None
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _title_field(self):
        title_label = ttk.Label(
            master=self._frame,
            text="Title"
        )
        self._title_entry = ttk.Entry(master=self._frame)

        title_label.grid(padx=5, pady=5, sticky=constants.W)
        self._title_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _description_field(self):
        title_label = ttk.Label(
            master=self._frame,
            text="Description (optional)"
        )
        self._description_entry = tk.Text(master=self._frame, height=4)

        title_label.grid(padx=5, pady=5, sticky=constants.W)
        self._description_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _deadline_field(self):
        label = ttk.Label(
            master=self._frame,
            text="Select due date"
        )

        self._deadline_entry=DateEntry(
            master=self._frame, 
            selectmode="day",
            textvariable=StringVar()
        )

        label.grid(sticky=constants.W)
        self._deadline_entry.grid(sticky=constants.W)

    def _create_task_handler(self):
        title = self._title_entry.get()
        description = self._description_entry.get("1.0", 'end-1c')
        deadline = self._deadline_entry.get_date()

        if title == "":
            self._show_error("Title must have at least one character")
        if len(title) > 30:
            self._show_error("Title is too long")

        study_app_service.add_task(title, description, deadline)
        self._show_course_view()

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
            text="Create new task"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(row=0, sticky=constants.W)

        self._title_field()

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        self._description_field()
        self._deadline_field()

        add_task_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._create_task_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._show_course_view
        )

        add_task_button.grid(padx=5, pady=5, sticky=constants.S)
        return_button.grid(padx=5, pady=5, sticky=constants.W)

        self._hide_error()

class TaskView:
    def __init__(self, root, show_course_view):
        self._root = root
        self.show_course_view = show_course_view
        self._task = study_app_service.get_current_task()
        self._task_state = self._task.state
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title = ttk.Label(
            master=self._frame,
            text=f"{self._task.title}"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

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
                self.show_course_view()
            ]
        )

        set_undone = ttk.Button(
            master=self._frame,
            text="Return task to TO-DO-list",
            command=lambda: [
                study_app_service.change_task_state(self._task, 1),
                self.show_course_view()
            ]
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self.show_course_view
        )

        title.grid(row=0, padx=5, pady=5, sticky=constants.W)
        description.grid(row=2, padx=5, pady=5, sticky=constants.W)
        deadline.grid(row=8, padx=5, pady=5, sticky=constants.W)

        if self._task.state == 1:
            set_done.grid(row=10, padx=5, pady=5, sticky=constants.W)
        if self._task.state == 0:
            set_undone.grid(row=10, padx=5, pady=5, sticky=constants.W)

        return_button.grid(row=12, padx=5, pady=5, sticky=constants.W)