from src.database_manager.domains.mysql.MySQLConnection import MySQLConnection

class DatabaseManager:

  @staticmethod
  def run():
    connection = MySQLConnection()
    connection.connect('localhost', 'root', 'root')
    databases = connection.get_databases()
    print(databases)