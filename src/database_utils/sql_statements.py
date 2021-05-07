SQL_CREATE_SUPERVISOR_TABLE = """ CREATE TABLE IF NOT EXISTS Supervisor(
                                        supervisor_id INTEGER PRIMARY KEY,
                                        supervisor_name TEXT(100) NOT NULL
                                    ); """

SQL_CREATE_ASSIGNED_STATUS_TABLE = """ CREATE TABLE IF NOT EXISTS Assigned_status(
                                        assigned_status_id INTEGER PRIMARY KEY,
                                        assigned_status TEXT(100) NOT NULL
                                    ); """

SQL_CREATE_NUMBER_OF_STUDENTS_TABLE = """ CREATE TABLE IF NOT EXISTS Number_of_students(
                                        num_students_id INTEGER PRIMARY KEY,
                                        num_students TEXT(100) NOT NULL
                                    ); """

SQL_CREATE_SPECIALIZATION_TABLE = """ CREATE TABLE IF NOT EXISTS Specialization(
                                        specialization_id INTEGER PRIMARY KEY,
                                        specialization_name TEXT(100) NOT NULL
                                    ); """

SQL_CREATE_THESIS_TABLE = """ CREATE TABLE IF NOT EXISTS Thesis(
                                        thesis_id INTEGER PRIMARY KEY,
                                        thesis_name TEXT(200) NOT NULL,
                                        supervisor_id INTEGER NOT NULL,
                                        assigned_status_id INTEGER NOT NULL,
                                        num_students_id INTEGER NOT NULL,
                                        url TEXT(100) NOT NULL,
                                        description TEXT(10000) NOT NULL,
                                        FOREIGN KEY (supervisor_id) 
                                            REFERENCES Supervisor(supervisor_id) 
                                                ON DELETE NO ACTION
                                                ON UPDATE CASCADE,
                                        FOREIGN KEY (assigned_status_id) 
                                            REFERENCES Assigned_status(assigned_status_id) 
                                                ON DELETE NO ACTION
                                                ON UPDATE NO ACTION,
                                        FOREIGN KEY (num_students_id) 
                                            REFERENCES Number_of_students(num_students_id) 
                                                ON DELETE NO ACTION
                                                ON UPDATE NO ACTION
                                    ); """

SQL_CREATE_THESIS_SPECIALIZATIONS_TABLE = """ CREATE TABLE IF NOT EXISTS Thesis_specializations(
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
