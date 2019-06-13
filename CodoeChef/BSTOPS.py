class Node:
    def __init__(self,data,pos):
        self.data = data;
        self.left = None;
        self.right = None;
        self.pos = pos;

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.insertHelper(self.root,1,data)
            
    def insertHelper(self,current,pos,data):
        if not current:
            current = Node(data,pos)
            print(pos)
            if pos==1:
                self.root = current
            return current
        elif data <= current.data:
            current.left = self.insertHelper(current.left,2*pos,data)
        else:
            current.right = self.insertHelper(current.right,2*pos+1,data)
            
    def delete(self,data):
        self.deleteHelper(self.root,data)
            
    def deleteHelper(self,current,data):
        if not current:
            return current
        if data < current.data:
            current.left = self.deleteHelper(current.left,data)
        elif data > current.data:
            current.right = self.deleteHelper(current.right,data)
        else:
            print(current.pos)
            #If both or one child is None
            if not current.right and not current.left:
                if current.pos==1:
                    self.root = None
                else:
                    current = None
                return None
            elif not current.left:
                temp = current.right
                current = None
                return temp
            elif not current.right:
                temp = current.left
                current = None
                return temp
            #If both child are not None
            #Replace with inorder successor-(leftmost in right subtree)
            temp = current.right
            while temp.left is not None:
                temp = temp.left
            current.data = temp.data
            current.right = self.deleteHelper(current.right,temp.data)

try:          
    Q = int(input())
    b = BST()   
    for _ in range(Q):
        query = input().split()
        x = int(query[1])
        if query[0]=='i':
            b.insert(x)
        elif query[0]=='d':
            b.delete(x)
except:
    pass
