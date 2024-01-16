# database table for user in our database bank.db
import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
connection = sqlite3.connect('bank.db')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

try:
    # Create the 'Login' table if it doesn't exist
    # create_table_query = '''
    # CREATE TABLE IF NOT EXISTS Login (
    #     s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    #     Email TEXT NOT NULL,
    #     pass TEXT NOT NULL,
    #     Phone no INTEGER  NOT NULL
    # )
    # '''

    # create_table_query = '''
    #     CREATE TABLE IF NOT EXISTS create_account (
    #         s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    #         Fname TEXT NOT NULL,
    #         Lname TEXT NOT NULL,
    #         Email TEXT  NOT NULL,
    #         PhoneNo INTEGER  NOT NULL,
    #         DateOfBirth DATE NOT NULL,
    #         AccountNo INTEGER NOT NULL,
    #         Balance INTEGER NOT NULL,
    #         AccountType TEXT NOT NUll,
    #         Date DATE NOT NULL
    #     )
    #     '''

    # create_table_query = '''
    #         CREATE TABLE IF NOT EXISTS deposit (
    #             s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    #             AccountN INTEGER NOT NULL,
    #             credit INTEGER NOT NULL,
    #             date DATE  NOT NULL,
    #             Balancee INTEGER  NOT NULL,
    #             FOREIGN KEY (Balancee) REFERENCES create_account(Balance)
    #
    #         )
    #         '''

    # create_table_query = '''
    #             CREATE TABLE IF NOT EXISTS withdraw (
    #                 s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 AccountN INTEGER NOT NULL,
    #                 debit INTEGER NOT NULL,
    #                 date DATE  NOT NULL,
    #                 Balancee INTEGER  NOT NULL,
    #                 FOREIGN KEY (Balancee) REFERENCES create_account(Balance)

    #             )
    #             '''

    # create_table_query = '''
    #                 CREATE TABLE IF NOT EXISTS Transfer (
    #                     s_no INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     sAccountN INTEGER NOT NULL,
    #                     oAccountN INTEGER NOT NULL,
    #                     Balancee INTEGER  NOT NULL,
    #                     amount INTEGER NOT NULL,
    #                     date DATE  NOT NULL,
    #                     ifsc_code TEXT NOT NULL,
    #                     FOREIGN KEY (Balancee) REFERENCES create_account(Balance)
    #                 )
    #                 '''

    create_table_query = '''
                        CREATE TABLE IF NOT EXISTS Historyy (
                            s_no INTEGER PRIMARY KEY AUTOINCREMENT,
                            Paid_to INTEGER NOT NULL,
                            amountt INTEGER  NOT NULL,
                            Received_from INTEGER NOT NULL,
                            amount INTEGER  NOT NULL,
                            date DATE  NOT NULL,
                            accountN INTEGER NOT NULL
                        )
                        '''



    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    print("Table created successfully")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
