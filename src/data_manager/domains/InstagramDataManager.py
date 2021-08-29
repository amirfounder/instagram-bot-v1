from src.database_manager.domains.mysql.MySQLConnection import MySQLConnection
from src.utils.FileParser import FileParser
from src.utils.constants import MITM_PROXY_INSTAGRAM_LOG_DIRECTORY
import time
import json


class InstagramDataManager:

  def __init__(self) -> None:
    self.file_parser = FileParser()
    self.file_parser.set_directory_path(MITM_PROXY_INSTAGRAM_LOG_DIRECTORY)

    self.mysql_connection = MySQLConnection()
    self.mysql_connection.connect('localhost', 'root', 'root')
  
  def transfer_file_data_to_mysql(self):
    data = self.get_latest_file_data()

    hashtag_data = self.get_hashtags_from_data(data)
    users_data = self.get_users_from_data(data)
    posts_data = self.get_posts_from_data(data)

    self.mysql_connection

  def get_responses_from_file(self):
    responses = self.file_parser.get_contents_from_files_in_directory()
    return responses
  
  def filter_responses(self, responses):
    pass
