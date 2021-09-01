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
  
  def group_responses(self, responses):
    hashtag_and_users_data = []
    unkown_data = []
    posts_data = []
    related_users_data = []

    for response in responses:
      if self.response_contains_hashtag_data(response['response']):
        hashtag_and_users_data.append(response)
      elif self.response_contains_posts_data(response['response']):
        posts_data.append(response)
      elif self.response_contains_related_users_data(response['response']):
        related_users_data.append(response)
      else:
        unkown_data.append(response)
    
    return {
      'hashtag_and_users_data': hashtag_and_users_data,
      'unkown_data': unkown_data,
      'posts_data': posts_data,
      'related_users_data': related_users_data
    }
  
  def response_contains_related_users_data(self, response):
    try:
      return 'edge_chaining' in response['user']['data']
    except:
      return False
  
  def response_contains_hashtag_data(self, response):
    try:
      return 'hashtags' in response and 'users' in response
    except:
      return False

  def response_contains_posts_data(self, response):
    try:
      return 'edge_web_feed_timeline' in response['data']['user']
    except:
      return False

  def get_instagram_responses(self):
    responses = self.file_parser.get_contents_from_files_in_directory()
    parsed_responses = self.parse_json_responses(responses)

    return parsed_responses
  
  def parse_json_responses(self, responses):
    parsed_responses = []
    
    for response in responses:
      data = response
      data['response'] = json.loads(response['response'])
      parsed_responses.append(data)

    return parsed_responses
  
  def filter_responses(self, responses):

    bad_responses = [
      {
        'checksum': '',
        'config': '',
        'config_owner_id': '',
        'app_data': '{}',
        'qpl_version': ''
      },
      {
        'status': 'ok'
      }
    ]
    
    filtered_responses = []

    for response in responses:
      if response['response'] not in bad_responses:
        filtered_responses.append(response)
    
    return filtered_responses
