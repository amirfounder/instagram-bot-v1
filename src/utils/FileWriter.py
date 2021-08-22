import json
from src.utils.FileSystem import FileSystem as fs


class FileWriter:

  def __init__(self, file_path=None) -> None:
    self.__file_path = file_path

  # Getters and setters

  def set_file_path(self, file_path) -> None:
    self.__file_path = file_path
  
  def get_file_path(self) -> str:
    return self.__file_path
  
  # Write to file

  def write_to_file(self, content):
    content = fs.convert_to_string(content)
    with open(self.__file_path, 'a') as f:
      f.write(content + '\n')
