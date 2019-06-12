'''
Given a N x N binary matrix A where each row and column of the matrix is sorted in ascending order.
Your task is to complete the function  countZero which returns the count of  number of 0s present in it.
'''

{
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k+=1
        print (countZeroes(matrix, n))
}
''' This is a function problem.You only need to complete the function given below '''
# You are required to complete this fucntion
# Function should return the an integer
def countZeroes(arr, n):
    # Code here
    count = 0
    for i in range(n):
        count += arr[i].count(0)
    return count
