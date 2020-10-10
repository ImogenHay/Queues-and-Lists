## LINKED LIST (node)##

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None #pointer initially points to nothing

    def __str__(self):
        report = "Items: " + str(self.item) + "\n"
        report = report + "\n"       
        return report  


node1 = Node("Mon") 
node2 = Node("Wed") 
node3 = Node("Tue") 
node1.next = node3 
node3.next = node2 
print(node1)

input("\n\nPress the enter key to exit.") #end program
