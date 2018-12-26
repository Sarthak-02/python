class Node:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode
    
    def getData(self):
        return self.data
    
    def getNextNode(self):
        return self.nextNode
    
class LinkedList:
    
    def __init__(self,head=None):
        self.head = None
        self.size=0
        
    def getSize(self):
        return self.size
    
    def addNode(self,data):
        newNode = Node(data,self.head)
        #newNode = self.head
        self.head = newNode
        self.size +=1
        return True
    
    def deleteNode(self):
        curr = self.head
        curr = curr.getNextNode()
        self.head = curr
        return True
    
    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()
            
            
            
myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
myList.printNode()             
