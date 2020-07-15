from util import Stack, Queue 
class Graph:

    def __init__(self):
        self.vertices = {}


    # Add verts
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()     # an empty set of edges, from this vert

    # Add edges
    # This adds a edge in one direction
    def add_edge(self, v1, v2):
        
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)   # add v2 as a neigbor to v1
        else:
            raise IndexError(f"Can not create edge between {v1} and {v2}")


    # Get neighbors for a vert
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    # For pairs(parent,child) in ancestor
    for pair in ancestors:
        # Add a vertices
        graph.add_vertex(pair[0])   
        graph.add_vertex(pair[1])           
        graph.add_edge(pair[1],pair[0])

    q = Queue()
    visited = set()

    longest_path = 1
    parent_end = -1

    q.enqueue([starting_node])

    while q.size() > 0:

        path = q.dequeue()
        vertex = path[-1]

        if len(path) >= longest_path and vertex < parent_end or len(path) > longest_path:
            parent_end = vertex
            visited.add(vertex)

        for neighbor in graph.vertices[vertex]:
                new_path= path.copy()
                new_path.append(neighbor)
                q.enqueue(new_path)

    return parent_end

