import json


class FileParser:

  def __init__(self, file_path=None, directory_path=None) -> None:
    self.directory_path = directory_path
    self.file_path = file_path

  def set_file_path(self, file_path):
    self.file_path = file_path
  
  def get_file_path(self):
    return self.file_path

  def set_directory_path(self, directory_path):
    self.directory_path = directory_path
  
  def get_directory_path(self):
    return self.directory_path
  
  def parse_file_contents_list(self):
    file_contents_string_list = self.parse_file_contents('\n')
    file_contents_list = []

    for file_contents_string in file_contents_string_list:
      try:
        file_contents = json.loads(file_contents_string)
        file_contents_list.append(file_contents)
      except:
        break
    
    return file_contents_list

  def parse_file_contents(self, delimiter):
    file_contents = self.read_file(self.file_path)
    file_contents_list = file_contents.split(delimiter)
    return file_contents_list

  def read_file(self, file_path):
    file_contents = ""

    with open(file_path, 'r') as f:
      file_contents = f.read()
    
    return file_contents