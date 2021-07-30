from database import new_connection

# select sem sql injection
filter_data = 'SELECT * FROM contacts WHERE name LIKE %s'

with new_connection() as connection:
    name = input('Search contact: ')
    args = (f'%{name}%', )

    cursor = connection.cursor()
    cursor.execute(filter_data, args)

    for x in cursor:
        print(x)
