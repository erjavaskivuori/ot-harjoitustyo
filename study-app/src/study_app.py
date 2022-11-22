#intention is to build graphic ui later

from database_connection import form_database_connection
from services.study_app_services import StudyAppServices

commands = {
    "q" : "q quit",
    "1" : "1 login",
    "2" : "2 create new user",
    "3" : "3 logout"
}

class StudyApp:
    def __init__(self):
        self._setup = StudyAppServices()

    def start(self):
        print("Welcome to Study-app")
        print("Commands:")
        for command in commands.values():
            print(command)

        while True:
            given_command = input("Give command: ")

            if not given_command in commands:
                print("Command not found")
                print("Commands:")
                for command in commands.values():
                    print(command)
                    continue

            if given_command == "q":
                break
            elif given_command == "1":
                username = input("Username: ")
                password = input("Password: ")
                self._setup.login(username, password)
                print(f"Your are now logged in as {username}")
            elif given_command == "2":
                username = input("Username: ")
                password = input("Password: ")
                self._setup.create_user(username, password)
                print(f"Your are now logged in as {username}")
            elif given_command == "3":
                try:
                    self._setup.logout()
                    print("You have logged out")
                except:
                    "No one has logged in"
            

if __name__ == "__main__":
    form_database_connection()
    app = StudyApp()
    while True:
        app.start()
