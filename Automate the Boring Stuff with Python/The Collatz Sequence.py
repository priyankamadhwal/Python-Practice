def collatz(number):
    if number%2 == 0: return number//2
    else: return 3*number + 1
print('Hello user!')
while True:
    try:
        number = int(input("Enter any positive number : "))
        if number <= 0 : print('The number should be greater than 0.')
        else: break
    except:
        print('The number should be an integer greater than 0.')
while number!=1:
    number = collatz(number)
    print(number)
