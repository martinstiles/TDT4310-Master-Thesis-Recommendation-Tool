import sqlite3
from sqlite3 import Error


def create_connection(db_file=""):
    """
    # Create a database connection to a SQLite database.
    If no file string is provided, the connection is made to an
    in-memory database. 
    :param db_file: database file string (optional)
    :return: Connection object or None
    """
    conn = None
    try:
        if db_file == "":
            conn = sqlite3.connect(':memory:')
        else:
            conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


# create_connection()
