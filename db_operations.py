import mysql.connector
from helper import helper

class db_operations():
    # constructor with connection path to DB
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost",
            user="root",
            password="password",
            auth_plugin='mysql_native_password')
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS RideShare")
        self.connection.database = "RideShare"
        self.create_all_tables()
        self.cursor = self.connection.cursor()

    # function to simply execute a DDL or DML query.
    # commits query, returns no results. 
    # best used for insert/update/delete queries with no parameters
    def modify_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # function to simply execute a DDL or DML query with parameters
    # commits query, returns no results. 
    # best used for insert/update/delete queries with named placeholders
    def modify_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    # function to simply execute a DQL query
    # does not commit, returns results
    # best used for select queries with no parameters
    def select_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    # function to simply execute a DQL query with parameters
    # does not commit, returns results
    # best used for select queries with named placeholders
    def select_query_params(self, query, dictionary):
        result = self.cursor.execute(query, dictionary)
        return result.fetchall()

    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with no parameters
    def single_record(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall() 
        return result[0][0] if result else None
    
    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with named placeholders
    def single_record_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchone()[0]
    
    # function to return all attributes for all records 
    # from some table with named placeholders
    def all_attributes_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        results = self.cursor.fetchall()
        return results[0]
    
    def multiple_records(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with no parameters
    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        if None in results:
            results.remove(None)
        return results
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with named placeholders
    def single_attribute_params(self, query, dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results

    def create_all_tables(self):
        # Check if the table 'users' exists, if not, create it
        self.cursor.execute("SHOW TABLES LIKE 'USER'")
        result = self.cursor.fetchone()
        if result is None:
            self.create_users_table()

        # Check if the table 'drivers' exists, if not, create it
        self.cursor.execute("SHOW TABLES LIKE 'DRIVER'")
        result = self.cursor.fetchone()
        if result is None:
            self.create_drivers_table()

        # Check if the table 'trip_log' exists, if not, create it
        self.cursor.execute("SHOW TABLES LIKE 'TRIPLOGS'")
        result = self.cursor.fetchone()
        if result is None:
            self.create_trip_log_table()
    
    # function that creates table songs in our database
    def create_users_table(self):
        query = '''
        CREATE TABLE USER (
            user_id INT PRIMARY KEY,
            email VARCHAR(100) UNIQUE NOT NULL,
            full_name VARCHAR(100) NOT NULL,
            is_driver BOOLEAN
        );
        '''
        self.cursor.execute(query)
        print('Table Created')

    def create_drivers_table(self):
        query = '''
        CREATE TABLE DRIVER (
            user_id INT NOT NULL,
            rating INT NOT NULL DEFAULT 0,
            driver_mode BOOLEAN DEFAULT FALSE,
            CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES USER(user_id)
        );'''
        self.cursor.execute(query)
        print('Driver Table Created')

    def create_trip_log_table(self):
        query = '''
        CREATE TABLE TRIPLOGS (
            trip_id INT NOT NULL,
            driver_id INT NOT NULL,
            rider_id INT NOT NULL,
            pickup_address VARCHAR(255) NOT NULL,
            dropoff_address VARCHAR(255) NOT NULL,
            CONSTRAINT driver_id FOREIGN KEY (driver_id) REFERENCES USER (user_id),
            CONSTRAINT rider_id FOREIGN KEY (rider_id) REFERENCES USER (user_id)
        );
        '''
        self.cursor.execute(query)
        print('Trip Log Table Created')

    # destructor that closes connection with DB
    def destructor(self):
        self.cursor.close()
        self.connection.close()