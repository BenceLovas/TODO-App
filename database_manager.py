import psycopg2

CONNECTION_STR = "dbname=todo_database user=bans password=pass host=localhost"


def query_select_all(sql_str="SELECT * FROM test", connection_str=CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_str)
                return cursor.fetchall()
    except psycopg2.DatabaseError as exception:
        print(exception)


def query_select(sql_str, variables, connection_str=CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_str, variables)
                return cursor.fetchall()
    except psycopg2.DatabaseError as exception:
        print(exception)


def query_modify(sql_str, variables, connection_str=CONNECTION_STR):
    try:
        with psycopg2.connect(connection_str) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_str, variables)
                connection.commit()
                print(sql_str.split()[0] + " done.")
    except psycopg2.DatabaseError as exception:
        connection.rollback()
        print(exception)
