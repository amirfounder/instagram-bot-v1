from src.content_factory.index import ContentFactory
from src.database_manager.index import DatabaseManager
from src.http_proxy.index import HttpProxy
from multiprocessing import Process

class ProgramRunner:

  content_creation_runners = [
    ContentFactory.run_flask_server,
    ContentFactory.run_react_server,
  ]

  research_runners = [
    HttpProxy.run,
    DatabaseManager.run
  ]


  # Main

  @classmethod
  def run(self):
    self.run_processes(self.content_creation_runners)

  # Helper

  @staticmethod
  def run_processes(runners):
    processes = []

    for runner in runners:
      processes.append(Process(name=str(runner), target=runner))
    
    for process in processes:
      process.start()
    
    for process in processes:
      process.join()