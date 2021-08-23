from src.http_proxy.domains.instagram.InstagramHttpAnalyzer import InstagramHttpAnalyzer
from src.utils.ConsoleLogger import ConsoleLogger


class HttpResponseSniffer:

  def __init__(self) -> None:
    self.instagram_http_sniffer = InstagramHttpAnalyzer()
    self.console_logger = ConsoleLogger()

  def handle_flow(self, flow, timestamp):
    request_url = flow.request.pretty_url
    
    if 'instagram.com' in request_url:
      self.console_logger.success('Instagram (instagram.com) found in the URL')
      self.instagram_http_sniffer.handle_flow(flow, timestamp)
    