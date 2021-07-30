from database import new_connection
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO groups (description) VALUES (%s)'
args = (('casa', ), ('Trabalho', ), )

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        print(f'{cursor.rowcount} records were included!')
