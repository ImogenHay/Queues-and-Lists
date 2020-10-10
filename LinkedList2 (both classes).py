## LINKED LIST ##


## Node Class ##

class Node(object): #contains each item and its pointer
   ## Constructor
   def __init__(self,item,pointer=None): #pointer initially always points to nothing
        ## Attributes
       self.item = item #the item being added
       self.pointer = pointer #which node to go to after current one

    ## Method
   def getNextNode(self): #returns the next node in the sequence
       return self.pointer





       
## Linked List ##

class LinkedList(object): #creates the nodes and keeps track of size and first node
    ## Constructor
   def __init__(self,first=None): #initially no first item
       self.first = first
       
    ## Methods
   def addNode(self,item):
       newNode = Node(item,self.first)#currently puts new nodes at the start of list
       self.first = newNode
       return "Node Added"
       
   def printNode(self):
       current = self.first #current node is last added node (which is first in list)
       while current: #repeats until there are no more nodes in sequence
           print(current.item) #prints current nodes item
           current = current.getNextNode() #changes current node to next node in sequence 




## Main Program ##
aList = LinkedList() #creates linked list called alist
print(aList.addNode(6)) #creates nodes
print(aList.addNode(18))
print(aList.addNode(24))

print("Nodes:") #prints list of nodes in order
aList.printNode()


input("\n\nPress the enter key to exit.") #end program
