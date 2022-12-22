from tkinter import Tk, ttk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Study-app")

    style = ttk.Style()
    window.tk.call('source', 'src/theme/ttk-Breeze-0.6/breeze.tcl')
    style.theme_use("Breeze")

    user_interface = UI(window)
    user_interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()
