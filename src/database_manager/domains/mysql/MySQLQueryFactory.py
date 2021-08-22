from src.database_manager.abstracts.QueryFactory import QueryFactory
from src.database_manager.data_structs.Column import Column
from src.database_manager.data_structs.Database import Database
from src.database_manager.data_structs.Table import Table


class MySQLQueryFactory(QueryFactory):
  
  def __init__(self) -> None:
    pass

  def build_query(self, query):
    return f"{query}\n;"
  
  def build_statement(self, statement):
    return f"{statement}\n"

  def build_show_databases_query(self):
    return self.build_query('SHOW DATABASES')
  
  def build_show_tables_query(self, database):
    return self.build_query(f'SHOW TABLES FROM {database}')
  
  def build_show_columns_query(self, database, table):
    return self.build_query(f'SHOW COLUMNS FROM {database}.{table}')