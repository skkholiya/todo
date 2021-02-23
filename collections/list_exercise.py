import random as rand
import itertools
import collections
#1 Write a Python program to sum all the items in a list. 

def sum_of_all_items(list1):
  total_sum = 0;
  for i in list1:
    total_sum += i;
  return total_sum


list1 = [-3,-23,-9,-12] 
print("sum of list items:",sum_of_all_items(list1)); #o/p -47


#2 Write a Python program to multiplies all the items in a list.

def multiplication_of_numbers(param):
  multiply = 1;
  for element in param:
    multiply *= element;
  return multiply
    
inp_list = [-12,-22,-5,-7]
print("multiplication of list items:",multiplication_of_numbers(inp_list)); #o/p 9240


#3 Get the largest number from a list

def get_largest(param):
  if len(param) == 0:
    return 1;
  largest = param[0];
  for i in range(1,len(param)):
    #checking if largest value > all the list items
    if(param[i] > largest):
      largest = param[i];
  return largest;
      
list2 = [-4,-15,-6,-6]
print("greatest value in list:",get_largest(list2)); #o/p -4



#4 Write a Python program to get the smallest number from a list.       
def smallest_in_list(arg):
  if len(arg) == 0:
    return 0;
  smallest = arg[0];
  for index in range(1,len(arg)):
    if arg[index] < smallest:smallest=arg[index];
  return smallest;  

list3 = [-34,2,-13,-1]
print("smallest in the list:", smallest_in_list(list3)); #o/p -34

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def count_match_value(sample_input):
  count = 0;
  for element in sample_input:
#checking if element length > 1 and first index value == last index value of the element.
    if len(element) >= 2 and element[0] == element[-1]:count +=1;
  return count;

sample_input =  ['abc', 'xyz', 'aba', '1221']
print("string (first == last) index value and length > 1 count:",count_match_value(sample_input)); #o/p 2

#6 Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

sample_inp = [(2, 5), (4, 4), (2, 3),(1, 2),  (2, 1)]
#sorted according to second item in the list of tuples.
sample_inp = sorted(sample_inp, key= lambda items:items[1])
print(sample_inp); #o/p [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#7 Remove Duplicate from list.
list_duplicate = [3,2,3,3,2,4,3]
without_duplicate = []
[without_duplicate.append(i) for i in list_duplicate if i not in without_duplicate]
print(without_duplicate)

#8 Check list is empty or not.
list_ex = []
result = True if len(list_ex) == 0 else False;
print("Is list empty?:", result);

#9 Write a Python program to clone or copy a list.
org_list = [1,2,3,4,5,3,3]
clone_org_list = org_list[:]
print("cloned list:", clone_org_list)

#10 Write a Python program to find the list of words that are longer than n from a given list of words.
def string_to_list(elements,n):
  return [ item for item in elements.split(" ") if len(item) > n ]
txt="The quick brown fox jumps over the lazy dog";
n =3
print(string_to_list(txt,n)) #['quick', 'brown', 'jumps', 'over', 'lazy']

#Write a Python function that takes two lists and returns True if they have at least one common member.
fruits = ["apple","banana","cherry"]
companies = ["microsoft","facebook"]

def any_common(list1,list2):
  for element in list2:
    if element in list1:
      return True;
  return False;
    
print(any_common(fruits,companies))    
    
#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
org_list= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def remove_specified_index_elements(eg_list):
  eg_list = [y for x,y in enumerate(eg_list) if x not in (0,4,5)]
  return eg_list;

print(remove_specified_index_elements(org_list));
'''

[[['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*']]
,[['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*']],
 [['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*']]]


[[['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*']], 
 [['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*']], 
 [['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*'], 
 ['*', '*', '*', '*', '*', '*']]]
'''

#13 generate 3*4*6 3D array.
generate_3d_array = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
print(generate_3d_array);

#14 Write a Python program to print the numbers of a specified list after removing even numbers from it.
original_list = [1,2,3,4,5,6,7,8,9]
original_list = [element for element in original_list if element%2!=0]
print("after removing even numbers:", original_list); #o/p [1, 3, 5, 7, 9]

#15 Write a Python program to shuffle and print a specified list.
list_string = ["apple","HCL","Microsoft","TCS","Google"]
rand.shuffle(list_string);
print("shuffled list:",list_string);

#16  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
square_list = [x**2 for x in range(1,31)]
print("first five square's",square_list[:5]);
print("last five square's",square_list[-5:]);

#17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
square_list = [x**2 for x in range(1,31)]
print("square except first 5 elements:", square_list[5:])

#18.  Write a Python program to generate all permutations of a list in Python.
given_input = [1,2,3]
permutation_list = list(itertools.permutations(given_input));
print(permutation_list);

#19. Write a Python program to get the difference between the two lists.
list1= [1,3,5,7,9]
list2= [1,2,4,6,7,8]
def difference_of_two_list(list1,list2):
  difference_list = []
  [difference_list.append(l1) for l1 in list1 if l1 not in list2]
  [difference_list.append(l2) for l2 in list2 if l2 not in list1]
  return difference_list;
  
print(difference_of_two_list(list1,list2));

#20. Write a Python program access the index of a list.
index_list = [1,2,4,6,7,8]
for index,element in enumerate(index_list):
  print("index:",index," ", "element:", element);
print()

#21. Write a Python program to convert a list of characters into a string.
list_of_string = ['g','o','o','g','l','e']
list_to_string = "".join(list_of_string)
print(list_to_string);

#22. Write a Python program to find the index of an item in a specified list. 
list_find_index = [1,2,3,4,5,6,4,3,4]
element = 4;
get_index = list_find_index.index(element);
print("element",element,"index is",get_index);

#23. Write a Python program to flatten a shallow list.
flatten_list = [[2,3,4],[1,5,6],[9],[7,9,0]]
res_flatten_list = [element for sub_list in flatten_list for element in sub_list]
print(res_flatten_list);

#24. Write a Python program to append a list to the second list.
eg_list1 = [1,2,3,4,5]
eg_list2 = [6,7,8,9,10]
final_list = eg_list1+eg_list2;
print(final_list)

#25. Write a Python program to select an item randomly from a list.
list_index = [1,2,3,4,5,6,7]
x = rand.choice(list_index)
print(x);

#26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print(' '.join(map(str, list2)) in ' '.join(map(str, list1*2)));
print(' '.join(map(str,list2)) in ' '.join(map(str,list1*2)));

#27. Write a Python program to find the second smallest number in a list.
def second_smallest_list(arr):
  if len(arr)<2:
    return
  if ((len(arr)==2)  and (arr[0] == arr[1]) ):
    return
  smallest = arr[0]
  second_smallest = 0;
  for i in range(1,len(arr)):
    if smallest>arr[i]:
      second_smallest = smallest;
      smallest = arr[i]
    elif second_smallest>arr[i]:
      second_smallest = arr[i];
  return second_smallest;
arr = [34,99,-3,-4,32,-11,90]
print("second smallest:",second_smallest_list(arr));

#28. Write a Python program to find the second largest number in a list.
def second_largest_list(arr):
  if len(arr)<2:
    return
  if ((len(arr)==2)  and (arr[0] == arr[1]) ):
    return
  largest = arr[0]
  second_largest = 0;
  for i in range(1,len(arr)):
    if largest<arr[i]:
      second_largest = largest;
      largest = arr[i]
    elif second_largest<arr[i]:
      second_largest = arr[i];
  return second_largest;
arr = [34,99,-3,-4,32,-11,90]
print("second largest",second_largest_list(arr));

#29. Write a Python program to get unique values from a list.
extract_unique_values = [10, 20, 30, 40, 20, 50, 60, 40]
unique_array = list(dict.fromkeys(extract_unique_values));
print(unique_array);


#30. Write a Python program to get the frequency of the elements in a list.
get_frequency = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
obj = dict(collections.Counter(get_frequency))
print(obj); #o/p {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

