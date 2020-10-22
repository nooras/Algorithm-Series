# Easy Sum Set Problem

# Date : 20/10/2020

'''
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/
'''

a = int(input())
setA = list(map(int, input().split()[:a]))
c = int(input())
setC = list(map(int, input().split()[:c]))
setB = []
for x in range(len(setA)):
    for y in range(len(setC)):
        b = setC[y] - setA[x]
        xx = 0
        for z in range(len(setA)):
                temp = b + setA[z]
                if temp not in setC:
                        xx = 1
                        break
        if xx == 0 and b not in setB:
                setB.append(b)  
#print(setB)
for x in range(len(setB)):
        print(setB[x], end=" ")