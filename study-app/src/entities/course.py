from entities.user import User


class Course:
    """Luokka, joka kuvaa yksittäistä kurssia.

    Attributes:
        course_id: Kokonaislukuarvo, joka kuvaa kurssin id:tä.
        owner: User-olio, joka kuvaa kurssin omistajaa.
        name: Merkkijonoarvo, joka kuvaa kurssin nimeä.
        visibility: Kokonaislukuarvo, joka kertoo, onko kurssi jo suroitettu.
    """

    def __init__(self, course_id: int, owner: User, name: str, visibility: int):
        """Luokan konstruktori, joka luo Course-olion.

        Args:
            course_id: Kokonaislukuarvo, joka kuvaa kurssin id:tä.
            owner: User-olio, joka kuvaa kurssin omistajaa.
            name: Merkkijonoarvo, joka kuvaa kurssin nimeä.
            visibility: Kokonaislukuarvo, joka kertoo, onko kurssi jo suroitettu.
        """

        self.id = course_id
        self.owner = owner
        self.name = name
        self.visibility = visibility
        self.tasks = []
