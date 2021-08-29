import json
from src.utils.FileLogger import FileLogger
from src.utils.ConsoleLogger import ConsoleLogger
from src.utils.constants import MITM_PROXY_INSTAGRAM_LOG_DIRECTORY


class InstagramHttpAnalyzer:

  def __init__(self) -> None:
    self.file_logger = FileLogger()
    self.file_logger.set_log_directory(MITM_PROXY_INSTAGRAM_LOG_DIRECTORY)
    self.console_logger = ConsoleLogger()

  def handle_response_flow(self, flow, timestamp):

    metadata = self.build_metadata(flow, timestamp)
    response = flow.response.text

    content = self.build_storeable_content(response, metadata)

    response_is_json = self.is_content_json(response)

    if response_is_json:
      self.handle_json_content(content)

  def handle_json_content(self, content):
    self.console_logger.info("Response is in json format")
    self.console_logger.info(content)
    self.file_logger.log(content)
    self.console_logger.success(f'Successfully logged response to file')

  def build_storeable_content(self, response, metadata):
    return {
      'response': response,
      'metadata': metadata
    }

  def build_metadata(self, flow, timestamp):
    return {
      'timestamp': timestamp,
      'request_url': self.try_get_request_url(flow),
      'version': 2
    }
  
  def try_get_request_url(self, flow):
    try:
      return flow.request.pretty_url
    except:
      return None
  
  def is_content_json(self, body):
    try:
      json.loads(body)
      return True
    except:
      return False