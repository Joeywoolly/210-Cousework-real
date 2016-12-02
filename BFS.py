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
