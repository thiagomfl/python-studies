from database import new_connection

# select order by
filter_data = 'SELECT name FROM contacts ORDER BY name DESC'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(filter_data)

    print('\n'.join(record[0] for record in cursor))
