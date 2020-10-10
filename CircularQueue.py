## CIRCULAR QUEUE ##

class CircularQueue(object): #class that always appends items to back of list and proccess them from the front to the back, once processed they move to the back like a circle
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
        
    def addItem(self,item):
        self.qList.append(item) #adds item to back of list
        return self.qList

    def getItem(self):
        item = self.qList.pop(0) #removes first item from list and returns it to process
        self.qList.append(item) #after it is removed from front of list it is sent to the back 
        return item     

    def getLength(self):
        length = len(self.qList) #finds length of list
        return length
    def emptyList(self):
        length = len(self.qList)
        for i in range(0,length):
            self.qList.pop(0)   #method that emptys list


##Adding items to queue
size = int(input("Max List Size: ")) #user input size of list
q1 = CircularQueue(size) #creates object with list of maxsize 'size'
length = 0 

while length < size-1: #repeats for each item there can be in list, then starts proccessing once list is full
    length = q1.getLength() #gets length of list
    item1 = input("Input Item: ") #user inputs item they want to add to list
    q1.addItem(item1) #adds item to back of list
text = q1.isFull() #prints text stating list is full
print(text)
print(q1)


##Processing items from queue
choice = 'no'
while choice == 'no':
        item = q1.getItem() #getItem functions uses pop to remove first item from list then moves to back
        print("Processed",item) #prints processed item
        choice = input("Do you want to stop processing? yes/no ")#its on a loop because its a circle to needs to ask when to stop
    
q1.emptyList() #runs function emptying list if want to stop processing
text = q1.isEmpty() #prints text stating list is empty
print(text)

input("\n\nPress the enter key to exit.") #end program
