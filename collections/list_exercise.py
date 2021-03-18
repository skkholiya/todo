import random as rand
import itertools
import ast
import collections
import operator
import heapq
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


#31. Write a Python program to count the number of elements in a list within a specified range. 
def count_numbers(list_ex,start, end):
  count = 0;
  for i in list_ex:
    if i in range(start,end):  
      count+=1;
  return count;
list1 = [211,23,322,412,125,6,711,90]
print(count_numbers(list1,0,200));


#32. Write a Python program to check whether a list contains a sublist.
org_list = [3,4,5,3,2,4,6,3]
subset = [5,3,2,1]
isSubSet = " ".join(map(str,subset)) in " ".join(map(str,org_list))
#or
isSubsetUsingSet = set(subset).issubset(org_list);
print(isSubsetUsingSet);
print(isSubSet);

#33. Write a Python program to generate all sublists of a list.

def generate_sublists(x):
  return_list = [] 
  for i in range(0,len(x)+1):
    y = [list(j) for j in (itertools.combinations(x,i))] 
    if len(y)>0:
      return_list.extend(y)
  return return_list;
    
x=['x','y','z']
print(generate_sublists(x));

#34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
def sieve_of_eratosthenes(n):
  return_list = [True for i in range(n+1)];
  start = 2;
  while(start*start <= n):
    #finding multiple of the specified number.
    for i in range(start*start,n+1,start):
    #setting false, the multiple of the number.
      return_list[i] = False;
    start +=1;

  for i in range(2,n+1):
    if return_list[i]:
      print(i);

sieve_of_eratosthenes(10);

#35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
n=5;
st_list = ['p','q']
out_st_list = ["{}{}".format(i,j) for i in st_list for j in range(1,n)]
print(out_st_list);

#36. Write a Python program to get variable unique identification number or string. 
a=49993
print(format(id(a),"x"));

#37 Write a Python program to find common items from two lists. 
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2));

#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
'''Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
 '''
sample_input = [0,1,2,3,4,5]
def change_position(sample_input):

  for i in range(0,len(sample_input),2):
    temp = sample_input[i];
    sample_input[i]=sample_input[i+1]
    sample_input[i+1]=temp;  
    #sample_input[i],sample_input[i+1] = sample_input[i+1],sample_input[i];
  return sample_input

print(change_position(sample_input));
 

#39. Write a Python program to convert a list of multiple integers into a single integer.
sampl_list = [11, 33, 50] 
list_to_int =int("".join( [str(i) for i in sampl_list]))
print(type(list_to_int));

  
#40. Write a Python program to split a list based on first character of word.
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']  

def split_by_first_character(word_list):
     
  for letter,word in itertools.groupby(sorted(word_list), operator.itemgetter(0)):
    print(letter)
    for words in word:
      print(words);

split_by_first_character(word_list);

#41. Write a Python program to create multiple lists.
list_of_dict = {}
#creating list for first 10 positive numbers. i.e key=integer, value=list
for i in range(1,11):
  list_of_dict[i] = [];
print(list_of_dict);

#42. Write a Python program to find missing and additional values in two lists. 
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

missing_value_list2 = " ".join([i for i in list1 if i not in list2])
additional_value_list2 = " ".join([i for i in list2 if i not in list1])
print("missing value in list2:",missing_value_list2);
print("additional value in list2:",additional_value_list2);

#43. Write a Python program to split a list into different variables.
sample_list = ["steve jobs","Huston","python"]

person, city, language = sample_list

print(person,city,language)

#44. Write a Python program to generate groups of five consecutive numbers in a list.
generate_group = [ [i + j*5 for i in range(1,6)] for j in range(5)]
print(generate_group);




#45. Write a Python program to convert a pair of values into a sorted unique array.
pair_of_value = [(1,2), (3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
sorted_unique_array = list(set(j for i in pair_of_value for j in i))
print(sorted_unique_array)




#46. Write a Python program to select the odd items of a list.
list_of_object = [1,2,3,4,5,6,7,8,9]
odd_items = [i for i in list_of_object if i%2!=0]
print(odd_items);





#47. Write a Python program to insert an element before each element of a list.
ls_c = ["red","black","green"]
return_list_of_colors = [i for element in ls_c for i in ('c',element)]
print(return_list_of_colors);





#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
colors = [["RED"], ["GREEN"],["BLACK"]]
for i in colors:
  print(i);




#49. Write a Python program to convert list to list of dictionaries.
list_of_color = ["Black", "Red", "Maroon", "Yellow"]
color_code =  ["#000000", "#FF0000", "#800000", "#FFFF00"];
dict_colors = [{"color_name":k,"color_value":v} for k,v in zip(list_of_color,color_code)]
print(dict_colors);



#50. Write a Python program to sort a list of nested dictionaries. 
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

return_list = sorted(my_list, key=lambda x : x['key']['subkey'], reverse = True)
print(return_list)



#51. Write a Python program to split a list every Nth element.
n=3
list_split = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
return_listt = [[list_split[j] for j in range(i,len(list_split),n)] for i in range(n)]
print(return_listt);




#52. Write a Python program to compute the difference between two lists
color_list1 = ["red", "orange", "green", "blue", "white"];
color_list2 =  ["black", "yellow", "green", "blue"];

difference_list1 = set(color_list1).difference(set(color_list2));
print("difference in list1:",difference_list1);
difference_list2 = set(color_list2).difference(set(color_list1));
print("diffrence in list2:",difference_list2);



#53. Write a Python program to create a list with infinite elements.
x = itertools.count();
print(next(x));
print(next(x));
print(next(x));
print(next(x));
print(next(x));




#54. Write a Python program to concatenate elements of a list.
list_of_fruits = ["red", "orange" , "green"]

#concatenating with -
join_with_hyfen = " - ".join(list_of_fruits);
print(join_with_hyfen);
join_with_quote = ''.join(list_of_fruits);
print(join_with_quote);



#55. Write a Python program to remove key values pairs from a list of dictionaries.
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
remove_value = [ {k,v} for list_items in original_list for k,v in list_items.items() if k !='key1']
print(remove_value);




#56 Group of the age 30+ in the list of dictionary

list_of_dict = [{"first_name":"Zahir","last_name":"Khan","age":40,"Country":"India"},
		{"first_name":"Rashid","last_name":"Khan","age":34,"Country":"Afganistan"},
		{"first_name":"Parthiv","last_name":"Patel","age":35,"Country":"India"},
		{"first_name":"Aksar","last_name":"Patel","age":25,"Country":"India"},
		{"first_name":"Ben","last_name":"Strokes","age":29,"Country":"England"}]

return_age_30 = list(filter(lambda x:x.get("age")>=30,list_of_dict));

print(return_age_30)


#57. Write a Python program to convert a string to a list.
string_ex = "['Red', 'Green', 'White']"
string_list = ast.literal_eval(string_ex);
#This can be used for safely evaluating strings containing Python expressions from untrusted sources without the need to parse the values oneself.
print(type(string_list)); #o/p -class 'list'




#57. Write a Python program to check whether all items of a list is equal to a given string.
string_eg = "google"
list_of_com = ["google","apple","microsoft","facebook"]
result = all(string_eg == i for i in list_of_com)
print(result);



#58. Write a Python program to replace the last element in a list with another list.
lis1 = [1, 3, 5, 7, 9, 10]
lis2 = [2, 4, 6, 8]
lis1[-1:] = lis2;
print("58:",lis1);



#59. Write a Python program to check whether the n-th element exists in a given list.
list_of_int = [1,2,3,4,5,6,7,8,9]
len_x = len(list_of_int)-1;
if len(list_of_int)>0:print("59.",list_of_int[len_x])



#60.Write a Python program to find a tuple, the smallest second index value from a list of tuples.
list_of_tuples = [(1,2),(3,1),(5,6),(7,3),(9,2)]
list_of_tuples.sort(key = lambda x:x[1])
print("60:",list_of_tuples[0]);



#61. Write a Python program to create a list of empty dictionaries.
list_of_empty_dict = []
#list_of_empty_dict = [{} for _ in range(5)]
for i in range(3):
  list_of_empty_dict.append(dict());

print("61. ",list_of_empty_dict)




#62. Write a Python program to print a list of space-separated elements.
list_example = [1,2,3,4,5,6,7,8,9]
#print(*list_example)
for i in list_example:
  print(i,end=" ");
  

#63. Write a Python program to insert a given string at the beginning of all items in a list.
print();
sample_list = [1,2,3,4]
x=["emp{}".format(i) for i in sample_list]
print(x);



#64. Write a Python program to iterate over two lists simultaneously. 
list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d','e','f']

for l1,l2 in zip(list1,list2):
  print(l1,l2)




#65. Write a Python program to move all zero digits to end of a given list of numbers.

list_ex = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1];
list_ex.sort(reverse=True)
print("65",list_ex);




#66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
list_of_lists = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
highest_sum = list_of_lists[0];
for i in range(1,len(list_of_lists)):
  if sum(highest_sum) < sum(list_of_lists[i]):
    highest_sum = list_of_lists[i];

print("66. highest sum in list_of_lists:",highest_sum)




#67. Write a Python program to find all the values in a list are greater than a specified number. 
specified_number = 50;
list_int = [53,23,66,23,5,6,9]
return_lis = [i for i in list_int if specified_number<i]
print("67.",return_lis);


#68. Write a Python program to extend a list without append. 
lis1 = [10, 20, 30]
lis2 = [40, 50, 60]
lis3 = lis2 + lis1;
print(lis3)



#69. Write a Python program to remove duplicates from a list of lists.
list_of_int = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
return_list = []
for i in list_of_int:
  if i not in return_list:
    return_list.append(i);
  
print("69.",return_list)


#70. Write a Python program to get the depth of a dictionary. 
list_of_string = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
#Items start with a from the said list:
start_with_a = [i for i in list_of_string if i.startswith('a')]
print("70",start_with_a);#['abcd', 'abc', 'acjd']
#Items start with d from the said list:
start_with_d = [i for i in list_of_string if i.startswith('d')]
print("start_with_d:",start_with_d);#['dagfa']
#Items start with w from the said list:
start_with_w = [i for i in list_of_string if i.startswith('w')] #[]
print("start_with_w:",start_with_w);



list_of_iterable = [{},{},{}]
list_of_iterable1 = [{1,2},{},{}]
res1 = all(not i for i in list_of_iterable)
print(res1);




#72. Write a Python program to flatten a given nested list structure.
nested_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flatten_list = []
print("type", isinstance(nested_list[2],list));
for i in nested_list:
  if isinstance(i,list):
    for ele in i:
      flatten_list.append(ele);
      
  else:
    flatten_list.append(i);
print("72.",flatten_list);





#73. Write a Python program to remove consecutive duplicates of a given list.
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
unique_list = []
for i in original_list:
  if i not in unique_list:unique_list.append(i);
print("unique list:",unique_list);



#74. Write a Python program to pack consecutive duplicates of a given list elements into sublists
eg_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
return_sub_list = []

for i,j in itertools.groupby( eg_list, key=lambda x:x):
 
  return_sub_list.append(list(j))

'''
for i in range(0,len(eg_list)):
  if [eg_list[i]] not in return_sub_list:
    return_sub_list.append([eg_list[i]]);
  elif [eg_list[i]] in return_sub_list:
    
    index = return_sub_list.index([eg_list[i]])
    print(index)
    return_sub_list[index].append(eg_list[i]);
'''
print("74.",return_sub_list); #o/p: 

#75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.

#given_list = [1, 1, 2, 3, 4, 4.3, 5, 1]
given_list = "automatically"
return_list = []
for i,j in itertools.groupby( given_list, key=lambda x:x):
    return_list.append([len(list(j)),i]);

print(return_list)




#76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
'''
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
'''

giv_lis = [1, 1, 2, 3, 4, 4, 5, 1]
return_lis = [] 
for i,group in itertools.groupby(giv_lis,key=lambda x:x):
  x = list(group)
  return_lis.append(x) if len(x) > 1 else return_lis.append(i)

print(return_lis);




#77. Write a Python program to decode a run-length encoded given list.
def decode_run_length_list(lis):
  print(lis);
  return_lis = []
  for i in lis:
    if isinstance(i,list):
      for j in i:
        return_lis.append(i[1]);
    else:
      return_lis.append(i); 
  return return_lis;
    
lis = [[2, 1], 2, 3, [2, 4], 5, 1]
print(decode_run_length_list(lis))



#78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

def split_two_parts(org_lis, n):
  length = int(len(org_list)/n)
  return tuple([org_lis[0:length+1]]+[org_lis[length+1:]])

org_lis = [1, 1, 2, 3, 4, 4, 5, 1]
n = 3
print(split_two_parts(org_lis, n))


#79. Write a Python program to remove the K'th element from a given list, print the new list.
lis = [1, 1, 2, 3, 4, 4, 5, 1]
element = 2

new_list = [i for i in lis if i!=element]
print(new_list)

#80. Write a Python program to insert an element at a specified position into a given list.
position = 3
add_element = 12
givn_list = [1, 1, 2, 3, 4, 4, 5, 1]

def insert_into_list(ele,lis,indx):
  for i in range(0,len(lis)):
    if indx-1 == i:
      lis[i] = ele
  return lis;
  
print("80.",insert_into_list(add_element,givn_list,position))



#81. Write a Python program to extract a given number of randomly selected elements from a given list.
listOfInt = [1, 1, 2, 3, 4, 4, 5, 1]
elements  = 3
rand.shuffle(listOfInt)
print(listOfInt[0:elements]);


#82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
combination =  [1, 2, 3, 4, 5, 6, 7, 8, 9] 
return_combi = []
for index in itertools.combinations(combination,2):
  return_combi.append(list(index))

print(return_combi);



#83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
nums = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
sum_of_nums = 0;
for i in nums:
  sum_of_nums += round(i)
  
print(sum_of_nums);



#84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
lis_org = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
retun_lis = " ".join(list(map(str,sorted([round(i) * 5  for i in lis_org]))))
print(retun_lis)



#85. Write a Python program to create a multidimensional list (lists of lists) with zeros.
#o/p [[0, 0], [0, 0], [0, 0]]
Two_by_2 = [[0,0] for i in range(3)]
print(Two_by_2)



#86. Write a Python program to create a 3X3 grid with numbers
Three_by_3 = [[j for j in range(1,4)] for i in range(3) ]
print(Three_by_3)



#87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user.



#88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
'''
size = int(input("Input the size of the matrix: "))
matrix = [[0] * size for row in range(0, size)]
for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print(sum_diagonal);
'''

#89. Write a Python program to Zip two given lists of lists.
lis1 = [[1, 3], [5, 7], [9, 11]]
lis2 = [[2, 4], [6, 8], [10, 12, 14]]

return_lis = list(map(list.__add__,lis1,lis2))

print(return_lis)



#90. Write a Python program to count number of lists in a given list of lists.
list_length = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
print("length of sub-lists:" , len(list_length));




#91. Write a Python program to find the list with maximum and minimum length.
list_of_int = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("max", len(max(list_of_int)),max(list_of_int))
print("min", len(min(list_of_int)),min(list_of_int))



#92. Write a Python program to check if a nested list is a subset of another nested list.
lis1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
lis2 = [[1, 3], [13, 15, 17]]

def check_subset(lis1,lis2):
  return all(map(lis1.__contains__,lis2))

print(check_subset(lis1,lis2));


#93. Write a Python program to count the number of sublists contain a particular element. 
def check_element_sublist(lis1, search_ele):
  if len(lis1) <= 0 : return;  
  i = 0;
  for sub_list in lis1:
    if search_ele in sub_list:
      i+=1;
  return i;

sub_list = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
search_element = 1
output = check_element_sublist([[],[]], search_element)
print(search_element,"Repeated in sub list",output,"times");



#94. Write a Python program to count number of unique sublists within a given list.
list_integers = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
c = collections.Counter()
for sub_list in list_integers:
  if tuple(sub_list) in c.keys():
    c[tuple(sub_list)] = c[tuple(sub_list)] + 1   
  else:
    c[tuple(sub_list)] = 1; 
print(dict(c))




#95. Write a Python program to sort each sublist of strings in a given list of lists.
sort_sublist_eg = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
sort = list(map(sorted,sort_sublist_eg))
print(sort);


#96. Write a Python program to sort a given list of lists by length and value.
sort_sublist = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
sort = sort_sublist.sort(key = lambda x:len(x), reverse=True)
print(sort_sublist[::-1]);


#97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range.
def remove_sublist(lis1, start,end):
  return [sub_list for sub_list in lis1 if start and end in(sub_list)]
      
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
left_range = 13
right_range = 17
print(remove_sublist(list1,left_range,right_range));



#98. Write a Python program to scramble the letters of string in a given list.
def shuffle_word(word):
  lis = list(word);
  rand.shuffle(lis);
  return ''.join(lis);

list_string = ['Python', 'list', 'exercises', 'practice', 'solution']
list_return = [shuffle_word(word) for word in list_string]
print(list_return);



#99. Write a Python program to find the maximum and minimum values in a given heterogeneous list.
hetrogenous = ['Python', 3, 2, 4, 5, 'version']
def min_max(lis):
  xmin=(min(i for i in hetrogenous if isinstance(i,int)));
  xmax=(max(i for i in hetrogenous if isinstance(i,int)));
  return (xmin,xmax);
  
print(min_max(hetrogenous));



#100. Write a Python program to extract common index elements from more than one given list.
num1=  [1, 1, 3, 4, 5, 6, 7]
num2=	[0, 1, 2, 3, 4, 5, 7]
num3=	[0, 1, 2, 3, 4, 5, 7]

def common_index_ele(l1,l2,l3):
  return_lis = []
  for i,j,k in zip(l1,l2,l3):
    if i==j==k:
      return_lis.append(i);
  return return_lis;
print(common_index_ele(num1,num2,num3));



#101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
given_list = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
given_list.sort(key= sum)
print(given_list)



#102. Write a Python program to extract specified size of strings from a give list of string values.
def filter_length(lis, length):
  return [l for l in lis if len(l) == length]
   
list_ = ['Python', 'list', 'exercises', 'practice', 'solution']
length = 8
print(filter_length(list_,length))



#103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously. 
org_lis = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
ls = []
return_lis = [ls.append(org_lis[i]) for i in range(0,len(org_lis)-1) if org_lis[i] == org_lis[i+1] and org_lis[i] not in ls]

#for i in range(0,len(org_lis)-1):
#  if org_
print(ls);



#104. Write a Python program to find the difference between consecutive numbers in a given list.
lis = [4, 5, 8, 9, 6, 10]
r_l = [lis[i+1] - lis[i]  for i in range(0,len(lis)-1)]
print(r_l)



#105. Write a Python program to compute average of two given lists.
lis1 = [1, 1, 3, 4, 4, 5, 6, 7]
lis2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

result = sum(lis1+lis2)/len(lis1+lis2)
print(result)


#106. Write a Python program to count integer in a given mixed list. 
mixed_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

def count_int(lis):
  count =0
  for i in lis:
    if type(i) is int: count +=1;

  return count;
  
print(count_int(mixed_list));
  
  
  
#107. Write a Python program to remove a specified column from a given nested list.  
remove_colum_lis = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
value = 1
return_lis = [i[1:] for i in remove_colum_lis]
print(return_lis)



#108. Write a Python program to extract a specified column from a given nested list.
def extract_column(lis, col_index):
  if len(lis) <= 0 and col_index < 0:
    return 
  res = [arr[col_index] for arr in lis if len(arr) > col_index]
  return res; 
  
lis = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
extract_index = 2;
print(extract_column(lis, extract_index));


#109. Write a Python program to rotate a given list by specified number of items to the right or left direction.
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("#Rotate the said list in left direction by 4:")
print(nums1[4:] + nums1[:4])

print("#Rotate the said list in left direction by 2:")
print(nums1[2:]+nums1[:2])

print("#Rotate the said list in Right direction by 4:")
print(nums1[-4:] + nums1[:-4])

print("#Rotate the said list in Right direction by 2:")
print(nums1[-2:] + nums1[:-2]);


#110. Write a Python program to find the item with maximum occurrences in a given list.
lis = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

def maximum_occurrences(lis):
  dic_store = {};
  for i in lis:
    dic_store[i] = lis.count(i);  
   
  return dict(sorted(dic_store.items(), key = lambda x:x[1]));

x = maximum_occurrences(lis)

print("maximum occurrences",x.get(len(x)-1));


#111. Write a Python program to access multiple elements of specified index from a given list.
eg = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
index_list = [0, 3, 5, 7, 10]
return_lis = [eg[i] for i in index_list]
print(return_lis)



#112. Write a Python program to check whether a specified list is sorted or not. Go to the editor Original list:
ls = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
check_sorted = all(ls[i] <= ls[i+1] for i in range(0,len(ls) -1))
print(check_sorted);


#113. Write a Python program to remove duplicate dictionary from a given list.
lis_of_dic = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

def remove_duplicate_dict(lis_dic):
  returnlis = []
  for i in lis_of_dic:
    if i not in returnlis:
      returnlis.append(i)
      
  return returnlis;
  
  
print("113.",remove_duplicate_dict(lis_of_dic));




#114. Write a Python program to extract the nth element from a given list of tuples.
list_of_tuple = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
nth_element = 2;

def extract_tuple(lis,ele):
  return [l[ele] for l in lis ]
  
print(extract_tuple(list_of_tuple,nth_element))


#115. Write a Python program to check if the elements of a given list are unique or not.
lis = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
#lis=[2, 4, 6, 8, 10, 12, 14]
def check_unique(lis):
  return True if len(set(lis)) == len(lis) else False
  
print(check_unique(lis))  



#116. Write a Python program to sort a list of lists by a given index of the inner list.
li = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
def sort_by_index(li,index):
  li.sort(key = lambda x : x[index]);
  return li;
  
sort_index = 2
print(sort_by_index(li,sort_index))



#117. Write a Python program to remove all elements from a given list present in another list.
lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis2 = [2, 4, 6, 8]

unique_list = [i for i in lis1 if i not in lis2]
print(unique_list)



#118. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
list_of_int = [2, 4, 6, 8]
diff_ = [  list_of_int[i+1] - list_of_int[i] for i in range(0,len(list_of_int)-1)]
print(diff_)


#119. Write a Python program to check if a substring presents in a given list of string values.
list_of_string = ['red', 'black', 'white', 'green', 'orange']
substring_to_search = 'abc'

def isSubstring(ls, substring):
  return any(substring in string for string in ls);


print(isSubstring(list_of_string,substring_to_search))
  


#120. Write a Python program to create a list taking alternate elements from a given list.
colors = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
alternate_items = colors[::2]
print(alternate_items)



#121. Write a Python program to find the nested lists elements which are present in another list.
lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lis2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

def find_in_nested(lis1,lis2):
  return [[i for i in lis1 if i in subList] for subList in lis2]
  
print(find_in_nested(lis1,lis2))
  
  

#122. Write a Python program to find common element(s) in a given nested lists. 
list_of_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

def find_common(lis):
  if len(list_of_list) < 2:
    return 
  res = []
  for length in range(1,len(lis)):
    for j in lis[length]:
      if j in lis[0] and j not in res:res.append(j);
  return res;
print(find_common(list_of_list))



#123. Write a Python program to reverse strings in a given list of string values.
org_lis = ['Red', 'Green', 'Blue', 'White', 'Black']
reverse_words = [i[::-1] for i in org_lis]
print(reverse_words)



#124. Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list.
lis_of_tupl = [(2, 7), (2, 6), (1, 8), (4, 9)]
def max_min_product(lis):
  product_tupl = []
  for i in lis:
    prod = 1;
    for j in i:
      prod *= j
    product_tupl.append(prod);
  
  return (max(product_tupl),min(product_tupl))
  
print(max_min_product(lis_of_tupl))



#125. Write a Python program to calculate the product of the unique numbers of a given list.
def product_unique_num(lis):
  prod = 1
  for i in set(lis):
    prod *= i;
  return prod;


lis = [10, 20, 30, 40, 20, 50, 60, 40]
print(product_unique_num(lis))



#126. Write a Python program to interleave multiple lists of the same length.
lis1 = [1, 2, 3, 4, 5, 6, 7]
lis2 = [10, 20, 30, 40, 50, 60, 70]
lis3 = [100, 200, 300, 400, 500, 600, 700]
return_lis = list(zip(lis1,lis2,lis3))
print(return_lis)



#127. Write a Python program to remove words from a given list of strings containing a character or string.

list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
char_list = ['#','color','@']

def remove_words(lis, char_list):
  res = []
  for line in lis:
    new_words = " ".join([ i for i in line.split() if not any([ls in i for ls in char_list])])
    res.append(new_words)
  return res;
  
print(remove_words(list1,char_list))
  

  
#128. Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
def sum_index_list(lis,m,n):
  res = 0;
  for i in range(m,n+1):
    res += lis[i]
  return res;

nums = [2,1,5,6,8,3,4,9,10,11,8,12]
m = 8
n = 10
print(sum_index_list(nums,m,n));
  


#129. Write a Python program to reverse each list in a given list of lists.

list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def reverse_sublist(lis):
  return [[i[::-1]] for i in lis]
  
print(reverse_sublist(list_of_lists))



#130. Write a Python program to count the same pair in three given lists.
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [2, 2, 3, 1, 2, 6, 7, 9]
l3 = [2, 1, 3, 1, 2, 6, 7, 9]

res = sum([int(i==j==k) for i,j,k in zip(l1,l2,l3)])
print(res)



#131. Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
lis = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]

dic_ex = {}
for i in lis:
  dic_ex[i] = lis.count(i);
    
x = (list(dic_ex.keys()),list(dic_ex.values()));

print(x)


#132. Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
lis = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

def min_max_index(lis):
  min_num = min(lis)
  max_num = max(lis)
  
  min_ = [i for i,j in enumerate(lis) if j==min_num]
  max_ = [i for i,j in enumerate(lis) if j == max_num]
  
  return min_,max_;
  

result = min_max_index(lis)
print("min",result[0]);
print("max",result[1]);



#133. Write a Python program to check common elements between two given list are in same order or not.
c1 = ['red', 'green', 'black', 'orange']
c2 = ['red', 'pink', 'green', 'white', 'black']
c3 = ['white', 'orange', 'pink', 'black']

def check_common_element(lis1,lis2):
  result = any( c1 == c2 for c1,c2 in zip(lis1,lis2))
  return result

print(check_common_element(c1,c2));




#134. Write a Python program to find the difference between two list including duplicate elements.
lis1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lis2 = [1, 1, 2, 4, 5, 6]

def diff_between_list(lis1,lis2):
  result = list(lis1)
  for i in lis2:
    result.remove(i)
  return result;

print(diff_between_list(lis1,lis2))


#135. Write a Python program to iterate over all pairs of consecutive items in a given list.
lis = [1, 1, 2, 3, 3, 4, 4, 5]
response = [(lis[i],lis[i+1]) for i in range(0,len(lis)-1)]
print(response); 


#136. Write a Python program to remove duplicate words from a given list of strings.
lis = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']

def remove_duplicate_words(lis):
  result = []
  for i in lis:
    if i not in result:
      result.append(i)
  return result
  
print(remove_duplicate_words(lis));



#137. Write a Python program to find a first even and odd number in a given list of numbers.
def first_even_odd(lis):
  first_even = next( (i for i in lis if i%2==0),-1)
  first_odd = next(i for i in lis if i%2 !=0);  
  return (first_even, first_odd);
  
nums= [1,3,5,7,4,1,6,8]
print(first_even_odd(nums))


#138. Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

def mixed_sorting(lis):
  #sorting using sorted function
  sorting_nums = sorted([i for i in lis if type(i) is int])
  sorting_str = sorted([i for i in lis if type(i) is str])
  return (sorting_nums+sorting_str)

print(mixed_sorting(original_list));


#139. Write a Python program to sort a given list of strings(numbers) numerically.
def str_num_sort(lis):
  return sorted([int(i) for i in lis])

lis = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
print(str_num_sort(lis))


#140. Write a Python program to remove the specific item from a given list of lists.
lis = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]

def remove_index(lis,index):
  return [[k for j,k in enumerate(i) if j!=index-1] for i in lis]
  
index = 4  
print(remove_index(lis,index))



#141. Write a Python program to remove empty lists from a given list of lists.
lis = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
def remove_empty_list(lis):
  return [i for i in lis if hasattr(i, '__iter__') and len(i) > 0]
  
print(remove_empty_list(lis));  


#142. Write a Python program to sum a specific column of a list in a given list of lists.
lis_of_lis = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

def sum_of_col(lis,col):
  return sum([i[col] for i in lis])
  
col = 3
print(sum_of_col(lis_of_lis,col))    


#143. Write a Python program to get the frequency of the elements in a given list of lists.
frequency_eg = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
dic = {}
def frequency_list_of_list(lis_of_lis):  
  for i in lis_of_lis:
    for j in i:
      count = 1
      if j in dic:
        dic[j] = dic.get(j) + 1
      else:  
        dic[j] = count
  return dic;
  
print(frequency_list_of_list(frequency_eg))


#144. Write a Python program to extract every first or specified element from a given two-dimensional list.
start = -5 
stop = 5
excpt = [-5,0,4,3,2]

def generate_num(start, end,lis):
  num = rand.choice([i for i in range(start,end+1) if i not in lis])
  return num 

print(generate_num(start,stop,excpt))




#146. Write a Python program to compute the sum of digits of each number of a given list.
num = [10, 20, -4, 5, -70]

def sum_of_digits(num):
  sum_ = 0;
  for i in num:
    if isinstance(i,int):
      x = abs(i)
      while x > 0:
        mod = int(x%10)
        x /= 10;
        sum_ += mod;
  return sum_      

print(sum_of_digits(num))



#147. Write a Python program to interleave two given list into another list randomly.
l1 = [1, 2, 7, 8, 3, 7]
l2 = [4, 3, 8, 9, 4, 3, 8, 9]
l3 = l1 + l2;
rand.shuffle(l3)
print(l3);



#148. Write a Python program to remove specific words from a given list.
lis = ['red', 'green', 'blue', 'white', 'black', 'orange']
remove_words = ['white', 'orange']
def given_list(lis, remove):
  return [i for i in lis if i not in remove]

print(given_list(lis,remove_words))




#!149. Write a Python program to get all possible combinations of the elements of a given list.
lis = ['orange', 'red', 'green', 'blue']
lis2 = list(itertools.combinations(lis,2))
#print(lis2)


#150. Write a Python program to reverse a given list of lists.
ls = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
reverse_lis = ls[::-1]
print(reverse_lis);



#151. Write a Python program to find the maximum and minimum values in a given list within specified index range.
lis = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
def min_max_range(lis,start,end):
  lis_min = min(lis[i] for i in range(start,end))
  lis_max = max(lis[i] for i in range(start,end))
  return lis_max,lis_min
  
  
start = 3
end = 8  
print(min_max_range(lis,start,end));



#152. Write a Python program to combine two given sorted lists using heapq module.
l1=[1, 3, 5, 7, 9, 11]
l2=[0, 2, 4, 6, 8, 10]
print(list(heapq.merge(l1,l2)));



#153. Write a Python program to check if a given element occurs at least n times in a list.
lis = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
#Check if 3 occurs at least 4 times in a list:
ele = 3
times = 4

#Check if 8 occurs at least 3 times in a list:
ele1 = 8
times2 = 3

def occurs_n_times(lis,ele,nth):
  return True if lis.count(ele) and lis.count(ele)>=4 else False 
    
#print(occurs_n_times(lis, ele,times))
print(occurs_n_times(lis, ele1,times2))


#154. Write a Python program to join two given list of lists of same length, element wise.
lis1 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
lis2 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]

def join_two_list(lis1,lis2):
  return [l1+l2 for l1,l2 in zip(lis1,lis2)]

print(join_two_list(lis1, lis2))


#155. Write a Python program to add two given lists of different lengths, start from left.
lis1 = [3, 3, -1, 7]
lis2 = [2, 4, 7, 0, 5, 8]

def add_two_list(l1, l2):
  lis1 = l1
  lis2 = l2
  if len(lis2) > len(lis1):
    temp = lis2
    lis2 = lis1
    lis1 = temp
  for i in range(0,len(lis1)):
    if i > len(lis2)-1:
      break;
    lis1[i] = lis1[i] + lis2[i]
  return lis1
  
print(add_two_list(lis1,lis2))


#156. Write a Python program to add two given lists of different lengths, start from right.

def add_two_list_right(lis1,lis2):
  lis1 = l1
  lis2 = l2
  
  if len(lis2) > len(lis1):
    temp = lis2
    lis2 = lis1
    lis1 = temp
  length2 = len(lis2) - 1
  for i in range(len(lis1)-1,-1,-1):
    if length2 < 0:
      break; 
    else:
      lis1[i] = lis1[i] + lis2[length2]
      length2 -= 1;
  return lis1
  
l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 4, -3]
print(add_two_list_right(l1,l2))


#157. Write a Python program to interleave multiple given lists of different lengths.


def interleave_multiple_list(l1,l2,l3,l4):
  ll1 = len(l1)
  ll2 = len(l2)
  ll3 = len(l3)
  ll4 = len(l4)
  
  result = []
  for i in range(max(ll1,ll2,ll3,ll4)):
    if i < ll1:
      result.append(l1[i])
      
    if i < ll2:
      result.append(l2[i])
    
    
    if i < ll3:
      result.append(l3[i])
    
    
    if i < ll4:
      result.append(l4[i])
    
  return result;
    

l1=[2, 4, 7, 0, 5, 8]
l2=[2, 5, 8]
l3=[0, 1]
l4=[3, 3, -1, 7]

print(interleave_multiple_list(l1,l2,l3,l4))




#158. Write a Python program to find the maximum and minimum values in a given list of tuples.
lis = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
lis_max = max(i[1] for i in lis)
lis_min = min(i[1] for i in lis)
print((lis_min,lis_max))



#159. Write a Python program to append the same value /a list multiple times to a list/list-of-lists.
def add_multiple_times(item, times, lis=[]):
   for i in range(times):
     lis.append(item);
     
   return lis

print(add_multiple_times([1, 2, 5],3,[[5, 6, 7], [1, 2, 5]]))


#160. Write a Python program to remove first specified number of elements from a given list satisfying a condition.
def remove_number_of_elements(ls,times):
  count = 1 
  result = [] 
  for i in ls:
    if count>times or (i%2 != 0):
      result.append(i);
    else:  
      count +=1;
    
  return result;    
    
ls = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]    
print(remove_number_of_elements(ls,4))



#162. Write a Python program to find the last occurrence of a specified item in a given list.
def last_occurrence_item(lis,ele):
  return "".join(lis).rfind(ele);
lis = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
print(last_occurrence_item(lis,'w'));


