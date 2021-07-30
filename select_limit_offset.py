from database import new_connection
from mysql.connector.errors import ProgrammingError

# select order by
sql = 'SELECT * FROM contacts LIMIT %s OFFSET %s'
args = (5, 8)

with new_connection() as connection:
    try:
      cursor = connection.cursor()
      cursor.execute(sql, args)
      contacts = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:10s} fone: {contact[1]}')
