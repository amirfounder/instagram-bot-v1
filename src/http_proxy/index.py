import os


class HttpProxyRunner:

  @staticmethod
  def run():
    os.system('mitmdump -s .\src\http_proxy\proxy.py --set console_eventlog_verbosity=error termlog_verbosity=error')