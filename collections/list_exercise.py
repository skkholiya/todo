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

