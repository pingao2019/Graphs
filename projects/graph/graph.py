"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        
        self.vertices[vertex_id]= set() # this will hold edges


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)# there's an edge from v1 to v2 
        else:
            raise IndexError('nonexistent vert')


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        
        return self.verteces[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        q=Queue()
        visited=set()
        # Init: enqueue the starting node
        q.enqueue(starting_vertex)
        while q.size()> 0:
            #dequeue the item in queue
            v=q.dequeue()
            if v is not in visited:
                 
                visited.add(v)
                print(f"Visited{v}")
                #add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        s=Stack()
        visited=set()
        # Init: enqueue the starting node
        s.push(starting_vertex_id)
        while Stack.size()> 0:
            #remove the item in stack
            v=s.pop()
            if v is not in visited:
                visited.add(v)
                print(f"Visited{v}")
                #add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert

    def dft_recursive (self, starting_vertex, destination_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in self.visited:
            print(starting_vertex)
            self.visited.add(starting_vertex)
            for next_vert in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_vert)
         
             
        # print(f"Visited{v}")
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty..
        while q.size() > 0:

            # Dequeue the first PATH
            path= q.dequeue()

            # Grab the last vertex from the PATH
            last_vertex=path[-1]
            #if the vertex has not been visited.
            if last_vert is not in visited:
                visited.add(last_vertex)
                
                # CHECK IF IT'S THE TARGET
                if last_vertex= destination_vertex:
                    return path                  

                # Mark it as visited...
                else:
                    # Then add A PATH TO its neighbors to the back of the queue                   
                    for next_vert in self.net_neighbors(last_vertex):
                        # COPY THE PATH 
                        copy_path=list(path)
                        # APPEND THE NEIGHOR TO THE BACK
                        copy_path.append(next_vert)
                        q.enqueue(copy_path)


                  

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the stackis not empty..
        while s.size() > 0:

            # pop the first PATH
            path= s.pop()

            # Grab the last vertex from the PATH
            last_vertex=path[-1]
            #if the vertex has not been visited.
            if last_vert is not in visited:
                visited.add(last_vertex)
                
                # CHECK IF IT'S THE TARGET
                if last_vertex= destination_vertex:
                    return path                  

                # Mark it as visited...
                else:
                    # Then add A PATH TO its neighbors to the back of the stack                   
                    for next_vert in self.net_neighbors(last_vertex):
                        # COPY THE PATH 
                        copy_path=list(path)
                        # APPEND THE NEIGHOR TO THE BACK
                        copy_path.append(next_vert)
                        s.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited=set()
        if path is None:
            path=[]
            path.append(starting_vertex)
        if starting_vertex is not in visited:
            Visited.add(starting_vertex)
            if path[-1]=destination_vertex:
                return path
            for nxt_vert in self.get_neighbors:
                copy_path=list(path)
                copy_path.append(nxt_vert)
                nxt_path =self.dfs_recursive
                if nxt_path is not None:
                    return nxt_path
        else:
            return

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
