'''
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
'''

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i*i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6
  
    return True

for _ in range(int(input())):
    print('Yes' if isPrime(int(input())) else 'No')
