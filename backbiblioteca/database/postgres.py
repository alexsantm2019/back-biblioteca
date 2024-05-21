import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        dbname='biblioteca_galapagos_test',
        user='postgres',
        password='postgres',
        host='localhost',
        port="5432"
    )
    return conn
