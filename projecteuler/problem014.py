#coding: utf-8

alist = list(range(2, 101))

for item in alist:
    while item <> 1:
        if item%2 == 0:
            item /= 2
        else:
            item = 3 * item + 1
        if item in alist:
            alist.remove(item)
print (alist)
