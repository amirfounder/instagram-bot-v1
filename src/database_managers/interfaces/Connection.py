from abc import ABCMeta, abstractmethod
from typing import Any


class Connection(metaclass=ABCMeta):

  @abstractmethod
  def connect(self, host, user, password, database) -> None:
    pass

  @abstractmethod
  def close(self) -> None:
    pass

  @abstractmethod
  def execute(self, query) -> Any:
    pass