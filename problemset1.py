#exc 2 print previous number current number and sum
for i in range(10):
    sum = i+(i-1)
    if i!= 0:
        print("current number is: ",i,"previous number is: ",i-1,"sum is: ",sum)
    else:
        print("current number is: ",i,"previous number is: 0","sum is: 0 ")

# exc 3 only printing even numbered strng indexes
user_str = input("enter a string")
counter = 0
for letter in user_str:
    if counter%2 == 0:
        print(letter)
    counter+=1

#exc 4 remove n characters from str
user_num = input("enter a number")
usr_str = input("enter a string: ")

user_num = int(user_num)
split_str = usr_str[user_num:]
print(split_str)

#exc 7 return the count of word/substr inside a string
substr = 'gun'
user_string = input("enter data: ")

the_count = user_string.count(substr)
print(the_count)

#ex8 loop pattern
for i in range(5):
    for j in range(i):
        print(i, end=" ")
    print("\n")

#str(n) == str(n)[::-1]
#A pythonic way to determine if a given value is a palindrome: ex9
number = 1012
number = str(number)
print(number[::-1])

#Exc 10 new list where odds from one list evens frm the other
list1=[10,20,25,30,35]
list2 = [40,45,60,75,90]
new_list = []

for item in list1:
    if item %2 != 0:
        new_list.append(item)

for x in list2:
    if x %2 == 0:
        new_list.append(x)

print("result list: ",new_list)

#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")

#Exc 12 income tax calculator
income = 45000
tax_total = 0
income_left = 0
if income <= 10000:
    tax_total = 0
elif income <= 20000:
    deduction = income-10000
    tax_total = 0.1*deduction

else:
    tax_total = 10000 * 10 / 100
    tax_total += (income - 20000) * 0.2

print("total tax to pay is: $",tax_total)

#Exercise 1B: Create a string made of the middle three characters
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JaSonAy")

#Exercise 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

mi = int(len(s1)/2)
x=s1[0:mi]
res = x+s2+s1[mi:]
print(res)

#Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
new_str = ""
lower_str=""
for letter in str1:
    if letter == letter.upper():
        new_str += letter
    else:
        lower_str = lower_str+ letter
print(lower_str+new_str)

#Exercise 5: Count all letters, digits, and special symbols from a given string
#instead of list of symbols use isdigit and isalpha and then else for shorter code
pword = "P@#yn26at^&i5ve"
special_symbols =["@","!","#","$","%","^","&","*"] 
letters = 0
symbol =0
digits =0
for chr in pword:
    if chr in special_symbols:
        symbol+=1
    
    elif chr.isdigit():
        digits +=1
    else:
        letters +=1

print("Total counts of chars, digits, and symbols ")
print("chars: ",letters," Digits: ",digits," symbols: ",symbol)

#Exercise 7: String characters balance Test
s1 = "Ynf"
s2 = "PYnative"

for item in s1:
    if item in s2:
        continue
    else:
        check = False

if check == True:
    print("True")
else: 
    print("False")

#Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
char_dict = {}
for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

#Python reverse string exc 11
str6 = "PYnative"
print("".join(reversed(str6)))

#exc 13 easy but 12 need help

#exc15 Remove special symbols / punctuation 
#string.punctuation contains all special symbols
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

#Exercise 16: Removal all characters from a string except integers
str9 = 'I am 25 years and 10 months old'
for item in str9:
    if item.isdigit() == False:
        
        str9 =str9.replace(item,'')

#Exercise 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

#Exercise 18: Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
for chr in str1:
    if chr in string.punctuation:
        str1 = str1.replace(chr,"#")

print(str1)

#xercise 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)




