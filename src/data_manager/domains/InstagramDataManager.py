from src.utils.FileParser import FileParser
from src.utils.constants import MITM_PROXY_INSTAGRAM_REQUEST_LOG_DIRECTORY, MITM_PROXY_INSTAGRAM_RESPONSE_LOG_DIRECTORY
import time


class InstagramDataManager:

  def __init__(self) -> None:
    self.request_file_parser = FileParser()
    self.response_file_parser = FileParser()

    self.request_file_parser.set_directory_path(MITM_PROXY_INSTAGRAM_REQUEST_LOG_DIRECTORY)
    self.response_file_parser.set_directory_path(MITM_PROXY_INSTAGRAM_RESPONSE_LOG_DIRECTORY)
  
  def main(self):
    self.loop(10)

  def loop(self, seconds_between):
    time.sleep(seconds_between)
  
  def get_instagram_responses(self):
    responses = self.response_file_parser.get_contents_from_files_in_directory()
    return responses