from tkinter import ttk, constants, StringVar
from services.study_app_services import study_app_service, UsernameExistsError


class RegisterView:
    """Rekisteröitymisnäkymästä vastaava luokka."""
    
    def __init__(self, root, register, show_welcome_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan.
            register: 
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä rekisteröidään
                ja kirjataan sisään sovellukseen.
            show_welcome_view:
                Kutsuttava arvo, jota kutsutaan, kun palataan aloitusnäkymään.
        """

        self._root = root
        self._register = register
        self._show_welcome_view = show_welcome_view
        self._frame = None
        self._username_entry = None
        self._password_entry1 = None
        self._password_entry2 = None
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
        """Alustaa kentät, joihin salasana annetaan."""

        password_label = ttk.Label(
            master=self._frame,
            text="Password"
        )

        password_again_label = ttk.Label(
            master=self._frame,
            text="Repeat password"
        )

        self._password_entry1 = ttk.Entry(master=self._frame, show="*")
        self._password_entry2 = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry1.grid(padx=5, pady=5, sticky=constants.EW)
        password_again_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry2.grid(padx=5, pady=5, sticky=constants.EW)

    def _registeration_handler(self):
        """Vastaa käyttäjän rekisteröimisestä sovellukseen."""

        username = self._username_entry.get()
        password1 = self._password_entry1.get()
        password2 = self._password_entry2.get()

        if username == "" or password1 == "" or password2 == "":
            self._show_error("Fill all the fields")

        if password1 != password2:
            self._show_error("Passwords don't match")

        if len(password1) < 6:
            self._show_error("Password must have at least 6 characters")

        try:
            study_app_service.create_user(username, password1)
            self._register()
        except UsernameExistsError:
            self._show_error(f"Usename {username} is taken")

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
            text="Register")

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        label.grid(columnspan=2, padx=5, pady=5, sticky=constants.N)

        self._username_field()
        self._password_field()

        self._error = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error,
            foreground="red"
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._registeration_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._show_welcome_view
        )

        label.grid(padx=5, pady=5, sticky=constants.EW)
        self._error_label.grid(padx=5, pady=5)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)
        return_button.grid(padx=5, pady=5, sticky=constants.S)

        self._hide_error()
