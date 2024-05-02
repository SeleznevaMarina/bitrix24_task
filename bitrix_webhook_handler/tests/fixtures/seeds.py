import psycopg2


def execute_query(query, params=None):
    connection = psycopg2.connect(
        dbname="test_bitrix",
        user="marina",
        password="123",
        host="localhost"
        )
    cursor = connection.cursor()
    if params is not None:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    connection.commit()
    connection.close()

def insert_data(table, data):
    sql = f"INSERT INTO {table} (name) VALUES (%s)"
    execute_query(sql, (data['name'],))

def delete_data(table, data):
    sql = f"DELETE FROM {table} WHERE name IN (%s)"
    execute_query(sql, (data['name'],))
