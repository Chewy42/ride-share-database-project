from time import sleep as delay
from db_operations import db_operations
from helper import helper
from bcrypt import hashpw, gensalt


class Swift():
    def __init__(self):
        self.db_ops = db_operations()
        self.initial_screen()
        self.login()
        pass

    def initial_screen(self):
        print("-----------------------")
        print("         Swift")
        print("A ride sharing service.")
        print("-----------------------")
        delay(2)

    def login(self):
        print("     Are you a:        ")
        print("      1. New User      ")
        print("      2. Rider         ")
        print("      3. Driver        ")
        print("-----------------------")
        choice = helper.get_choice([1, 2, 3])

        if choice == 1:
            self.new_user()
        elif choice == 2:
            print("Rider")
        else:
            print("Driver")

    def new_user(self):
        print("-----------------------")
        print(" New User Registration ")
        delay(1)
        print("")
        name = input("Enter your full name: ")
        username = input("Enter your username: ")   
        password = input("Enter your password: ")

        user_id = helper.generate_id()

        query = f'''
        INSERT INTO users(user_id, full_name, username, password)
        VALUES('{user_id}', '{name}', '{username}', '{hashed_password.decode('utf-8')}');
        '''

        self.db_ops.modify_query(query)

        print("User created successfully.")


        
        



    def rider(self):
        print("Rider")

    def driver(self):
        print("Driver")

    
        
if __name__ == "__main__":
    swift = Swift()