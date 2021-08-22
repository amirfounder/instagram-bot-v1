import os
import json


class FileSystem:

  @staticmethod
  def is_valid_directory(directory_path):
    return os.path.isdir(directory_path)
  
  @staticmethod
  def is_valid_file(file_path):
    return os.path.isfile(file_path)
  
  @staticmethod
  def get_file_size(file_path):
    return os.path.getsize(file_path)
  
  @staticmethod
  def convert_to_string(content):
    if type(content) is not str:
      return json.dumps(content)
    return content

  # Extract

  @classmethod
  def get_directory_path_from_file_path(self, file_path):

    path_list = file_path.split('\\')
    path_list.pop()

    return '\\'.join(path_list)

  # Build directories

  @classmethod
  def build_directories_from_file_path(self, file_path) -> None:
    directory_path = self.get_directory_path_from_file_path(file_path)
    self.build_directories_from_path(directory_path)

  @classmethod
  def build_directories_from_path(self, path) -> None:
    directory_list = path.split('\\')
    base_path = ""

    for directory_list_item in directory_list:

      base_path += directory_list_item
      self.build_directory_from_path(base_path)
      base_path += "\\"

  @classmethod
  def build_directory_from_path(self, path) -> None:
    try:
      os.mkdir(path)
    except FileExistsError:
      pass

  # Get items from directories

  @classmethod
  def get_dirs_from_directory(self, directory_path):
    dirs = []

    items = self.get_items_from_directory(directory_path)
    for item in items:
      if item['type'] == 'directory':
        dirs.append(item)

    return dirs

  @classmethod
  def get_files_from_directory(self, directory_path):
    files = []

    items = self.get_items_from_directory(directory_path)
    for item in items:
      if item['type'] == 'file':
        files.append(item)
    
    return files

  @classmethod
  def get_items_from_directory(self, directory_path):
    item_names = os.listdir(directory_path)
    return self.get_items_list(directory_path, item_names)
  
  # Constructing items

  @classmethod
  def get_items_list(self, directory_path, item_names):
    items = []

    for item_name in item_names:
      items.append(self.get_item(directory_path, item_name))
    
    return items

  @classmethod
  def get_item(self, directory_path, item_name):
    item_path = f'{directory_path}\\{item_name}'
    item_type = 'file' if os.path.isfile(item_path) else 'directory'
    item_ext = None

    if item_type == 'file' and '.' in item_name:
      item_attr_list = item_name.split('.')
      item_name = item_attr_list[0]
      item_ext = item_attr_list[1]

    return {
      'name': item_name,
      'path': item_path,
      'type': item_type,
      'ext': item_ext
    }