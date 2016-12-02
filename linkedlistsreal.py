class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None



 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x

      def LISTREMOVE(self,n):   ## create the function to remove a linked list
             if n.prev != 0:  ## if the previous node is not equal to 0
                   n.prev.next = n.next  ## make that node the next node in the list
             else:
                   l.head = n.next
             if n.next !=0:  ## if the next node in the list is not equal to 0
                   n.next.prev = n.prev ##make that node the next in the list
             else:
                   l.tail = n.prev


              
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
         
if __name__ == '__main__':
      l=List()
      n = Node(7)
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(6)) ## here i am removing node 6
      l.insert(l.head,Node(7)) ## here i added an extra node
      l.insert(l.head,Node(8)) ## here i removing node 8
      l.LISTREMOVE(l.head.next.next)## go to the frount of the linked list and remove the next node
      l.LISTREMOVE(l.tail.prev)## go to the end of the list (8) and remove the node previous
      l.display()

      ##the output is : List:4,6,8 as i have removed 6 and 8



      
      
