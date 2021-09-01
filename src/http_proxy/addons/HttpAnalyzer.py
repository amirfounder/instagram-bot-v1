from src.http_proxy.analyzers.HttpResponseAnalyzer import HttpResponseAnalyzer
from src.utils.ConsoleLogger import ConsoleLogger
from src.utils import utils


class HttpAnalyzer:

  def __init__(self) -> None:
    self.response_analyzer = HttpResponseAnalyzer()
    self.console_logger = ConsoleLogger()
    self.console_logger.success('Started analyzing HTTP Requests / Responses')

  def response(self, flow):
    timestamp = utils.get_timestamp()
    self.response_analyzer.handle_response_flow(flow, timestamp)