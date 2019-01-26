for _ in range(int(input())):
    grade = int(input())
    if grade >= 38:
        nextMultiple5 = (grade//10)*10+[0,5,5,5,5,5,10,10,10,10][grade%10]
        diff = nextMultiple5 - grade
        if diff < 3 : grade = nextMultiple5
    print(grade)
