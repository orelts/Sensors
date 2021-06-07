"""!
@brief sql_initiate: lazy initializing all the needed sql server tables for the modules interactions.
sql server is Azure SQL edge server.
"""


from sql.sql_config import *


if __name__ == '__main__':

    conn, cursor = connect_to_db()
    init_database(cursor, conn)

    init_sql_table(cursor, conn, "SensorsInfo", d_sensors, False)

    print_sql_row(cursor, "SensorsInfo")
    
