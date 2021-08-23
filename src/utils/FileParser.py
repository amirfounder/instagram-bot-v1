from src.utils.FileSystem import FileSystem as fs
import json


class FileParser:

  def __init__(self, file_path=None, directory_path=None) -> None:
    self.directory_path = directory_path
    self.file_path = file_path

  # Getters and setters

  def set_file_path(self, file_path):
    self.file_path = file_path
  
  def get_file_path(self):
    return self.file_path

  def set_directory_path(self, directory_path):
    self.directory_path = directory_path
  
  def get_directory_path(self):
    return self.directory_path
  
  # Getting contents

  def get_contents_from_files_in_directory(self, directory_path=None):
    raw_content = self.read_files_from_directory(directory_path or self.directory_path)
    parsed_content = self.parse_content(raw_content)
    return parsed_content

  def get_contents_from_file(self, file_path=None):
    raw_content = self.read_file(file_path or self.file_path)
    parsed_content = self.parse_content(raw_content)

  # Parsing contents

  def parse_content(self, content):
    contents_list = self.split_content_into_list(content, '\n')
    parsed_contents = []

    for file_contents_string in contents_list:
      try:
        file_contents = json.loads(file_contents_string)
        parsed_contents.append(file_contents)
      except:
        pass
    
    return parsed_contents

  def split_content_into_list(self, content, delimiter):
    file_contents_list = content.split(delimiter)
    return file_contents_list

  # Getting contents

  def read_files_from_directory(self, directory_path=None):
    contents = ""

    files = fs.get_files_from_directory(directory_path or self.directory_path)
    dirs = fs.get_dirs_from_directory(directory_path or self.directory_path)

    for file in files:
      file_path = file['path']
      file_contents = self.read_file(file_path)
      contents += file_contents
      contents += '\n'
    
    for directory in dirs:
      dir_path = directory['path']
      dir_contents = self.read_files_from_directory(dir_path)
      contents += dir_contents
      contents += '\n'
    
    return contents
  
  def read_file(self, file_path):
    contents = ""

    with open(file_path or self.file_path, 'r') as f:
      contents = f.read()
    
    return contents
  
