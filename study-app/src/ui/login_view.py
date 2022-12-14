from tkinter import ttk, constants, StringVar, font
from services.study_app_service import study_app_service, InvalidCredentialsError


class LoginView:
    """Kirjautumisnäkymästä vastaava luokka."""

    def __init__(self, root, login, previous_view):
        """Luokan kontruktori. Luo uuden kirjautumisnäkymän.

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan.
            login: Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu sisään.
            previous_view: 
                Kutsuttava arvo, jota kutsutaan, kun palataan aloitusnäkymään.
        """

        self._root = root
        self._login = login
        self._previous_view = previous_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _username_field(self):
        """Alustaa kentän, johon annetaan käyttäjänimi."""

        username_label = ttk.Label(
            master=self._frame,
            text="Username"
        )
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _password_field(self):
        """Alustaa kentän, johon annetaan salasana"""

        password_label = ttk.Label(
            master=self._frame,
            text="Password"
        )
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _login_handler(self):
        """Vastaa käyttäjän kirjaamisesta sisään."""

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            study_app_service.login(username, password)
            self._login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, error):
        if self._error != None:
            self._error.set(error)
            self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label = ttk.Label(
            master=self._frame,
            text="Login",
            font=font.Font(weight='bold')
        )

        label.grid(padx=5, pady=5, sticky=constants.N)

        self._username_field()
        self._password_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._previous_view
        )

        self._error_label.grid(padx=5, pady=5)
        login_button.grid(padx=10, pady=10, sticky=constants.EW)
        return_button.grid(padx=10, pady=10, sticky=constants.S)

        self._hide_error()
