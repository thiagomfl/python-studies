from database import new_connection
from mysql.connector.errors import ProgrammingError

sql_join = '''
  SELECT
    groups.description AS group,
    contacts.name AS contact
  FROM contacts
  INNER JOIN groups ON contacts.group_id = groups.id
  ORDER BY group, contact
'''

with new_connection() as connection:
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_join)
        contacts = cursor.fetchall()

    except ProgrammingError as e:
        print(f'Error: {e.msg}')

    else:
        for contact in contacts:
            print(f'{contact["group"]}: {contact["contact"]}')
