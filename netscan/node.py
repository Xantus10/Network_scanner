from __future__ import annotations

class Node:
  def __init__(self, serial_number: str, hostname: str, interfaces: dict[str, str]) -> None:
    self.serial_number = serial_number
    self.hostname = hostname
    self.interfaces = interfaces
    self.neighbors: list[Node] = []
  
  def add_neighbor(self, node: Node):
    if not node in self.neighbors:
      self.neighbors.append(node)

  def __eq__(self, value: object) -> bool:
    if value.__class__.__name__ == 'Node':
      return self.__hash__() == value.__hash__()
    raise TypeError(f'The __eq__ operator is not defined for classes of {self.__class__.__name__} and {value.__class__.__name__}')

  def __hash__(self) -> int:
    return int.from_bytes(self.serial_number.encode('utf-8'))
