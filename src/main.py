from mysql import connector
from database_managers.mysql.MySQLConnection import MySQLConnection

connection = MySQLConnection()
connection.connect('localhost', 'root', 'root')

print(connection.get_tables('test'))
print(connection.get_columns('test', 'test'))
print(connection.get_columns('test', 'test2'))