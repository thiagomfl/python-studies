from database import new_connection

with new_connection() as connection:
    if connection.is_connected():
        print('Connected!')

print('The end!')