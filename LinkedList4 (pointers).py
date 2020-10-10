## LINKED LIST ##


## Node Class ##

class Node(object): #contains each item and its pointer
   ## Constructor
   def __init__(self,item,pointer=None): #pointer initially always points to nothing
        ## Attributes
       self.item = item #the item being added
       self.pointer = pointer #which node to go to after current one

    ## Methods
   def getItem(self): #returns current item
       return self.item

   def setItem(self,value): #sets current item
       self.item = value

   def getNextNode(self): #returns the next node in the sequence
       return self.pointer

   def setNextNode(self,value): #sets the pointer of the node to determine what will be after it in the list 
       self.pointer = value



       
## Linked List ##

class LinkedList(object): #creates the nodes and keeps track of size and first node
    ## Constructor
   def __init__(self,first=None): #initially no first item
       self.first = first
       self.size = 0
       self.items = []
        
    ## Methods
   def getSize(self):
       return self.size #size used to work out next free position

   def addNode(self,item):
       self.items.append(item)
       self.items.sort()
       index = self.items.index(item)
       print(index)
       newNode = Node(item,self.first)#currently puts new nodes at the start of list, makes it point to the last item added
       self.first = newNode
       self.size += 1
       return "Node Added"

   def orderNodes(self):
       self.items.sort()
       current = self.items[0]
       x = 1
       while current:
          current.setNextNode(x)
          x = x + 1
       
   def printNode(self):
       current = self.first #current node is last added node (which is first in list)
       while current: #repeats until there are no more nodes in sequence
           print(current.item) #prints current nodes item
           current = current.getNextNode() #changes current node to next node in sequence 




## Main Program ##
           
aList = LinkedList() #creates linked list called alist
print(aList.addNode(18)) #creates nodes
print(aList.addNode(6))
print(aList.addNode(24))
aList.orderNodes()
print("Nodes:") #prints list of nodes in order
aList.printNode()
print("\nList Size:") #prints size of the list (total number of nodes)
print(aList.getSize())

input("\n\nPress the enter key to exit.") #end program
