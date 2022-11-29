from tkinter import ttk, constants


class WelcomeView:
    def __init__(self, root, show_login, show_register):
        self._root = root
        self._frame = None
        self._show_login = show_login
        self._show_register = show_register

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Welcome to Study-app!")

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._show_login
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._show_register
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(padx=5, pady=5, sticky=constants.N)
        login_button.grid(padx=5, pady=5, sticky=constants.N)
        register_button.grid(padx=5, pady=5, sticky=constants.N)
