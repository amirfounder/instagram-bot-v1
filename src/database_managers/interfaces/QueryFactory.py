from abc import ABCMeta, abstractmethod


class QueryFactory(metaclass = ABCMeta):

  @abstractmethod
  def build_select_query() -> str:
    pass