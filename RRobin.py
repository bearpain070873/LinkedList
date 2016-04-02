'''
Created on April 1, 2016

@author: barry payne
'''
import random
import time

def generateProcess(idNum, TQ): #generate random numbers for process ID and time quantum
    if random.randint(1,5) == 5:
    #Long process
        length = random.randint(TQ,TQ+20)
    else:
    #short process
        length = random.randint(1,TQ)
    return [idNum, length]

class LinkNode:     #create node
    def __init__(self,pId,tLength):
        self.pId = pId
        self.tLength = tLength 
        self.next = next
        
    def getPid(self):
        return self.pId
    
    def getLength(self):
        return self.tLength

    def getNext(self):
        return self.next

    def setPid(self, pId):
        self.pId = pId
    
    def setTlength(self,tLength):
        self.tLength = tLength

    def setNext(self,newnext):
        self.next = newnext
        
    def tick(self):     #decrements the process time in the node
        self.tLength -= 1


class LinkedList:       #creates a linked list

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):      #formats output of linked list
        result = ""
        node = self.head
        while node != None:
            result += "[" + str(node.pId) + ":" + str(node.tLength) + "]"
            result += "->"
            if node.next is None:
                result = result[:-2]
            node = node.getNext()
        return result
        
    def __repr__(self):
        return self.__str__()

    def isEmpty(self):
        return self.head == None

    def add(self,prCss, pLength):       #adds node to front of linked list
        temp = LinkNode(prCss,pLength)
        temp.setNext(self.head)
        temp.setPid(prCss)
        temp.setTlength(pLength)
        self.head = temp
        
    def click(self):        #calls decrement module in node class
        self.head.tick()
        
    def size(self):     #determines size of linked list
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
    
        return count
    
    def append(self,prCss,pLength):     #appends node to end of linked list
        temp = LinkNode(prCss,pLength)
        temp.setPid(prCss)
        temp.setTlength(pLength)
        temp.setNext(None)
        if self.head == None:
            self.head = temp
        elif self.head != None and self.tail == None:
            self.tail = temp
            self.head.next = self.tail
        else:
            self.tail.setNext(temp)
            self.tail = temp
            
    def move(self,prCss,pLength):
        temp = LinkNode(prCss,pLength)
        temp.setPid(prCss)
        temp.setTlength(pLength)
        temp.setNext(None)
        if self.head == None:
            self.head = temp
        elif self.head != None and self.tail == None:
            self.tail = temp
            self.head.next = self.tail
        else:
            self.tail.setNext(temp)
            self.tail = temp
            self.head = self.tail
            
    def remove(self):
        temp = self.head.next
        self.head = temp    

def main():
    timeEnter=input("Enter the time quantum:")
    timeP = int(timeEnter)      #set time variable as an integer
    cCount=1
    lList = LinkedList()    #instantiate linked list
    rNum = 1    #instantiate random number variable
    while cCount <= 100:        #loop to keep program running
        lCount = lList.size()
        if lCount >= 1:
            rNum = random.randint(1,lCount)
        if rNum == 1:
            gProcess=generateProcess(cCount, timeP)     #instantiate new process
            pProcess=gProcess[0]    #call process number
            tProcess=gProcess[1]    #call process time
            cCount+=1
            lList.append(pProcess,tProcess)     #append to linked list
        pVar = "TQ:{timeP}  ".format(**locals())
        print(pVar,lList)
        time.sleep(1)       #slow down to make output more legible
        timeP-=1
        ttLength = lList.head.tLength   #variable to check process time
        lList.click()
        if cCount == 100:
            cCount = 0
        if timeP == 0 and ttLength >= 1:    #if time quantum runs out and process time available
            mPrcs = lList.head.pId
            mLnth = lList.head.tLength
            lList.append(mPrcs, mLnth)
            lList.remove()
            timeP = int(timeEnter)
            continue
        if ttLength <= 1 and timeP != 0:    #if process time runs out and time quantum is still available
            lList.remove()
            timeP = int(timeEnter)
            continue
        if ttLength <= 1 and timeP == 0:    #if process time and time quantum run out simultaneously
            lList.remove()
            timeP = int(timeEnter)
            continue
main()
