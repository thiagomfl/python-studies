from collections import defaultdict
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
        try:
          cursor.execute(sql_join)
          contacts = cursor.fetchall()

        finally:
          cursor.close()

    except ProgrammingError as e:
        print(f'Error: {e.msg}')

    else:
        grouped = defaultdict(list)
        for contact in contacts:
            grouped[contact['group']].append(contact['name'])

        print(grouped)
