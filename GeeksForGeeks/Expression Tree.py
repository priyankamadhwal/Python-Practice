class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        
''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
# function should return an integer denoting the required answer
def evalExpressionTree(root):
    if not isOperator(root.data):
        return root.data
    return str(eval(evalExpressionTree(root.left) + root.data + evalExpressionTree(root.right)))

def isOperator(c):
    return (c=='+' or c=='-' or c=='*' or c=='/')
    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        q = []
        p = 0
        root = node(arr[p])
        q.append(root)
        p = 1
        while q!=[]:
            f = q.pop(0)
            l = node(-1)
            r = node(-1)
            if (p!=n):
                l.data = arr[p]
                f.left = l
                p+=1
                l.left = l.right = None
                q.append(l)
            else:
                f.left=None
            if p!=n:
                r.data = arr[p]
                f.right = r
                p+=1
                q.append(r)
                r.left = r.right = None
            else:
                f.right = None
        # inorder(root)
        # print ''
        print(evalExpressionTree(root))
# Contributed By: Harshit Sidhwa

