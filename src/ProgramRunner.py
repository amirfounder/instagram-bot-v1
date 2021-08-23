from os import stat
from src.database_manager.index import DatabaseManagerRunner
from src.http_proxy.index import HttpProxyRunner
from multiprocessing import Process

class ProgramRunner:

  # Main

  @classmethod
  def run(self):
    self.research()

  # Specialized Processes

  @classmethod
  def research(self):
    runners = [
      DatabaseManagerRunner.run,
      HttpProxyRunner.run
    ]
    self.run_processes(runners)

  # Helpers

  @staticmethod
  def run_processes(runners):
    processes = []

    for runner in runners:
      processes.append(Process(name=str(runner), target=runner))
    
    for process in processes:
      process.start()
    
    for process in processes:
      process.join()