import random as rand
import itertools
import ast
import collections
import operator
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





