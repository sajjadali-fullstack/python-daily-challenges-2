
# Write a Python program to input room numbers, count the frequency of each room,
# and print the room number that occurs only once.

k = int(input("Enter group size (K): "))
rooms = list(map(int, input("Enter room numbers: ").split()))
room_count = {}

for rno in rooms:
    if rno in room_count:
        room_count[rno] += 1
    else:
        room_count[rno] = 1
for rno, count in room_count.items():
    if count == 1:
        print(rno)