from tkinter import ttk, constants, StringVar
from services.study_app_services import study_app_service


class CourseView:
    def __init__(self, root, show_all_courses_view):
        self._root = root
        self._frame = None
        self._show_all_courses_view = show_all_courses_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text=f"{study_app_service.get_current_course()}"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(row=0, sticky=constants.W)
