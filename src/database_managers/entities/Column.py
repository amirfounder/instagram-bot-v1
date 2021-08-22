from dataclasses import dataclass


@dataclass
class Column:
  name: str
  data_type: str
  key: str
  auto_increment: bool = False
  not_null: bool = False
