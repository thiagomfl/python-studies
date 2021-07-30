from database import new_connection
from mysql.connector.errors import ProgrammingError

# select order by
sql = 'DELETE FROM contacts WHERE name = %s'
args = ('Moura', )

with new_connection() as connection:
    try:

      cursor = connection.cursor()
      cursor.execute(sql, args)
      connection.commit()

      print('\n'.join(record[0] for record in cursor))
    except ProgrammingError as error:
        print(f'Error: {error.msg}')
    else:
        print(f'{cursor.rowcount} row(s) deleted!')
