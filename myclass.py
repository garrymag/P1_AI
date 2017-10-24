###################################################
# Projeto 1 AI 2017/2018                          #
# IST                                             #
# PEDRO SILVA                                     #
# ANDRE BAIAO                                     #
###################################################
#from implementation import*
import collections
class graph:
    def __init__(self):
        self.edges = {}
        self.weight = {}
        
    def neighbors(self,node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weight[(from_node + to_node)]

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def bfs(graph,start):
    front = Queue()
    front.put(start)
    visited = {}
    visited[start] = True

    while not front.empty():
        current = front.get()
        print ("visiting %r"%current)
        for nex in graph.neighbors(current):
            if nex not in visited:
                front.put(nex)
                visited[nex] = True


class node:
    #creates tree node
    def __init__(self,state,cost=0):#,parent = None, children = None):
        #set std value for state = void
        if state is None:
            self.state = []
        
        self.state = state
        self.cost = cost
        self.parents = []
        self.children = []
        
    def new_children(self,obj):
        self.children.append(obj)
        obj.parents.append(self)
        
        
###################################################
class launch(object):
    def __init__(self,date,max_load,cost,ucost):
        self.date = date
        self.max_load = max_load
        self.cost = cost
        self.ucost = ucost 
###################################################
class problem(object):
    #create problem obj
    def __init__(self,vertices=[],edges=[],launches=[]):
        
            
        self.vertices = vertices
        self.edges = edges
        self.launches = launches
###################################################
class module(object):
    
    def __init__(self,neme,mass):
        self.name = name
        self.mass = mass
        
