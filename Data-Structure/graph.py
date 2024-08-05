from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)

    def _dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            v = queue.popleft()
            print(v, end=" ")

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Usage example
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Depth First Traversal (starting from vertex 2):")
    g.dfs(2)
    print("\nBreadth First Traversal (starting from vertex 2):")
    g.bfs(2)
