from src.database_manager.index import DatabaseManager
from src.http_proxy.index import HttpProxy
from multiprocessing import Process

class ProgramRunner:

  runners = [
    DatabaseManager.run,
    HttpProxy.run
  ]

  # Main

  @classmethod
  def run(self):
    self.run_processes(self.runners)

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