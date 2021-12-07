class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.start=None

    def addData(self,data): 
        if self.start==None:
            self.start=Node(data)
        else:
            self.insertData(data,self.start)

    def insertData(self,data,curr):
        if(data<curr.data):
            if(curr.left==None):
                curr.left=Node(data)
            else:
                self.insertData(data,curr.left)
        elif(data>curr.data):
            if(curr.right==None):
                curr.right=Node(data)
            else:
                self.insertData(data,curr.right)
        else:
            print("The data can not be duplicated !!")
    
    def printData(self):
        if(self.start==None):
            print("There is no data to print")
        else:
            self.printDT(self.start)

    def printDT(self,curr):
        if curr!=None:
            self.printDT(curr.left)
            print(curr.data)
            self.printDT(curr.right)

            # print(f"curr {curr} curr left {curr.data} curr right {curr.data}")
        else:
            return

    def MinimumValue(self):
        if self.start==None:
            print("BST is Empty")
        else:
            temp=self.start
            while temp.left!=None:
                temp=temp.left

            return temp.data

    def MaximumValue(self):
        if self.start==None:
            print("BST is Empty")
        else:
            temp=self.start
            while temp.right!=None:
                temp=temp.right

            return temp.data
    def Search(self,data):
        if(self.start=='None'):
            # print("BST is empty")
            return False
        else:
            return self.searchByNode(data,self.start)
    def searchByNode(self,data,curr):
        if(data==curr.data):
            return True
        elif(data<curr.data):
            if(curr.left==None):
                return False
            else:
                return self.searchByNode(data,curr.left)
        else:
            if(curr.right==None):
                return False
            else:
                return self.searchByNode(data,curr.right)

    def PreOrderTraverse(self):
        if self.start==None:
            print("BST is empty")
        else:
            self.PreOrderTraverseLg(self.start)


    def PreOrderTraverseLg(self,curr_node):
        if curr_node==None:
            return
        else:
            print(curr_node.data)
            self.PreOrderTraverseLg(curr_node.left)
            self.PreOrderTraverseLg(curr_node.right)

            print(f"last {curr_node.data}")

        

          

bst1=BST()

bst1.addData(10)
bst1.addData(7)
bst1.addData(4)
bst1.addData(9)
bst1.addData(12)
bst1.addData(15)
bst1.addData(11)

print("Python ---  Java")


bst1.printData()

print(f"Minimum value of the BST tree is {bst1.MinimumValue()}")
print(f"Maximum value of the BST tree is {bst1.MaximumValue()}")


res=bst1.Search(44)
print(res)


bst1.PreOrderTraverse()

