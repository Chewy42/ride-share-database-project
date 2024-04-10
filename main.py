from time import sleep as delay
from db_operations import db_operations
from helper import helper


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
        print("      2. Existing User ")
        print("-----------------------")
        choice = helper.get_choice([1, 2])

        if choice == 1:
            self.new_user()
        elif choice == 2:
            self.existing_user()
        else:
            print("Driver")

    def new_user(self):
        print("-----------------------")
        print(" New User Registration ")
        delay(1)
        print("")
        email = input("Enter your email address: ") 
        name = input("Enter your full name: ") 

        user_id = str(int(self.db_ops.single_record("SELECT COUNT(*) FROM USER")) + 1)

        query = f'''
        INSERT INTO USER (user_id, email, full_name)
        VALUES('{user_id}', '{email}', '{name}');
        '''

        self.db_ops.modify_query(query)

        print(f"\n-- User created successfully! Welcome {str(name)} --\n")
        rider_has_profile = False
        while True:
            print("--------------------------------------")
            print("     Would you like to setup a:      ")
            print("      1. Driver Profile               ")
            print("      2. Continue as Rider            ")
            print("      3. Not Now                      ")
            print("--------------------------------------")
            choice = helper.get_choice([1, 2, 3])
            if(choice == 1):
                self.driver(user_id)
            elif(choice == 2):
                self.menu(user_id)
            elif(choice == 3):
                self.menu(user_id)

    def existing_user(self):
        print("-----------------------")
        print(" Existing User Login  ")
        delay(1)
        print("")
        email = input("Enter your email: ") 

        user_id = self.db_ops.single_record(f"SELECT user_id FROM USER WHERE email = '{email}'")

        name = self.db_ops.single_record(f"SELECT full_name FROM USER WHERE email = '{email}'")

        print(f"\n-- Welcome {str(name)} --\n")
        has_driver_profile = self.check_if_driver_profile_exists(user_id)
        if has_driver_profile:
            driver_mode = self.get_driving_mode(user_id)
            print(f"  Rank(s): Rider, Driver")
            print("  Driver Mode: ENABLED" if driver_mode else "  Driver Mode: DISABLED")
        else:
            print(f"  Rank(s): Rider")
        print("-----------------------------")
        self.menu(user_id)

    def driver(self, user_id):
        driver_id = str(int(self.db_ops.single_record("SELECT COUNT(*) FROM DRIVER")) + 1)

        query = f'''
        INSERT INTO DRIVER (user_id)
        VALUES('{driver_id}');
        '''

        self.db_ops.modify_query(query)

        print(f"\n-- Driver profile created successfully! --")
        print(f"          Driver ID: {driver_id}")
        print("----------------------------------------------")
    
    def menu(self, user_id):
        while True:
            has_driver_profile = self.check_if_driver_profile_exists(user_id)
            print("\n     What would you like to do?     ")
            print("      1. Book a Ride                 ")
            print("      2. View Rides                  ")
            print("      3. View Profile                ")
            if(not has_driver_profile):
                print("      4. Register as a Driver")
                print("      5. Logout")
            else:
                driving_mode = self.get_driving_mode(user_id)
                print(f"      4. Toggle Driving Mode: {'ENABLED' if driving_mode else 'DISABLED'}")
                print("      5. Logout                      ")
            print("--------------------------------------")
            choice = helper.get_choice([1, 2, 3, 4, 5])
            if(choice == 1):
                self.book_ride(user_id)
            elif(choice == 2):
                self.view_rides(user_id)
            elif(choice == 3):
                self.view_profile(user_id)
            elif(not has_driver_profile and choice == 4):
                self.driver(user_id)
            elif(has_driver_profile and choice == 4):
                driving_mode = self.get_driving_mode(user_id)
                self.toggle_driving_mode(user_id, ("1" if not driving_mode else "0"))
            else:
                print("Logging out...")
                break

    def check_if_driver_profile_exists(self, user_id):
        return self.db_ops.single_record(f"SELECT COUNT(*) FROM DRIVER WHERE user_id = '{user_id}'")
    
    def book_ride(self, user_id):

        pickup_address = input("Enter your pickup address: ")
        dropoff_address = input("Enter your dropoff address: ")

        trip_id = str(int(self.db_ops.single_record("SELECT COUNT(*) FROM TRIPLOGS")) + 1)
        driver_id = self.db_ops.single_record(f"SELECT user_id FROM DRIVER WHERE driver_mode = 1")

        if driver_id:
            rider_id = user_id

            query = f'''
            INSERT INTO TRIPLOGS (trip_id, driver_id, rider_id, pickup_address, dropoff_address)
            VALUES('{trip_id}', '{driver_id}', '{rider_id}', '{pickup_address}', '{dropoff_address}');
            '''

            self.db_ops.modify_query(query)

            print(f"\n-- Ride booked successfully! --")
            print(f"          Trip ID: {trip_id}")
            print("----------------------------------------------")

            delay(2)

            self.give_rating(driver_id)
        else:
            print("\n-- No drivers available at the moment. --")
            print("----------------------------------------------")

    def give_rating(self, driver_id):
        print("\n-----------------------")
        print("       Rate Driver      ")
        rating = int(input("Enter a rating between 1 and 5: "))

        query = f'''
        SELECT rating
        FROM DRIVER
        WHERE user_id = '{driver_id}';
        '''
        result = self.db_ops.select_query(query)
        current_rating = result[0][0] if result else 0

        if current_rating == 0:
            new_rating = rating
        else:
            new_rating = (current_rating + rating) / 2

        query = f'''
        UPDATE DRIVER
        SET rating = '{new_rating}'
        WHERE user_id = '{driver_id}';
        '''

        self.db_ops.modify_query(query)

        print("\n-- Rating submitted successfully! --")
            
    
    def view_rides(self, user_id):
        print("\n-----------------------")
        print("       Your Rides      ")
        rides = self.db_ops.multiple_records(f"SELECT * FROM TRIPLOGS WHERE rider_id = '{user_id}'")
        if rides:
            for ride in rides:
                print(f"Trip ID: {ride[0]}")
                print(f"Driver ID: {ride[1]}")
                print(f"Pickup Address: {ride[3]}")
                print(f"Dropoff Address: {ride[4]}")
                print(f"Role: {'Rider' if ride[1] == user_id else 'Driver'}")
                print("-----------------------")
        else:
            print("    No rides found.")

    def view_profile(self, user_id):
        print("\n-----------------------")
        print("       Profile         ")
        name = self.db_ops.single_record(f"SELECT full_name FROM USER WHERE user_id = '{user_id}'")
        print("Name: ", name)
        has_driver_profile = self.check_if_driver_profile_exists(user_id)
        if has_driver_profile:
            driver_mode = self.get_driving_mode(user_id)
            print("Rank(s): Rider, Driver")
            print("Driver Mode: ENABLED" if driver_mode else "Driver Mode: DISABLED")
            rating = self.db_ops.single_record(f"SELECT rating FROM DRIVER WHERE user_id = '{user_id}'")
            print(f"Rating: {rating}")
        else:
            print("Rank(s): Rider")
        print("-----------------------")

    def get_driving_mode(self, user_id):
        driver_mode = self.db_ops.single_record(f"SELECT driver_mode FROM DRIVER WHERE user_id = '{user_id}'")
        return driver_mode if driver_mode else False
    
    def toggle_driving_mode(self, user_id, mode):
        query = f'''
        UPDATE DRIVER
        SET driver_mode = '{mode}'
        WHERE user_id = '{user_id}';
        '''

        self.db_ops.modify_query(query)
        
if __name__ == "__main__":
    swift = Swift()