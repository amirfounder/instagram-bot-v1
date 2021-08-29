from src.http_proxy.domains.instagram.InstagramHttpAnalyzer import InstagramHttpAnalyzer
from src.utils.ConsoleLogger import ConsoleLogger


class HttpResponseAnalyzer:

  def __init__(self) -> None:
    self.instagram_http_analyzer = InstagramHttpAnalyzer()
    self.console_logger = ConsoleLogger()

  def handle_response_flow(self, flow, timestamp):
    request_url = flow.request.pretty_url
    
    if 'instagram.com' in request_url:
      self.console_logger.info('Instagram (instagram.com) found in the URL')
      self.instagram_http_analyzer.handle_response_flow(flow, timestamp)
    
    if 'google.com' in request_url:
      self.console_logger.info('Google (google.com) found in the URL')
    
    if 'facebook.com' in request_url:
      self.console_logger.info('Facebook (facebook.com) found in the URL')
    
    if 'reddit.com' in request_url:
      self.console_logger.info('Reddit (reddit.com) found in the URL')