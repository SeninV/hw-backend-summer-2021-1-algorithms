from typing import Any

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
        return None



a = Node('a')
b = Node('b')
c = Node('c')
a.point_to(b)
b.point_to(c)
a.point_to(c)

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')
# k = Node('k')
# a.point_to(b)
# b.point_to(c)
# c.point_to(d)
# d.point_to(a)
# b.point_to(d)
# a.point_to(e)
# e.point_to(f)
# e.point_to(g)
# f.point_to(i)
# f.point_to(h)
# g.point_to(k)

g = Graph(a)
print(g.dfs())


        # assert dfs_values(g) == ['a', 'b', 'c']

e = {1 , 3 , 4}

q = {2, 5, 1}

