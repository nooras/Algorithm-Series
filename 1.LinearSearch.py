# Linear Search

# Date : 19/10/2020

'''

Linear search is used on a collections of items. It relies on the technique of traversing a list from start to end by exploring properties of all the elements that are found on the way.

For example, consider an array of integers of size . You should find and print the position of all the elements with value . Here, the linear search is based on the idea of matching each element from the beginning of the list to the end of the list with the integer , and then printing the position of the element if the condition is `True'.

Implementation:

The pseudo code for this example is as follows :

for(start to end of array)
{
    if (current_element equals to 5)  
    {
        print (current_index);
    }
}

Time Complexity:

The time complexity of the linear search is O(N) because each element in an array is compared only once.

'''

# Write your code here
n, find = map(int, input().split())
li = list(map(int, input().split()[:n]))
temp = -1
for x in range(len(li)):
	if li[x] == find:
		temp = x + 1
print(temp)