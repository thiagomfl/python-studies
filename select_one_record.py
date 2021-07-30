from database import new_connection

select_data = 'SELECT name, fone FROM contacts'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(select_data)
    print(cursor.fetchone())
