from database import new_connection
from mysql.connector.errors import ProgrammingError

table_group = 'CREATE TABLE IF NOT EXISTS groups(id INT AUTO_INCREMENT PRIMARY KEY, description VARCHAR(50), fone VARCHAR(40))'

insert_field = 'ALTER TABLE contacts ADD group_id INT'
update_contact = 'ALTER TABLE contacts ADD FOREIGN KEY (group_id) REFERENCES groups(id)'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_group)
            cursor.execute(insert_field)
            cursor.execute(update_contact)

        except ProgrammingError as e:
            print(f'Error: {e.msg}')

except ProgrammingError as e:
    print(f'Connection Error: {e.msg}')
