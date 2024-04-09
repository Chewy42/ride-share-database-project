from random import randint

class helper():
    # function checks for user input given a list of choices
    @staticmethod
    def get_choice(lst):
        choice = input("Enter choice number: ")

        while choice.isnumeric() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")
            
        return int(choice)
    
    @staticmethod
    def print_result(lst):
        print("Results..\n")
        for i in lst:
            print(i)
        print("")

    @staticmethod
    def generate_id():
        return str(randint(1000000000000000000000, 9999999999999999999999))