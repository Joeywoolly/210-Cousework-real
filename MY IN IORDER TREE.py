def IN_ORDER(self, val):
        currentRoot = self.root
        while (currentRoot != None and currentRoot.get() != val):
            if val < currentRoot.get():
                currentRoot = currentRoot.leftChild
            else:
                currentRoot = currentRoot.rightChild
                
       	if currentRoot == None:
            return False
        else:
            return True
