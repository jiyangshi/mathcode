#coding: utf-8

with open('problem013.txt') as files:
    Sum   = 0
    lines = files.readlines()
    for line in lines:
        Sum += int(line)

print (str(Sum)[0:10])
