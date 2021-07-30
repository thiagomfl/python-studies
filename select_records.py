from database import new_connection
from mysql.connector.errors import ProgrammingError

select_data = 'SELECT * FROM contacts'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(select_data)
        contacts = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:10s} fone: {contact[1]}')
