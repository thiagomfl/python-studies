from database import new_connection
from mysql.connector.errors import ProgrammingError

list_table = 'SHOW TABLES'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(list_table)
        except ProgrammingError as error:
            print(f'Error: {error.msg}')
except ProgrammingError as error:
    print(f'Connection Error: {error.msg}')

for i, table in enumerate(cursor, start=1):
	print(f'Table: {i}, {table[0]}')
