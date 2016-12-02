class Node:
    def __init__(self,name):
        self.name = name
        #self.neighbour = None

    def __str__(self): 
        return self.name
    
class Graph:
    def __init__(self):
        self.dictionary = {}
    def addNode(self, name, connections):  ##want to add itself, the name of the node
        new_node = Node(name)               ## and who the node can talk too,
        self.connections = connections

        if(new_node.name not in self.dictionary): #stops the same 
            self.dictionary[new_node.name] = []#empty connection at the moment
        if connections != None:
            self.dictionary[new_node.name].append(self.connections)
            self.dictionary[self.connections].append(new_node.name)
        print(self.dictionary)


##goes through each of the nodes        
    def DFS(self,node):
        stack = []
        visited = []
        stack.append(node)
        while stack:
            temp = stack.pop()   ## removes and returns the last item 
            for n in self.dictionary[temp]:
                if n not in visited:
                    stack.append(n)  
            visited.append(temp)    ##every node that has been visited goes in visited 
            print('visited',temp)
        print( visited)
        print (temp)

#visits each node in turn, by finding the connections so in this case it will go from 1 to 3, 3 is connected to 2 
    def BFS(self,node):
        queue = []
        visited = []
        queue.append(node)
        while queue:
            temp = queue.pop(0)
            for n in self.dictionary[temp]:
                if n not in visited:
                    queue.append(n)  
            visited.append(temp)
            print('visited',temp)
        print( visited)

 
node = Graph()
node.addNode(1, None)
node.addNode(3, 1)
node.addNode(4, 1)
node.addNode(2, 3)
node.addNode(2, 4)




node.DFS(1)

node.BFS(1)
