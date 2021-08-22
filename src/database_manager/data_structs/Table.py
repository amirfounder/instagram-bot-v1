from dataclasses import dataclass


@dataclass
class Table:
  name: str
  columns: list = None