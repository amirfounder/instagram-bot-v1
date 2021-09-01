from src.database_manager.domains.mysql.MySQLConnection import MySQLConnection

from src.utils.ConsoleLogger import ConsoleLogger

class DatabaseManager:

  @staticmethod
  def run():
    connection = MySQLConnection()
    connection.connect('localhost', 'root', 'root')