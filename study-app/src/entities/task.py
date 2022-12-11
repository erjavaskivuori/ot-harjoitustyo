from datetime import date
from entities.course import Course


class Task:
    """Luokka, joka kuvaa yksittäistä tehtävää.

    Attributes:
        task_id: Kokonaislukuarvo, joka kuvaa tehtävän id:tä.
        course: Course-olio, joka kuvaa kurssia, johon tehtävä kuuluu.
        title: Merkkijonoarvo, joka kuvaa tehtävän otsikkoa.
        description: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
        deadline: Päivämääräolio, joka kuvaa tehtävän määräpäivää.
        state: Kokonaislukuarvo, joka kertoo, onko tehtävä jo suoritettu.
    """

    def __init__(self, task_id: int, course: Course, title: str,
                 description: str, deadline: date, state: int):
        """Luokan konstruktori, joka luo Task-olion.

        Args:
            task_id: Kokonaislukuarvo, joka kuvaa tehtävän id:tä.
            course: Course-olio, joka kuvaa kurssia, johon tehtävä kuuluu.
            title: Merkkijonoarvo, joka kuvaa tehtävän otsikkoa.
            description: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
            deadline: Päivämääräolio, joka kuvaa tehtävän määräpäivää.
            state: Kokonaislukuarvo, joka kertoo, onko tehtävä jo suoritettu.
        """

        self.id = task_id
        self.course = course
        self.title = title
        self.description = description
        self.deadline = deadline
        self.state = state
