#xc1 reverse alist in pyton
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

i = 0
while i < len(list1):
    for item in list2:
        list1[i]+=item 
        i = i+1

print(list1)

#Exercise 3: Turn every item of a list into its square
#even used that weird 1 line loop format
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [i*i for i in numbers]
print(res)

#Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [i+j for i in list1 for j in list2 ]
print(list3)

#exercise 10: Remove all occurrences of a specific item from a list
list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)

#Exercise 7: Add new item to list after a specified item
#add 7000 after 6000
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

#Exercise 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

#print(list1[2][1][2]) This is tryna attempt to find the correct indexing for where 
#to place the hij sublist

# sub list to add
sub_list = ["h", "i", "j"]

for item in sub_list:
    list1[2][1][2].append(item)

print(list1)

#exercise 9: Replace list’s item with new value if found only first occurence
#the version below works using a while loop however a faster way would be to use the python .index(20) option
list5 = [5, 10, 15, 20, 25, 50, 20]

i =0
while i < len(list5):
    if list5[i] == 20:
        list5[i] = 200
        break
    i = i+1
print(list5)

#Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

#Exc 1Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#function returns a zip object, which is an iterator of tuples where 
#the first item in each passed iterator is paired together
#thenthe second item in each passed iterator are paired together etc.
my_dict = dict(zip(keys, values))
print(my_dict)

# ex2 Merge two Python dictionaries into one
# use the .copy() method
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

d3 = dict1.copy()
d3.update(dict2)
print(d3)