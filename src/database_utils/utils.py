from tabulate import tabulate
import connector


def create_table(conn, create_table_sql):
    """
    Creates a table from the create_table_sql statement

    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_record(conn, table, values):
    """
    Inserts a single new record into the given table

    :param conn: Connection object
    :param table: the table to insert the record into
        (snake_case, with first letter Capitalized)
    :values: the values of the record to be inserted
        in each field of the table
    :return: record id
    """
    insert_statement = "INSERT INTO " + table + " VALUES("
    for value in values:
        insert_statement += "?,"
    insert_statement = insert_statement[:-1] + ")"
    cur = conn.cursor()
    cur.execute(insert_statement, values)
    conn.commit()
    return cur.lastrowid


def insert_records(conn, table, values):
    """
    Inserts multiple new records into the given table

    :param conn: Connection object
    :param table: the table to insert the record into
        (snake_case, with first letter Capitalized)
    :values: the list of records to be inserted
        in each row of the table
    :return: record id of the last record inserted
    """
    insert_statement = "INSERT INTO " + table + " VALUES("
    for value in values[0]:
        insert_statement += "?,"
    insert_statement = insert_statement[:-1] + ")"
    cur = conn.cursor()
    cur.executemany(insert_statement, iter(values))
    conn.commit()
    return cur.lastrowid


def select_all(conn, table, limit=-1):
    """
    Returns all rows in the table, with option to limit number of rows

    :param table: the table to retrieve values from
    :param limit: an optional number specifying row limit
    :return: Cursor object containing result 
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + table + " LIMIT ?", (limit,))
    print_table(cursor)
    return cursor


def print_table(cursor):
    """
    Prints result as formatted table

    :param cursor: Cursor object containing query result
    """
    rows = cursor.fetchall()
    headers = [cursor.description[i][0]
               for i in range(len(cursor.description))]
    print(tabulate(rows, headers=headers), "\n")
