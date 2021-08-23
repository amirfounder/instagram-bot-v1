from datetime import datetime
from src.utils.FileWriter import FileWriter as fw
from src.utils.FileSystem import FileSystem as fs
from src.utils import utils


class FileLogger:

  def __init__(self, log_directory=None, max_file_size=None) -> None:
    self.log_directory = log_directory
    self.max_file_size = max_file_size or 25 * 1000 * 1000
    self.fw = fw()
  
  # Getters and setters

  def set_log_directory(self, log_directory):
    self.log_directory = log_directory
  
  def get_log_directory(self):
    return self.log_directory
  
  def set_max_file_size(self, max_file_size):
    self.max_file_size = max_file_size
  
  def get_max_file_size(self):
    return self.max_file_size

  # Log

  def log(self, content):
    file_path = self.generate_valid_log_file_path(content)
    self.fw.set_file_path(file_path)
    self.fw.write_to_file(content)

  # Generate file paths and directories

  def generate_valid_log_file_path(self, content):
    directory_path = self.generate_todays_log_directory_path()
    is_valid_directory_path = fs.is_valid_directory(directory_path)

    if is_valid_directory_path:

      files = fs.get_files_from_directory(directory_path)

      if len(files) == 0:
        return self.generate_todays_first_log_file_path(directory_path)

      target_file = files[len(files) - 1]
      target_file_path = target_file['path']
      target_file_name = target_file['name']

      content_is_greater_than_file = self.is_content_greater_than_file(target_file_path, content)

      if content_is_greater_than_file:
        
        target_file_name = len(files) + 1
        target_file_name = self.pad_filename(target_file_name)
      
      return f'{directory_path}\\{target_file_name}.log'
    
    else:
      return self.generate_todays_first_log_file_path(directory_path)
  
  def generate_todays_first_log_file_path(self, directory_path):
      fs.build_directories_from_path(directory_path)
      return f'{directory_path}\\001.log'

  def generate_todays_log_directory_path(self):
    todays_log_directory = self.generate_todays_log_directory()
    return f'{self.log_directory}\\{todays_log_directory}'

  def generate_todays_log_directory(self):
    now = datetime.now()
    return now.strftime("%Y_%m_%d")

  def is_content_greater_than_file(self, file_path, content):
    content = fs.convert_to_string(content)

    content_size = len(content)
    file_size = fs.get_file_size(file_path)

    return content_size > self.max_file_size - file_size
  
  def pad_filename(self, filename):
    return utils.pad_string(str(filename), '0', 3, 'BEFORE')
