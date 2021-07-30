from database import new_connection
from mysql.connector.errors import ProgrammingError

insert_data = 'INSERT INTO contacts (name, fone) VALUES (%s, %s)'
args = (
    ('Thiago', '81998113680'),
    ('Moura', '8194513680'),
    ('Ferreira', '81955413680'),
    ('Lima', '324234234'),
)


with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(insert_data, args)
        connection.commit()
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        print(f'{cursor.rowcount} records were included!')
