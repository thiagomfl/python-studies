from mysql.connector import connect

connection = connect(host='localhost', port=3306, user='root', passwd='root')

cursor = connection.cursor()
cursor.execute('CREATE DATABASE iF NOT EXISTS agenda')

