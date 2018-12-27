K, rooms = int(input()), list(map(int,input().split()))
distinctRooms = set(rooms)
print((sum(distinctRooms)*K - sum(rooms)) // (K-1))
