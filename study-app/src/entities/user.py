class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        user_id: Kokonaislukuarvo, joka kuvaa käyttäjän id:tä.
        username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjänimeä.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
    """

    def __init__(self, user_id: int, username: str, password: str):
        """Luokan konstruktori, joka luo User-olion.

        Args:
            user_id: Kokonaislukuarvo, joka kuvaa käyttäjän id:tä.
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjänimeä.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        """

        self.id = user_id
        self.username = username
        self.password = password
