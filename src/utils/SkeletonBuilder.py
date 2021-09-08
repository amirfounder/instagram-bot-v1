class TestClass(object):
  def __init__(self, key='green') -> None:
    self.custom_key = key

class SkeletonBuilder:

  def __init__(self) -> None:
    pass

  def build(self, object_to_skelatize: dict):
    built_target = None

    if type(object_to_skelatize) is dict:
      built_target = self.skelatize_dict(object_to_skelatize)
    elif type(object_to_skelatize) is list:
      built_target = self.skelatize_list(object_to_skelatize)
    
    return built_target

  def skelatize_dict(self, dictionary_to_skelatize: dict):
    items = dictionary_to_skelatize.items()
    skeleton = {}

    for key, value in items:

      value_type = type(value)
      value_type_name = value_type.__name__

      if value_type_name == 'list': 
        skeleton[key] = self.skelatize_list(value)
      elif value_type_name == 'dict':
        skeleton[key] = self.skelatize_dict(value)
      else:
        skeleton[key] = value_type_name
    
    return skeleton

  def skelatize_list(self, list_to_skelatize: list):
    value_types = []
    unique_value_types = []

    for item in list_to_skelatize:

      item_type = type(item)
      item_type_name = item_type.__name__

      if item_type_name == 'list':
        unique_value_types.append(self.skelatize_list(item))
      elif item_type_name == 'dict':
        unique_value_types.append(self.skelatize_dict(item))
      else:
        unique_value_types.append(item_type_name)
    
    # Using a manual for loop due to the fact when calling a set a dictionary is not hashable
    for value_type in value_types:
      if value_type not in unique_value_types:
        unique_value_types.append(value_type)

    return unique_value_types
  
  def skelatize_custom_class(self, object_to_skelatize):
    if '__dict__' in dir(object_to_skelatize):
      return self.skelatize_dict(object_to_skelatize.__dict__)

  def is_custom_class(self, object_to_check):
    if '__class__' in dir(object_to_check):
      if '__module__' in object_to_check.__class__:
        if object_to_check.__class__.__module__ != 'builtins':
          return True
    return False


test_class_instance = TestClass('blue')

test_dict = {
  'string_ley': 'random_string',
  'int_key': 9,
  'float_key': 9.2,
  'dict_key': {
    'key1': 'value1',
    'key2': 'value2'
  },
  'list_key': [8, 'string', 92.5, 8, 8, 8, 3],
  'advanced_obj1': {
    'blue': [
      {
        'green': 'yes'
      }
    ],
  },
  'class_key': test_class_instance
}

builder = SkeletonBuilder()
skeleton = builder.build(test_dict)

object1 = {'blue': 'green', 'person': {'name': 'jack'}}
object2 = {'blue': 'yellow', 'person': {'name': 'bob'}}

skeleton1 = builder.build(object1)
skeleton2 = builder.build(object2)

print(skeleton1 == skeleton2)