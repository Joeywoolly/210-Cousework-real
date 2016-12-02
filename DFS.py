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
