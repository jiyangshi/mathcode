#coding: utf-8


def nameScores(name):
    Sum = 0
    for char in name:
        Sum += (ord(char) - 64)
    return Sum


files = open('names.txt')
line  = files.readlines()
lines = line[0].split(',')
# Sum: To store the total of all name scores
# Count: To mark the number of all names
Sum   = 0
Count = 1
names = []
for item in lines:
    names.append(item.split('"')[1])

names.sort()
for name in names:
    Sum  += (nameScores(name) * Count)
    Count = Count + 1
print("Sum: %d\n " %Sum)
