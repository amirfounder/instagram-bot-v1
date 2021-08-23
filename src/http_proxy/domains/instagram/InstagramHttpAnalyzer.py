from src.utils.FileLogger import FileLogger
from src.utils.ConsoleLogger import ConsoleLogger


class InstagramHttpAnalyzer:

  def __init__(self) -> None:
    self.file_logger = FileLogger()
    self.file_logger.set_log_directory('C:\\logs\\mitm_logs\\ig_responses')

    self.console_logger = ConsoleLogger()

  def handle_flow(self, flow, timestamp):

    metadata = self.build_metadata(flow, timestamp)
    body = flow.response.text

    self.console_logger.info(metadata)
    self.console_logger.info(body)
  
  def build_metadata(self, flow, timestamp):
    request_url = self.try_get_request_url(flow)
    
    return {
      'timestamp': timestamp,
      'request_url': request_url
    }
  
  def try_get_request_url(self, flow):
    try:
      return flow.request.pretty_url
    except:
      return None