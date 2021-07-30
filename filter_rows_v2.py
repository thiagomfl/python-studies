from database import new_connection

filter_data = 'SELECT * FROM contacts WHERE fone LIKE "%819%"'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(filter_data)

    for x in cursor:
        print(x)
