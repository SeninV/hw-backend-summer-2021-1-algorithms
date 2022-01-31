from typing import Any
from collections import deque


__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        a = self._root
        visited = [a]

        def dfs_node(point):
            x = point.outbound
            for i in x:
                visited.append(i)
                if set(i.outbound) - set(visited) != set():
                    dfs_node(i)
            return None
        dfs_node(a)
        otv = []
        for i in visited:
            if i not in otv:
                otv.append(i)

        return otv


    def bfs(self) -> list[Node]:
        a = self._root
        visited =  []
        visited.append(a)
        stack = deque([a])
        while stack:
            sosed = stack.popleft()
            for neighbour in sosed.outbound:
                if neighbour not in set(visited):
                    visited.append(neighbour)
                    stack.append(neighbour)

        return visited


