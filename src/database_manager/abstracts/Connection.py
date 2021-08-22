from abc import ABCMeta, abstractmethod


class Connection(metaclass=ABCMeta):

  @abstractmethod
  def connect(self, host, user, password, database):
    pass

  @abstractmethod
  def close(self):
    pass

  @abstractmethod
  def execute(self, query):
    pass