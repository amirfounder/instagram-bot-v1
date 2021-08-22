import os


class HttpProxy:

  @staticmethod
  def run():
    os.system('mitmdump -s .\src\http_proxy\proxy.py')