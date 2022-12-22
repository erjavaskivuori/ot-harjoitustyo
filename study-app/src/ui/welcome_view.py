from tkinter import ttk, constants
import ui.styles as s


class WelcomeView:
    """Sovelluksen aloitusnäkymästä vastaava luokka."""

    def __init__(self, root, show_login, show_register):
        """Luoka kontstruktori. Luo uuden aloitusnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            show_login: 
                Kutsuttava arvo, jota kutsutaan kun siirrytään kirjautumisnäkymään.
            show_register:
                Kutsuttava arvo, jota kutsutaan kun siirrytään rekisteröitymisnäkymään.
        """

        self._root = root
        self._frame = None
        self._show_login = show_login
        self._show_register = show_register

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(
            master=self._frame,
            text="Welcome to Study-app!",
            font=s.headers()
        )

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
