from connector import *
from dataset_parser import Parser


def create_table(conn, create_table_sql):
    """
    Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def create_viewings(conn, viewings):
    """
    Create a new viewing into the viewings table
    :param conn: Connection object
    :param viewing: a viewing to be inserted (tuple of values)
    :return: viewing id
    """
    sql = ''' INSERT INTO Viewings(series_id, date, screen, views, weekday)
              VALUES(?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.executemany(sql, viewings)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":

    # ONLY FOR CREATING DATABASE, SHOULD NOT BE RUN

    database_file = ""
    database_file_windows = r"C:\Users\magnu\TDT4310-final-project\database\thesis_database.db"
    database_file_unix = r"../../database/thesis_database.db"

    # dataset_file = r".\dataset\Datasett_seertall_NRK_2018.csv"

    # Parse file and make rows
    # p = Parser(dataset_file)
    # p.parse_file()

sql_create_supervisor_table = """ CREATE TABLE IF NOT EXISTS Supervisor(
                                        supervisor_id INTEGER PRIMARY KEY,
                                        supervisor_name TEXT(100) NOT NULL
                                    ); """

sql_create_assigned_status_table = """ CREATE TABLE IF NOT EXISTS Assigned_status(
                                        assigned_status INTEGER PRIMARY KEY,
                                        assigned_status_name TEXT(100) NOT NULL
                                    ); """

sql_create_number_of_students_table = """ CREATE TABLE IF NOT EXISTS Number_of_students(
                                        num_students INTEGER PRIMARY KEY,
                                        num_students_name TEXT(100) NOT NULL
                                    ); """

sql_create_specialization_table = """ CREATE TABLE IF NOT EXISTS Specialization(
                                        specialization_id INTEGER PRIMARY KEY,
                                        specialization_name TEXT(100) NOT NULL
                                    ); """

sql_create_thesis_table = """ CREATE TABLE IF NOT EXISTS Thesis(
                                        thesis_id INTEGER PRIMARY KEY,
                                        thesis_name TEXT(200) NOT NULL,
                                        supervisor_id INTEGER NOT NULL,
                                        assigned_status INTEGER NOT NULL,
                                        num_students INTEGER NOT NULL,
                                        url TEXT(100) NOT NULL,
                                        description TEXT(10000) NOT NULL,
                                        FOREIGN KEY (supervisor_id) 
                                            REFERENCES Supervisor(supervisor_id) 
                                                ON DELETE NO ACTION
                                                ON UPDATE CASCADE,
                                        FOREIGN KEY (assigned_status) 
                                            REFERENCES Assigned_status(assigned_status) 
                                                ON DELETE NO ACTION
                                                ON UPDATE NO ACTION,
                                        FOREIGN KEY (num_students) 
                                            REFERENCES Number_of_students(num_students) 
                                                ON DELETE NO ACTION
                                                ON UPDATE NO ACTION
                                    ); """

sql_create_thesis_specializations_table = """ CREATE TABLE IF NOT EXISTS Thesis_specializations(
                                        thesis_id INTEGER,
                                        specialization_id INTEGER,
                                        PRIMARY KEY (thesis_id, specialization_id),
                                        FOREIGN KEY (thesis_id)
                                            REFERENCES Thesis(thesis_id)
                                                ON DELETE CASCADE
                                                ON UPDATE CASCADE,
                                        FOREIGN KEY (specialization_id)
                                            REFERENCES Specialization(specialization_id)
                                                ON DELETE CASCADE
                                                ON UPDATE CASCADE 
                                    ); """
# CHOOSE THE APPROPIATE FILE
is_windows = True
if is_windows:
    conn = create_connection(database_file_windows)
else:
    conn = create_connection(database_file_unix)
#conn = create_connection()

with conn:
    # Create Supervisor table
    create_table(conn, sql_create_supervisor_table)

    # Create Specialization table
    create_table(conn, sql_create_specialization_table)

    # Create Assigned_status and Number_of_students tables
    # as enumerators for Thesis table values
    create_table(conn, sql_create_assigned_status_table)
    create_table(conn, sql_create_number_of_students_table)

    # Create (main) Thesis table
    create_table(conn, sql_create_thesis_table)

    # Create Thesis_specializations table for N-N mappings
    # of theses and related specializations
    create_table(conn, sql_create_thesis_specializations_table)

    # # add all rows of viewings
    # create_viewings(conn, p.rows)
