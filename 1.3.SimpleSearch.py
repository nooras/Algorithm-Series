'''

https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/simple-search-4/submissions/

Date : 22/10/2020

'''
n = int(input())
a = list(map(int, input().split()))
k = int(input())

for x in range(n):
    if k == a[x]:
        print(x)
        break
