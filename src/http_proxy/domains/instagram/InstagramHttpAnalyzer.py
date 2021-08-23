import json
from src.utils.FileLogger import FileLogger
from src.utils.ConsoleLogger import ConsoleLogger
from src.utils.constants import MITM_PROXY_INSTAGRAM_REQUEST_LOG_DIRECTORY, MITM_PROXY_INSTAGRAM_RESPONSE_LOG_DIRECTORY


class InstagramHttpAnalyzer:

  def __init__(self) -> None:
    self.file_logger_requests = FileLogger()
    self.file_logger_responses = FileLogger()
    
    self.file_logger_requests.set_log_directory(MITM_PROXY_INSTAGRAM_REQUEST_LOG_DIRECTORY)
    self.file_logger_responses.set_log_directory(MITM_PROXY_INSTAGRAM_RESPONSE_LOG_DIRECTORY)

    self.console_logger = ConsoleLogger()

  def handle_response_flow(self, flow, timestamp):

    metadata = self.build_metadata(flow, timestamp)
    response = flow.response.text

    content_is_json = self.is_content_json(response)

    if content_is_json:
      self.console_logger.info("Response is in json format")
      self.console_logger.info(response)
      self.file_logger_responses.log({'response': response, 'metadata': metadata})
      self.console_logger.success(f'Successfully logged response to file')
  
  def build_metadata(self, flow, timestamp):
    return {
      'timestamp': timestamp,
      'request_url': self.try_get_request_url(flow)
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