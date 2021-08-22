from abc import ABCMeta, abstractmethod


class QueryFactory(metaclass = ABCMeta):

  @abstractmethod
  def build_query():
    pass

  @abstractmethod
  def build_statement():
    pass