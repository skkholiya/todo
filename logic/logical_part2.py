import collections
import re
from json import loads
#28 Python program to print even numbers in a list
int_list=[89,65,87,23,45,8]
even_numbers = [int(num) for num in int_list if num%2==0]
print("even numbers:",even_numbers)

#29 Python program to print odd numbers in a List
odd_numbers = [int(num) for num in int_list if num%2!=0]
print("odd numbers:",odd_numbers);

#30 Python program to print positive numbers in a list
all_numbers = [-89,80,23,21,-1,-334,-212,-81,7]
postive_numbers = [num for num in all_numbers if num>=0]
print("Postive Numbers:",postive_numbers)

#31 Python program to print negative numbers in a list
negative_numbers = [num for num in all_numbers if num<0]
print("Negative Numbers:",negative_numbers);

#32 Python program to print all Strong numbers in given list
def factorial(num):
  if num == 0:
    return 1;
  else: 
    return num * factorial(num-1)
  
#Strong num: factorial of each digit of a number is equal to the number.
def get_strong_num(find_strong_num):
  strong_num = []
  for num in find_strong_num:
    temp_num=num;
    result =0;
    mod=0;
    while(temp_num>0):
      mod = int(temp_num%10);
      result += factorial(mod);
      temp_num = int(temp_num/10);
    if result == num:strong_num.append(num);
  return strong_num;
  
find_strong_num = [15, 1,58, 75, 675, 145, 2];
print("Strong Number:", get_strong_num(find_strong_num))

#33 Merging duplicates to list of list
'''
The original list : [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1]
The elements after grouping are : [[1, 1, 1], [2, 2], [3, 3, 3], [4, 4, 4]]
'''
list_of_list = [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1];
#converting to dictionary store key as element, value as number of times it's occur in list.
dict_ = collections.Counter(list_of_list);

#multiplying key to number of times its occur in the list or dict.
x= [[x] * y for x,y in dict_.items()];
print(x);



"""
The original list : [['24'], ['45'], ['78'], ['40']]
The list after conversion : [[2, 4], [4, 5], [7, 8], [4, 0]]

"""
#34 Convert list of numerical string to list of Integers
input_list = [['24'], ['45'], ['78'], ['40a']];

#checking if unicode value of a string character is in between(48-58), store the element to integer list.
res = [[int(j) for j in k  if ord(j) in range(48,59)] for i in input_list for k in i]
print(res); #o/p- [[2, 4], [4, 5], [7, 8], [4, 0]]


#35 Remove Duplicates from a List
list_of_numbers = [43,2,34,5,43,5,65,3,2,4]
remove_duplicate = [];
#result= [i if i not in list_of_numbers else list_of_numbers.remove(i) for i in list_of_numbers]
for i in list_of_numbers:
  if i not in remove_duplicate:remove_duplicate.append(i);

print(remove_duplicate); #o/p-[43, 2, 34, 5, 65, 3, 4]

#37 Ways to remove duplicates from list
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]
#using dict.fromkeys
print(list(dict.fromkeys(test_list))); #o/p- [1, 4, 5, 6, 7, 3, 9]

#using set
print(list(set(test_list))); #o/p- [1, 4, 5, 6, 7, 3, 9]

#using list comprehension
op_list = []
result = [ op_list.append(i) for i in test_list if i not in op_list]; #o/p- [1, 4, 5, 6, 7, 3, 9]

'''
The original list : [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]
The list after duplicate removal : [(-1, 0, 1), (1, 3, 4), (1, 2, 3)]
'''
#38
orignal_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]];

#iterating the list inside set(doesn't contains duplicate).
return_list = list( set(tuple(sorted(i)) for i in orignal_list if i in orignal_list));

print(return_list) #o/p-[(1, 2, 3), (-1, 0, 1), (1, 3, 4)]


'''
Input:  [[-1, 5, 3], [3, 5, 0], [-1, 5, 3], 
         [1, 3, 5], [-1, 3, 5], [5, -1, 3]]
Output:  {(1, 3, 5), (0, 3, 5), (-1, 3, 5)}
'''
#39 Remove all duplicates and permutations in nested list
input_list=[[-11, 0, 11], [-11, 11, 0], [-11, 0, 11], 
         [-11, 2, -11], [-11, 2, -11], [-11, -11, 2]]
returnList= set(tuple(sorted(i)) for i in input_list);
print(returnList); #o/p- {(-11, 0, 11), (-11, -11, 2)}


#40 Split a list having single integer
split_list = [15478]
return_list = [int(j) for i in split_list for j in str(i) if ord(j) in range(48,59)]
print(return_list) #o/p- [1, 5, 4, 7, 8]

#41 Convert list of numerical string to list of Integers
'''
The original list : [['24'], ['45'], ['78'], ['40']]
The list after conversion : [[2, 4], [4, 5], [7, 8], [4, 0]]
'''
ex_str_list = [['24'], ['45'], ['78'], ['40']]
rs = [[int(k) for k in j] for i in ex_str_list for j in i]
print(rs) #o/p- [['2', '4'], ['4', '5'], ['7', '8'], ['4', '0']]

#42 Convert number to list of integers
num = 2019
res = [int(i) for i in str(num) if str(num).isdigit()]
print(res) #o/p- [2, 0, 1, 9]

#43 Print single and multiple variable in python
#end denotes the ending of the output
print(1,end="");
print(1,2);


'''
Input : Wiiiin, ch = 'i'
Output : Win
'''
#Replace multiple occurrence of character by single
sample_input = "Wiin"
ch = 'i'
pattern= ch+'{2,}' #creating pattern if two or more than two i occur in string.
c= re.sub(pattern,ch,sample_input) #replace the matched characters with specified string.
    
print(c)
#Ways to convert Boolean values to integer
bool_value = True
#using if else
if bool_value:
  bool_value =1;
else:
  bool_value = 0;

#using int()
bool_value1= False
bool_value1 = int(bool_value1)
print(bool_value1)

#using map()
bool_value2 = [True,False]
bool_value2 = list(map(int,bool_value2))
print(bool_value2)

'''
Associating a single value with all list items
'''
list_of_int = [1,2,3,4,5,6,7,8]
associate_value = "Integer"
#mapping the value to the list elements and return as tuple
res = list(map(lambda x:(x,associate_value),list_of_int));
print(res); #o/p- [(1, 'Integer'), (2, 'Integer'), (3, 'Integer'), (4, 'Integer'), (5, 'Integer'), (6, 'Integer'), (7, 'Integer'), (8, 'Integer')]





#47 Convert list of string to list of list
list_of_str = [['[1, 4, 5]', '[4, 6, 8]']]
#removing bracket using strip, after that spliting the list elements using comma(,) seperator.
result_list = [j.strip("'[]'").split(",") for i in list_of_str for j in i]
print(result_list) #o/p- [['1', ' 4', ' 5'], ['4', ' 6', ' 8']]






#48 Convert list of tuples to list of list
list_of_tuples = [("delhi"),("mumbai"),("noida")]
#converting tuple to list.
res_list_of_list = [[i] for i in list_of_tuples]
print(res_list_of_list); #o/p- [['delhi'], ['mumbai'], ['noida']]





#49 Convert list of strings to list of tuples
list_str = ['4, 1', '3, 2', '5, 3']
#spliting the list using ", " then mapped into int
result_tuple_str = [tuple(map(int,i.split(", "))) for i in list_str]
print(result_tuple_str) #o/p- [(4, 1), (3, 2), (5, 3)]





#50 Convert a string representation of list into list
list_int = "[1, 2, 3, 4, 5]"
#spliting the string using comma seperator and removing "[]" from the string.
convert_to_str = [str(i).strip("[]") for i in list_int.split(", ")]
print((convert_to_str));





#51 Convert string enclosed list to list
def convert_list(arg):
  return loads(arg)

inp_string = "[0, 2, 9, 4, 8]"
#passing inp_string to as json object and it will deserialize it to python object.
x = convert_list(inp_string)
print(x) #o/p- [0, 2, 9, 4, 8]





#52 Convert 1D list to 2D list of variable length
input_list = [1, 2, 3, 4, 5, 6]

var_lst = [1, 2, 3]

return_list= []
k=0
for i in range(len(var_lst)):
  #slicing list elements 0 to (0 + var_list element)
  return_list.append(input_list[k:k + var_lst[i]]);
  k += var_lst[i];
print(return_list) #o/p- [[1], [2, 3], [4, 5, 6]]





#9 Convert list of tuple into dictionary
list_of_tuples = [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)];

x={}
for i,j in dict(list_of_tuples).items():
  #if key is not present in the dict, it will insert a key into dictionary
  x.setdefault(i,[j])
print(x)  #o/p- {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}





#53 Convert list of tuples to list of strings
list1 = [('M','o','n'), ('d','a','y'), ('7', 'pm')]
res1 = ["".join(i) for i in list1]
print(res1) #o/p - ['Mon', 'day', '7pm']
