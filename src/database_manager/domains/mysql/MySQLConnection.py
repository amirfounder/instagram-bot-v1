import mysql.connector
from typing import Any

from src.database_manager.abstracts.Connection import Connection
from src.database_manager.data_structs.Database import Database
from src.database_manager.data_structs.Column import Column
from src.database_manager.data_structs.Table import Table
from src.database_manager.domains.mysql.MySQLQueryFactory import MySQLQueryFactory


class MySQLConnection(Connection):

  def __init__(self, host=None, user=None, password=None, database=None) -> None:

    if all(x is not None for x in [host, user, password]):
      self.connect(host, user, password, database)

    self.query_factory = MySQLQueryFactory()
    
  def connect(self, host, user, password, database=None) -> None:
    self.connection = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )
    connection_host = self.connection._host
    connection_port = self.connection._port
    print(f'Successfully connected to Database @{connection_host}:{connection_port}')

    self.cursor = self.connection.cursor()

  def load_database(self, database: Database) -> None:
      return super().load_database(database)
  
  def load_table(self, table: Table) -> None:
    return super().load_table(table)
  
  def close(self) -> None:
    self.connection.close()
  
  def execute(self, query) -> Any:
    self.cursor.execute(query)
    return self.cursor.fetchall()

  def get_databases(self):
    databases = []
    
    query = self.query_factory.build_show_databases_query()
    results = self.execute(query)

    for result in results:
      databases.append(Database(result[0]))
    
    return databases
  
  def get_tables(self, database):
    tables = []

    query = self.query_factory.build_show_tables_query(database)
    results = self.execute(query)

    for result in results:
      tables.append(Table(result[0]))
    
    return tables
  
  def get_columns(self, database, table):
    columns = []

    query = self.query_factory.build_show_columns_query(database, table)
    results = self.execute(query)

    for result in results:
      columns.append(Column(result[0], result[1], result[3]))
    
    return columns