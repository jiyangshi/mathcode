#coding: utf8

def cubicPermutations(nr):
    result      = float('inf')
    dictionary1 = {}
    dictionary2 = {}
    for i in range(1000, 10000):
        num    = i**3
        string = ''.join(sorted(str(num)))
        if dictionary1.has_key(string):
            dictionary1[string] += 1
        else:
            dictionary1[string]  = 1
            dictionary2[string]  = num
    for key in dictionary1.keys():
        if dictionary1[key] == nr:
            if result > dictionary2[key]:
                result = dictionary2[key]
    return result


if __name__ == '__main__':
    print cubicPermutations(5)
