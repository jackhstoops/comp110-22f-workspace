from __future__ import annotations

from typing import Union

class Node:
    data: int
    next: Union[Node, None]

    def __init__(self, data:init, next;Union[Node, None]):
        self.data = data
        self.next = next

    head: Node = Node(1, None)