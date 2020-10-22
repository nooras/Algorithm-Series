'''
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/submissions/

Date : 22/10/2020
'''
a=[]

b=[]

n=int(input())

x=list(map(int,input().split()))

k=0

for i in x:

if i>=0:

a.append(i)

k+=1

else:

b.append(i)



 

if sum(a)>0:

print(sum(a),end=" ")

print(k)

elif sum(b)<0:

print(max(b),end=" ")

print(1)

elif sum(a)==0:

print(0,1)
