## PRIORITY QUEUE ##

class PriorityQueue(object): #class that proccesses items from front to back (removes after processed) but orders them in the list in order of priority
    ## Constructor
    def __init__(self, maxSize):

        print("A list has been created")

        ## Attributes
        self.maxSize = maxSize
        self.qList = []

        
    ## String Method - special method that will be called on print  
    def __str__(self):
        report = "\nQueue "
        report = report + "Max Size: " + str(self.maxSize) + "\n"

        if len(self.qList) > 0:
               report = report + "has the following Items\n"
               for i in self.qList:
                   report = report + str(i) + ", "
        report = report + "\n"       
        return report       

    ## Other Methods  
    def isFull(self):
        text = "No more items can be added\n"
        return text
        
    def isEmpty(self):
        text = "List is empty" 
        return text
        
    def addItem(self,item,priority): #adds item to list in order of priority
        if priority == 1:
            length = len(self.qList)
            self.qList.insert(length,item) #inserts at end of list if least priority
        elif priority == 3:
            self.qList.insert(0,item) #inserts at start of list if highest priority
        else:
            middle = len(self.qList)/2
            self.qList.insert(int(middle),item) #inserts at middle of queue if anything else priority

        return self.qList

    def getItem(self):
        item = self.qList.pop(0) #removes first item from list
        return item     

    def getLength(self):
        length = len(self.qList) #finds length of list
        return length
    
    def emptyList(self):
        length = len(self.qList)
        for i in range(0,length):
            self.qList.pop(0)   #method that emptys list by popping each item in list one by one


##Adding items to queue
size = int(input("Max List Size: ")) #user input size of list
q1 = PriorityQueue(size) #creates object with list of maxsize 'size'
length = 0
amount3 = 0
amount2 = 0

while length < size-1: #repeats for each item there can be in list
    length = q1.getLength() #gets length of list
    item1 = input("Input Item: ") #user inputs item they want to add to list
    priority1 = int(input("Input Priority (1-3 = least-most): ")) #selects priority within queue
#    if priority1 = 3:



    
    q1.addItem(item1,priority1) #adds item to back of list
text = q1.isFull() #prints text stating list is full
print(text)
print(q1)


##Processing items from queue
while length > 1: #repeats for each item in list
    length = q1.getLength() #find current length of list
    item = q1.getItem() #getItem functions uses pop to remove first item from list
    print("Processed ",item) #prints removed/processed item
text = q1.isEmpty() #prints text stating list is empty
print(text)

q1.emptyList() #runs function emptying list

input("\n\nPress the enter key to exit.") #end program
