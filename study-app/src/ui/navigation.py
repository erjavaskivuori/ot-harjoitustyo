from datetime import date
from tkinter import ttk, constants, messagebox
from PIL import Image, ImageTk
from services.study_app_service import study_app_service


class Navigation():
    def __init__(self, frame, previous_view, logout):
        """Luokan konstruktori. Luo uuden navigaation.

        Args:
            frame: Ikkuna, jonka sisään navigaatio sijoitetaan.
            previous_view :
                Kutsuttava arvo, jota kutsutaan, kun palataan edelliseen näkymään.
            logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
        """

        self._frame = frame
        self._previous_view = previous_view
        self._logout = logout

        photo = Image.open("src/ui/arrow.png")
        photo = photo.resize((14, 14), Image.ANTIALIAS)
        self._img = ImageTk.PhotoImage(photo)

    def _initialize_logout_popup(self):
        """Alustaa viesti-ikkunan käyttäjän uloskirjautumiselle.
        """

        msg_box = messagebox.askyesno(
            title="Logout",
            message=f"Do you want to log out?",
        )

        if msg_box == True:
            study_app_service.logout()
            self._logout()

    def _initialize_return_button(self, view):

        return_button = ttk.Button(
            master=self._frame,
            image=self._img,
            style="Custom.TButton",
            command=lambda: [self._frame.destroy(), view()]
        )

        return_button.grid(row=0, sticky=constants.NW)

    def initialize(self, value):
        ttk.Style().configure("Custom.TButton", font="Helvetica 10")

        today = date.today().strftime("%d.%m.%Y")

        date_label = ttk.Label(
            master=self._frame,
            text=f"{today}",
            style="Custom.TButton",
            font="Helvetica 10",
            width=30
        )

        date_label.grid(row=0, sticky=constants.EW)

        if value == 1:
            self._initialize_return_button(self._previous_view)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._initialize_logout_popup,
            style="Custom.TButton"
        )

        logout_button.grid(row=0, sticky=constants.NE)
