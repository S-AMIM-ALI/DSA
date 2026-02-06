class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_mat=[[0]*vno for e in range(vno)]
    def add_edge(self,u,v,w=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_mat[u][v]=w
            self.adj_mat[v][u]=w
        else:
            print("invalid syntax")
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_mat[u][v]=0
            self.adj_mat[v][u]=0
        else:
            print("inavlid syntax")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_mat[u][v]
        else:
            print("invalid edges")
    def display(self):
        for row_list in self.adj_mat:
            print(" ".join(map(str,row_list)))
g=Graph(5)


g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3,5)

g.display()



