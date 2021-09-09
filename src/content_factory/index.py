import os
import subprocess
from threading import Thread


class ContentFactory:

  @staticmethod
  def run_react_server():
    os.system('node src/content_factory/ui/scripts/start.js')
  
  @staticmethod
  def run_flask_server():
    os.system('python src/content_factory/api/server.py')
