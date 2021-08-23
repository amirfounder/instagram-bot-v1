from datetime import datetime
import json

def pad_string(string, pad_char, length, position):
    while len(string) < length:

      if position.upper() == 'BEFORE':
        string = pad_char + string
      elif position.upper() == 'AFTER':
        string += pad_char
      else:
        raise Exception(f'Unsupported position value: {position}')

    return string

def get_timestamp():
  now = datetime.now()
  return now.strftime("%Y-%m-%d %H:%M:%S.%f")[:23]

def convert_to_string(content):
    if type(content) is not str:
      return json.dumps(content)
    return content