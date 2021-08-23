from src.database_manager.index import DatabaseManagerRunner
from src.http_proxy.index import HttpProxyRunner
from multiprocessing import Process


def main():

  p1 = Process(name='DatabaseManager Process', target=DatabaseManagerRunner.run)
  p2 = Process(name='HttpProxy Process', target=HttpProxyRunner.run)

  p1.start()
  p2.start()

  p1.join()
  p2.join()

if __name__ == '__main__':
  main()