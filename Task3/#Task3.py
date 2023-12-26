#NODE CLASS
class Node:
    #CONSTRUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    #BASIC USER-DEFINED OPERATIONS OF NODE

    def updateData(self,data):
        self.data = data

    def setLink(self,link):
        self.link = link

    def removeLink(self):
        self.link = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.link

#LINKED LIST CLASS
class LL:
    #LL CONSTRUCTOR
    def __init__(self):
        self.head = None

    #ADD A NODE TO THE START OF THE LIST
    def addToStart(self,data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode

    #ADD A NODE TO THE END OF THE LIST
    def addToEnd(self,data):
        current = self.head
        if current is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            while current.getNext():
                current = current.getNext()
            current.setLink(tempNode)

    def clearList(self):
        self.head = None

    #GET THE LENGTH
    def count(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            return count

    #PUSH DATA INTO TOP OF STACK
    def push(self,data):
        self.addToStart(data)

    #POP DATA FROM THE TOP OF STACK
    def pop(self):
        if self.head is None:
            return "Stack is empty"
        tempNode = self.head
        self.head = tempNode.getNext()
        return tempNode
    
    #QUEUE DATA INTO END OF QUEUE
    def enqueue(self,data):
        self.addToEnd(data)

    #DEQUEUE DATA FROM FRONT OF QUEUE
    def dequeue(self):
        if self.head is None:
            return "Queue is empty"
        tempNode = self.head
        self.head = tempNode.getNext()
        return tempNode
    
    def displayList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(),end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        print()
        
def convertToArray(linked_list):
    array = []
    
    while linked_list.count() > 0:
            array.append(linked_list.pop().getData())
    
    linked_list.clearList()

    return array

def reverseList(original, reversed):
    while original.count() > 0:
        data = original.pop().getData()
        reversed.push(data)

    original.clearList()
    
# #Task3A        
# listA = LL()
# listA.push('P')
# listA.push('Y')
# listA.enqueue('T')
# listA.enqueue('H')
# listA.push('O')
# listA.enqueue('N')
# listA.displayList()
# print(listA.count())
# listA.pop()
# listA.dequeue()
# listA.pop()
# listA.displayList()
# print(listA.count())

# #Task3B
# listA = LL()
# listA.push('I')
# listA.enqueue('L')
# listA.enqueue('O')
# listA.enqueue('V')
# listA.enqueue('E')
# listA.push('C')
# listA.push('O')
# listA.push('D')
# listA.push('I')
# listA.push('N')
# listA.push('G')
# listA.displayList()
# arrayA = convertToArray(listA)
# listA.displayList()
# print(arrayA)

# #Task3c
# listA = LL()
# listB = LL()
# listA.push('I')
# listA.enqueue('A')
# listA.enqueue('M')
# listA.push('A')
# listA.enqueue('M')
# listA.enqueue('U')
# listA.enqueue('S')
# listA.enqueue('L')
# listA.enqueue('I')
# listA.enqueue('M')
# listA.displayList()
# reverseList(listA,listB)
# listA.displayList()
# listB.displayList()
