from os import path
import utils
import sql_statements


if __name__ == "__main__":

    # ONLY FOR CREATING DATABASE, SHOULD NOT BE RUN NORMALLY.

    # Choose between in-memory (runtime only) and disk-based (persistent) database
    conn = None
    is_on_disk = True
    if is_on_disk:
        conn = create_connection(r"database/thesis_database.db")
    else:
        conn = create_connection()

    # Connect to database and execute queries
    with conn:
        # # Create Supervisor table
        # create_table(conn, SQL_CREATE_SUPERVISOR_TABLE)

        # # Create Specialization table
        # create_table(conn, SQL_CREATE_SPECIALIZATION_TABLE)

        # # Create Assigned_status and Number_of_students tables
        # # as enumerators for Thesis table values
        # create_table(conn, SQL_CREATE_ASSIGNED_STATUS_TABLE)
        # create_table(conn, SQL_CREATE_NUMBER_OF_STUDENTS_TABLE)

        # # Create (main) Thesis table
        # create_table(conn, SQL_CREATE_THESIS_TABLE)

        # # Create Thesis_specializations table for N-N mappings
        # # of theses and related specializations
        # create_table(conn, SQL_CREATE_THESIS_SPECIALIZATIONS_TABLE)

        description = "To be creative, we need to produce something which is new, meaningful and has some sort of value. Computers are able to support humans in creative processes, but to also themselves be creative or to assess if an idea or a product is creative. A master thesis project on computational creativity can investigate any creative field matching the interests and backgrounds of the student or students (language, design, music, art, mathematics, computer programming, etc.), and concentrate on one or several aspects of computational creativity, such as the production, understanding or evaluation of creativity, or on computer systems that support human creativity. "

        # Add Supervisor rows
        # insert_record(conn, "Supervisor", (1, "Björn Gambäck"))
        # insert_record(conn, "Assigned_status", (0, "Valgbart"))
        # insert_record(conn, "Assigned_status", (1, "Tildelt"))
        # insert_record(conn, "Number_of_students", (0, "En student"))
        # insert_record(conn, "Number_of_students",
        #               (1, "Gruppe / En eller flere studenter"))
        # insert_record(conn, "Specialization", (0, "Programvaresystemer"))
        # insert_record(conn, "Thesis", (2014, "Computational Creativity", 1, 0, 1,
        #                                "https://www.idi.ntnu.no/education/oppgaveforslag.php?oid=2014", description))
        # insert_record(conn, "Thesis_specializations", (2014, 0))
        # select_all(conn, "Thesis")
        # select_all(conn, "Assigned_status")
        # select_all(conn, "Number_of_students")
        # select_all(conn, "Specialization")
        # select_all(conn, "Thesis_specializations")
        # insert_records(conn, "Supervisor", [
        #    (2, "Svein-Erik Brattsberg"), (3, "Norvald Ryeng")])
        # select_all(conn, "Supervisor")
        # cursor = conn.cursor()
        # cursor.execute("SELECT thesis_name, supervisor_name, assigned_status, num_students, specialization_name FROM "
        #                "Thesis NATURAL JOIN Supervisor "
        #                "NATURAL JOIN Assigned_status "
        #                "NATURAL JOIN Number_of_students "
        #                "NATURAL JOIN Thesis_specializations "
        #                "NATURAL JOIN Specialization "
        #                )
        # print_table(cursor)
