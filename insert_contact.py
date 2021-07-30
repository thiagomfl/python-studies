from database import new_connection
from mysql.connector.errors import ProgrammingError

insert_data = 'INSERT INTO contacts (name, fone) VALUES (%s, %s)'
args = ('Thiago', '81998113680')


with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(insert_data, args)
        connection.commit()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        print('1 record included, ID:', cursor.lastrowid)
