from collections import namedtuple
N, Student = int(input()), namedtuple('Student',','.join(input().split()))
totalMarks = sum([int(Student(*input().split()).MARKS) for _ in range(N)])
print('{0:.2f}'.format(totalMarks/N))
