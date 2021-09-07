from src.database_manager.domains.mysql.MySQLConnection import MySQLConnection
from src.utils.FileParser import FileParser
from src.utils.constants import MITM_PROXY_INSTAGRAM_LOG_DIRECTORY
from src.utils.SkeletonBuilder import SkeletonBuilder
import json


class InstagramDataTransporter:
  """
  Summary:
  --------
  The purpose of the InstagramDataTransporter is to transport data across multiple mediums. The only use case (at
  this time) is parsing data from a file and saving it to the database.

  Process:
  --------
  1. Read contents from file (return list(strings))
  2. Parse contents (return list(dicts))
  3. Analyze each data item:
    3a. Filter data items based
    3b. Group similar data items
    3c. Save data items to database
  """

  def __init__(self) -> None:
    self.file_parser = FileParser()
    self.file_parser.set_directory_path(MITM_PROXY_INSTAGRAM_LOG_DIRECTORY)

    self.mysql_connection = MySQLConnection()
    self.mysql_connection.connect('localhost', 'root', 'root')
    
    self.skeleton_builder = SkeletonBuilder()
  
  def transport_file_data_to_mysql_database(self):
    data = self.get_latest_file_data()

    hashtag_and_user_data = self.get_hashtags_from_data(data)
    posts_data = self.get_posts_from_data(data)

    self.mysql_connection
  
  def group_responses_by_skeleton(self, responses):
    groups = []

  def group_responses(self, responses):
    hashtag_and_users_data = []
    posts_data = []
    related_users_data = []
    unkown_data = []

    for response in responses:
      if self.response_contains_hashtag_and_users_data(response['response']):
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
  
  def response_contains_hashtag_and_users_data(self, response):
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
    contents = self.file_parser.get_contents_from_files_in_directory()
    parsed_json_contents = self.parse_json_contents(contents)

    return parsed_json_contents
  
  def parse_json_contents(self, contents):
    parsed_json_contents = []
    
    for content_item in contents:
      data_item = {}
      data_item['metadata'] = content_item['metadata']
      data_item['response'] = json.loads(content_item['response'])
      parsed_json_contents.append(data_item)

    return parsed_json_contents
  
  def filter_response_data(self, response_data):

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
    
    filtered_response_data = []

    for response_data_point in response_data:
      if response_data_point['response'] not in bad_responses:
        filtered_response_data.append(response_data_point)
    
    return filtered_response_data
