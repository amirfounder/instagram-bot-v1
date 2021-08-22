from src.database_manager.index import DatabaseManager
from src.http_proxy.index import HttpProxy
from multiprocessing import Process
import os


def main():

  p1 = Process(target=DatabaseManager.run)
  p2 = Process(target=HttpProxy.run)

  p1.start()
  p2.start()

  p1.join()
  p2.join()

# if __name__ == '__main__':
#   main()