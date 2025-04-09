import random
def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end= ' ')
        print()
        
n = 3
m = 3
array = []
sum = 0

for i in range(n):
    array.append([])
    for j in range(m):
        array[i].append(random.randint(2,8))
printList(array)

for i in range(n):
    for j in range(m):
        if i == j:
            sum = sum + array[i][j]**2
print(sum)
