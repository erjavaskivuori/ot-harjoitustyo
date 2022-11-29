from tkinter import ttk, constants, StringVar
from services.study_app_services import study_app_service

class AllCoursesView:
    def __init__(self, root, show_welcome_view, show_course_view):
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
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        study_app_service.logout()
        self._show_welcome_view()

    def _create_course_field(self):
        create_label = ttk.Label(
            master=self._frame,
            text="Create new course"
        )

        self._course_name_entry = ttk.Entry(master=self._frame)

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_course_handler()
        )

        create_label.grid(row=2, column=0, sticky=constants.W)
        self._course_name_entry.grid(row=3, padx=5, pady=5, sticky=constants.EW)
        create_button.grid(row=3, sticky=constants.E)

    def _create_course_handler(self):
        
        name = self._course_name_entry.get()

        if name == "":
            self._show_error("Give at least one character")
        else:
            study_app_service.create_course(name)
            self._show_course_view()

    def _initialize_course_entity(self, course):
        
        course_button = ttk.Button(
            master=self._frame,
            text=f"{course}",
            command=self._show_course_view
        )

        course_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _show_error(self, error):
        if self._error != None:
            self._error.set(error)
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame, 
            text=f"Welcome {self._user}"
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(row=0, sticky=constants.W)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._show_welcome_view
        )

        logout_button.grid(row=0, sticky=constants.E)
    
        self._create_course_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        if self._courses != None:
            for course in self._courses:
                self._initialize_course_entity(course)

        self._hide_error()

        