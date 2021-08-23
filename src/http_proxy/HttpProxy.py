from src.http_proxy.analyzers.HttpResponseAnalyzer import HttpResponseAnalyzer
from src.utils.ConsoleLogger import ConsoleLogger
from src.utils import utils


class HttpProxy:

  def __init__(self) -> None:
    self.resposne_analyzers = HttpResponseAnalyzer()
    self.console_logger = ConsoleLogger()
    self.console_logger.success('Started sniffing. No errors', format=False)

  def response(self, flow):
    timestamp = utils.get_timestamp()
    self.resposne_analyzers.handle_response_flow(flow, timestamp)