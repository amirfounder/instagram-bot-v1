from os import times
from colorama import Fore, Style
from src.utils import utils


class ConsoleLogger:

  def __init__(self, colors=None) -> None:
    self.__colors = {
      'success': Fore.GREEN + Style.BRIGHT,
      'info': Fore.WHITE + Style.NORMAL,
      'warn': Fore.YELLOW + Style.BRIGHT,
      'error': Fore.RED + Style.DIM,
      'alert': Fore.RED + Style.BRIGHT
    }
    if colors is not None:
      self.set_colors(colors)

  def set_colors(self, colors) -> None:
    for key, value in colors.items():
      if key in self.__colors.keys():
        self.__colors[key] = value
  
  def get_colors(self) -> None:
    return self.__colors

  def log(self, message, log_type):
    message = self.pad_log_message(message, log_type)
    
    if log_type.lower() not in self.__colors:
      raise Exception(f'Invalid log type: {log_type}')
    
    color = self.__colors[log_type]

    self.log_with_color(message, color)
    
  def log_with_color(self, message, color):
    print(color + message + Style.RESET_ALL)
  
  def pad_log_message(self, message, log_type):
    padded_message = ""
    timestamp = utils.get_timestamp()
    
    padded_message += self.pad_log_section(timestamp, 30)
    padded_message += self.pad_log_section(log_type.upper(), 10)
    padded_message += self.pad_log_section(message, 100)

    return padded_message
  
  def pad_log_section(self, string, section_length):
    padded_string = utils.pad_string(string, '.', section_length - 1, 'AFTER')
    padded_string += ' '
    return padded_string

  def success(self, message):
    pass
  
  def info(self, message):
    pass
  
  def warn(self, message):
    pass
  
  def error(self, message):
    pass

  def alert(self, message):
    pass