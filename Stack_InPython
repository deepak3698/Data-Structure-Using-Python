### LinkedList Program using python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None
    #Insert at the beginning of linked list
    def inserAtBegining(self,data):
        newNode=Node(data)
        newNode.next=self.start
        self.start=newNode
    #Insert at the last of the linked list
    def insertAtLast(self,data):
        newNode=Node(data)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            
    #Traverse of the linked list / View linked list
    def view(self):
        temp=self.start
        if(temp==None):
            print("empty")
        while temp!=None:
            print(temp.data)
            temp=temp.next
    
    #Delete from the beginning of the linked list

    def deleteFromBeg(self):
        if self.start==None:
            print("There is no Node in the linked list")
        else:
            self.start=self.start.next
    #Delete from the end/last of the linked list
    def deleteFromEnd(self):
        if(self.start==None):
            print("Linked list is empty")
        else:
            if(self.start.next==None):
                self.start=None
            else:
                temp=self.start
                prev=self.start
                while temp.next!=None:
                    prev=temp
                    temp=temp.next
                prev.next=temp.next
            
    #Insert at the specific position according to data in the linked list
    def insertAtTheMid(self,data,data1):  
        if(self.start.data==data):
            newNode=Node(data1)
            newNode.next=self.start
            self.start=newNode
        else:
            temp=self.start
            prev=self.start
            while temp.data!=data:
                if(temp.next==None):
                    break
                prev=temp
                temp=temp.next     
            if(temp.next==None and temp.data!=data):
                print("Link list is empty")
            else:
                newData=Node(data1)
                newData.next=temp
                prev.next=newData
    def insertByPosition(self,position):
        pass
    def deleteByPosition(self,position):
        pass
            
    #Delete from the specific position according to data in the linked list
    def deleAtTheMid(self,data):
        if(self.start.data==data):
            self.start=self.start.next
        else:
            temp=self.start
            prev=self.start
            while temp.data!=data:
                if(temp.next==None):
                    break
                prev=temp
                temp=temp.next     
            if(temp.next==None and temp.data!=data):
                print("No Match")
            else:
                prev.next=temp.next
    #Reverse of the linked list
    def reverseLinkedList(self):
        prev=None
        temp=self.start
        while temp.next !=None:
            val=temp.next
            temp.next=prev
            prev=temp
            temp=val
        temp.next=prev
        self.start=temp
    # def reverseLinkedList(self):
    #     prev=None
    #     temp=self.start
    #     while temp !=None:
    #         val=temp.next
    #         temp.next=prev
    #         prev=temp
    #         temp=val
    #     self.start=prev
    #Adding of the list in the lisnked list
    def addList(self,dataList):
        for data in dataList:
            self.insertAtLast(data)
    #Counting to the linked list / Lenght of the linked list
    def countLinkedList(self):
        count=0
        temp=self.start
        while(temp!=None):
            temp=temp.next
            count+=1
        print(f"The length of the Linked list is {count}")
    #Search data by position in the linked list
    def searchAtPosition(self,position):
        count=0
        temp=self.start

        while(temp!=None):
            if(count==position):
                print(temp.data)
                break
            temp=temp.next
            count+=1

    #Search by value in the linked list
    def searchByValue(self,data):
        count=0
        temp=self.start
        while(temp!=None):
            if(temp.data==data):
                print(f" {data} Found at position {count}")
            temp=temp.next
            count+=1



    


list1=LinkedList()

# list1.inserAtBegining(10)
# list1.inserAtBegining(30)
# list1.view()


list1.insertAtLast(12)
list1.insertAtLast(23)
list1.view()
print("After")
list1.reverseLinkedList()
list1.view()
print("Adding list")

list1.addList([26,27,28])
list1.view()
list1.countLinkedList()

list1.searchAtPosition(0)

list1.searchByValue(23)
# list1.insertAtTheMid(13,18)

# print("delete")
# # list1.deleteFromBeg()
# # list1.deleteFromEnd()
# list1.deleAtTheMid(23)
# list1.view()

# # list1.inserAtBegining(40)

# list1.view()
