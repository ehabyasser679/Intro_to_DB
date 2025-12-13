import mysql.connector
from mysql.connector import errorcode
import getpass

HOST = "localhost"
USER = "root"

DATABASE = "alx_book_store"

def create_database():
    PASSWORD = getpass.getpass ("Enter password: ")
    conncetion = None
    cursor = None
    
    try:
        print (f"\nConnecting to MySQL server at {HOST} as user {USER}")
        connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD
        )

        cursor = connection.cursor()

        sql_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE}"

        cursor.execute(sql_query)

        print (f"\nDatabase '{DATABASE}' created successfully")

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print (f"\nError {error.errno}: {error.msg}")
            print (f"\nYou don't have the necessary permissions to create a database: {error}")
        
        elif error.errno == errorcode.CR_CONNECTION_ERROR:
            print (f"\nError {error.errno}:{error.msg}")
            print (f"\nFailed to connect to MySQL server: {error}")
       
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print (f"\nError {error.errno}: {error.msg}")
            print (f"\nDatabase does not exist: {error}")
        
        else:
            print (f"\n Error {error.errno}: {error.msg}")
            print (f"\n an unexpected error occurred during execution: {error}")
    except Exception as error:
        print (f"\n a genral error occurred during execution: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print ("\nConnection to MySQL server closed successfully")
if __name__ == "__main__":
    create_database()
    
