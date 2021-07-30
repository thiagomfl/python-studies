from database import new_connection
from mysql.connector.errors import ProgrammingError

delete_table_emails = 'DROP TABLE IF EXISTS emails'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(delete_table_emails)
        except ProgrammingError as error:
            print(f'Error: {error.msg}')
except ProgrammingError as error:
    print(f'Connection Error: {error.msg}')
