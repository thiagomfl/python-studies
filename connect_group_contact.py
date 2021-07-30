from mysql.connector.errors import ProgrammingError
from database import new_connection

select_group = 'SELECT if FROM groups WHERE description = %s'
update_contact = 'UPDATE contacts SET group_id = %s WHERE name = %s'
contact_group = {
    'Thiago Moura': 'Casa',
    'Thiago': 'Trabalho',
    'Ferreira': 'Casa',
    'Lima': 'Trabalho'
}

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        for contact, group in contact_group.items():
            cursor.execute(select_group, (group, ))
            group_id = cursor. fetchone()[0]
            cursor.execute(update_contact, (group_id, contact))

    except ProgrammingError as e:
        print(f'Error: {e.msg}')

    else:
        print('Contacts were connecteds!')

