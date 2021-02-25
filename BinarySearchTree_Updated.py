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
            self.__insertData(data,self.start)

    def __insertData(self,data,curr):
        if(data<curr.data):
            if(curr.left==None):
                curr.left=Node(data)
            else:
                self.__insertData(data,curr.left)
        elif(data>curr.data):
            if(curr.right==None):
                curr.right=Node(data)
            else:
                self.__insertData(data,curr.right)
        else:
            print("The data can not be duplicated !!")
    
    def InOrderTraverse(self):
        if(self.start==None):
            print("There is no data to print")
        else:
            self.__printDT(self.start)

    def __printDT(self,curr):
        if curr!=None:
            self.__printDT(curr.left)
            print(curr.data,end="  ")
            self.__printDT(curr.right)

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
            return self.__searchByNode(data,self.start)
    def __searchByNode(self,data,curr):
        if(data==curr.data):
            return True
        elif(data<curr.data):
            if(curr.left==None):
                return False
            else:
                return self.__searchByNode(data,curr.left)
        else:
            if(curr.right==None):
                return False
            else:
                return self.__searchByNode(data,curr.right)

    def PreOrderTraverse(self):
        if self.start==None:
            print("BST is empty")
        else:
            self.__PreOrderTraverseLg(self.start)


    def __PreOrderTraverseLg(self,curr_node):
        if curr_node==None:
            return
        else:
            print(curr_node.data,end="  ")
            self.__PreOrderTraverseLg(curr_node.left)
            self.__PreOrderTraverseLg(curr_node.right)

    def PostOrderTraverse(self):
        if self.start==None:
            print("Binary Search Tree is empty")
        else:
            self.__PostOrderTraverse(self.start)

    def __PostOrderTraverse(self,curr_data):
        if curr_data==None:
            return 
        else:
            self.__PostOrderTraverse(curr_data.left)
            self.__PostOrderTraverse(curr_data.right)
            print(curr_data.data,end="  ")


    def DeleteNode(self,data):
        if(self.start==None):
            print("Binary Search Tree is Empty")
        else:
            node_side=""
            prev=self.start
            self.__DeleteNode(data,prev,self.start,node_side)
            
    def __MaximumToDelete(self,curr_data):    
        temp=curr_data
        while temp.right!=None:
            prev=temp
            temp=temp.right
        return prev,temp

    def __DeleteNode(self,data,prev,curr_node,node_side):
        if(curr_node.data==data):
            if(curr_node.left==None and curr_node.right==None):
                if(node_side=="right"):
                    prev.right=None
                else:
                    prev.left=None 
            elif(curr_node.left!=None and curr_node.right==None):
                prev.left=curr_node.left
            elif(curr_node.right!=None and curr_node.left==None):
                prev.right=curr_node.right
            else:
                parent,child=self.__MaximumToDelete(curr_node)
                curr_node.data=child.data
                parent.right=None
            print()
            print(f"{data} deleted successfully from the Binary seacrh tree")
        
        elif(data>curr_node.data):
            if(curr_node.right==None):
                print("No Data founf to delete")
                return
            else:
                self.__DeleteNode(data,curr_node,curr_node.right,"right")
        else:
            if(curr_node.left==None):
                print("No Data founf to delete")
                return
            else:
                self.__DeleteNode(data,curr_node,curr_node.left,"left")







        

          

bst1=BST()
### Adding data in in the Binary Tree
bst1.addData(10)
bst1.addData(7)
bst1.addData(4)
bst1.addData(9)
bst1.addData(12)
bst1.addData(15)
bst1.addData(11)

## Finding the maximum and minimum value of the binary search tree
print(f"Minimum value of the BST tree is {bst1.MinimumValue()}")
print(f"Maximum value of the BST tree is {bst1.MaximumValue()}")

# Searching data from the binary search tree
n=int(input("Enter a number which you want to seach in the binary search tree "))
res=bst1.Search(n)
if res:
    print(f"Yes {n} is in the Binary search tree")
else:
    print(f"No {n} is not in the Binary search tree")

# Traversing to Bianary Search Tree

print("InOrder method to traverse BST")
bst1.InOrderTraverse()
print()

print("PreOrder method to traverse BST")
bst1.PreOrderTraverse()
print()

print("PostOrder method to traverse BST")
bst1.PostOrderTraverse()

# bst1.DeleteNode(9)

# bst1.addData(2)
# bst1.DeleteNode(7)

bst1.DeleteNode(10)

print("InOrder method to traverse BST")
bst1.PreOrderTraverse()






