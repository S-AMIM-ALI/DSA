class Graph:
    def __init__(self,vno):
        self.v_count=vno
        self.adj_list={v:[] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.v_count and 0<=v<self.v_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("invalid vertex")
    def remove_edge(self,u,v):
        if 0<=u<self.v_count and 0<=v<self.v_count:
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("invalid vertex")
            return False
    def has_edge(self,u,v):
        if 0<=u<self.v_count and 0<=v<self.v_count:
            return any(vertex==v for vertex,weight in self.adj_list.items())
        else:
            print("invalid vertex")
            return False
    def print_adj_list(self):
        for vertex,x in self.adj_list.items():
            print(f'{vertex} is {x}')
g = Graph(4)

# Add edges
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 5)
g.add_edge(1, 3, 7)

print("Graph after adding edges:")
g.print_adj_list()

# Check edges
print("\nChecking edges:")
print("0-1:", g.has_edge(0, 1))
print("0-3:", g.has_edge(0, 3))

# Remove edge
g.remove_edge(0, 1)

print("\nGraph after removing edge 0-1:")
g.print_adj_list()

