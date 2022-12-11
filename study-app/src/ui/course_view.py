from tkinter import ttk, constants, messagebox
from datetime import date
from services.study_app_services import study_app_service


class CourseView:
    def __init__(self, root, show_all_courses_view, show_create_task_view, show_task_view):
        self._root = root
        self._frame = None
        self._show_all_courses_view = show_all_courses_view
        self._show_create_task_view = show_create_task_view
        self._show_task_view = show_task_view
        self._course = study_app_service.get_current_course()
        self._course.tasks = study_app_service.get_tasks_by_course(
            self._course)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_task_entity(self, task):

        task_button = ttk.Button(
            master=self._frame,
            text=f"{task.title}",
            command=lambda: [study_app_service.set_current_task(
                task), self._show_task_view()]
        )

        task_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_remove_course_popup(self):

        msg_box = messagebox.askyesno(
            title="Remove course",
            message=f"Are you sure you want to remove {self._course.name} from your courses?",
        )

        if msg_box == True:
            study_app_service.remove_course(self._course)
            self._show_all_courses_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text=f"{self._course.name}"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(row=0, padx=5, pady=5, sticky=constants.W)

        current_date = date.today()

        date_label = ttk.Label(
            master=self._frame,
            text=current_date
        )

        date_label.grid(row=0, padx=5, pady=5, sticky=constants.E)

        add_task_button = ttk.Button(
            master=self._frame,
            text="Add task",
            command=self._show_create_task_view
        )

        add_task_button.grid(sticky=constants.N)

        todo_label = ttk.Label(
            master=self._frame,
            text="TO-DO:"
        )

        todo_label.grid(padx=5, pady=5, sticky=constants.W)

        for task in self._course.tasks:
            if task.state == 1:
                self._initialize_task_entity(task)

        done_label = ttk.Label(
            master=self._frame,
            text="\nCompleted tasks:"
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

        remove_button.grid(padx=5, pady=5, sticky=constants.E)

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._show_all_courses_view
        )

        return_button.grid(padx=5, pady=5, sticky=constants.W)
