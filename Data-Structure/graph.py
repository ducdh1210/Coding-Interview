from collections import defaultdict


# Imagine a graph as a social network where people (vertices) are connected by friendships (edges)
class Graph:
    def __init__(self):
        # We use a defaultdict to automatically create an empty list for new friends
        # Think of this as everyone starting with an empty friends list
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Adding a friendship: u becomes friends with v
        self.graph[u].append(v)

    def remove_edge(self, u, v):
        # Removing a friendship: u unfriends v
        if v in self.graph[u]:
            self.graph[u].remove(v)

    def has_edge(self, u, v):
        # Checking if a friendship exists: Is v in u's friend list?
        return v in self.graph[u]

    def get_vertices(self):
        # Getting all people in the network
        return list(self.graph.keys())

    def get_edges(self):
        # Getting all friendships in the network
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                edges.append((u, v))
        return edges

    def bfs(self, start):
        # Breadth-First Search: Exploring friends level by level
        # Imagine throwing a party and inviting friends, then friends of friends, and so on
        visited = set()  # People already invited
        queue = [start]  # People to invite next
        visited.add(start)
        result = []  # Order of people invited
        while queue:
            person = queue.pop(0)  # Invite the next person
            result.append(person)
            for friend in self.graph[person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)  # Add their friends to invite later
        return result

    def dfs(self, start, visited=None):
        # Depth-First Search: Exploring one friendship chain to its end before backtracking
        # Imagine tracing a family tree, going deep into one branch before exploring others
        if visited is None:
            visited = set()
        result = []

        def dfs_util(v):
            visited.add(v)  # Mark this person as visited
            result.append(v)  # Add to our exploration path
            for friend in self.graph[v]:
                if friend not in visited:
                    dfs_util(friend)  # Recursively explore this friend's connections

        dfs_util(start)
        return result

    def display(self):
        # Displaying the entire social network
        for person in self.graph:
            print(f"{person}: {self.graph[person]}")  # Person: [list of friends]


# Test code
if __name__ == "__main__":
    graph = Graph()

    print("Adding friendships to the social network:")
    friendships = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
    for u, v in friendships:
        graph.add_edge(u, v)
        print(f"Added friendship: {u} is now friends with {v}")

    print("\nSocial network representation:")
    graph.display()

    print("\nPeople in the network:", graph.get_vertices())
    print("All friendships:", graph.get_edges())

    print("\nRemoving friendship between 2 and 3")
    graph.remove_edge(2, 3)
    graph.display()

    print("\nChecking if friendship exists:")
    print("Are 0 and 1 friends?", graph.has_edge(0, 1))
    print

    print("\nExploring friendships using BFS starting from person 0:")
    print(graph.bfs(0))

    print("\nExploring friendships using DFS starting from person 0:")
    print(graph.dfs(0))
