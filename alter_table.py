from database import new_connection
from mysql.connector.errors import ProgrammingError

alter_table_contacts = 'ALTER TABLE contacts ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(alter_table_contacts)
        except ProgrammingError as error:
            print(f'Error: {error.msg}')
except ProgrammingError as error:
    print(f'Connection Error: {error.msg}')
