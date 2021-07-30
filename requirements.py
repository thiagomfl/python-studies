try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector is not installed!')
else:
    print('MySQL Connector already installed!')
