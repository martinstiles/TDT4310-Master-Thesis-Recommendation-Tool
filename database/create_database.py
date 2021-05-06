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
    database_file = r".\database\viewership.db"

    dataset_file = r".\dataset\Datasett_seertall_NRK_2018.csv"

    # Parse file and make rows
    p = Parser(dataset_file)
    p.parse_file()

    sql_create_viewings_table = """ CREATE TABLE IF NOT EXISTS Viewings(
                                        id INTEGER PRIMARY KEY,
                                        series_id TEXT NOT NULL,
                                        date DATE NOT NULL,
                                        screen TEXT,
                                        views INTEGER NOT NULL,
                                        weekday TEXT NOT NULL
                                    ); """

    conn = create_connection(database_file)

    with conn:
        # create viewings table
        create_table(conn, sql_create_viewings_table)

        # add all rows of viewings
        create_viewings(conn, p.rows)
