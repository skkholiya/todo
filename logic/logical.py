import sys;
import functions_ as fp;

# . Program to remove duplicates from a list of integers
_list=[1,2,4,3,6,4,2,7,9,44,3,3,5,21,44];
#Storing the list elements as dictonary keys(doesn't allow duplicate keys)
#after that converting keys to the list
duplicate_elements_list= list(dict.fromkeys(_list));
#print(duplicate_elements_list);

#print("list",_list);
# 5. Program to print duplicates from a list of integers
_list=[1,2,4,3,6,4,2,7,9,44,3,3,5,21,44];
#for storing the duplicate elements
duplicate_elements = [];
#length of list
_size = len(_list);
for index in range(_size):
  next = index + 1;
  #getting the next element index and iterating upto the list size.
  for sub_index in range(next,_size):
    #comparing the first element is equals to any of the sub-list element 
    #if true then check if element already present in the duplicate_elements
    # list or not(for more than two duplicate) 
    result=_list[index] ==_list[sub_index] and _list[index] not in duplicate_elements;
    if result:
      duplicate_elements.append(_list[index]);
      
      
#print(duplicate_elements);
# o/p- [2, 4, 3, 44]


# smallest and second smallest element
integer_list = [8,5,9,2,3,6,1,1,4];
_size_list = len(integer_list);
for i in range(_size_list):
  j = i+1; 
  for j in range(j,_size_list):
    if(integer_list[i]>integer_list[j]):
      temp = integer_list[j];
      integer_list[j]=integer_list[i];
      integer_list[i]=temp;      
            
print(list(dict.fromkeys(integer_list))[:2]);

#extract int from string
txt="Hello John, How are you. Call me on this number 7982116616 use pincode +91";
length = len(txt);
for index in range(length):
  #getting ASCII code(48-57 reserve for 0-9) of each character, if true simply display the value 
  if ord(txt[index]) in range(48,58):
    print(txt[index]);

#convert list to string
int_list = [4,3,5,4,2,1,6];
#iterate all the int_list elements and convert the elements to string type of list
#after that using seperator "," join all list elements into one string.
list_to_string=",".join([str(x) for x in int_list]);

print(list_to_string);

#Convert a list of multiple integers into a single integer
int_list= [44,32,2,"dd"]

string_obj = [str(outcome) for outcome in int_list if isinstance(outcome,int)];
convert_to_string = "".join(string_obj);
convert_to_int = int(convert_to_string)

print(convert_to_int);#o/p = 44322;

#convert list to tuple of lists e.g - ["happy","new","year","2021"] 
#o/p - (["happy"],["new"],["year"],["2020"])

txt_str= ["happy","new","year","2021"]

tuple_ex = tuple([i] for i in txt_str);

print(tuple_ex);

ashish_icici = "9897257046";

list_of_tuple = [("hello"),("how"),("are"),("you")];
print(list_of_tuple);

#l-ist [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
#final list [5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 6, 6, 6, 2, 2, 7, 7, 3, 8, 9]
frequency_list = [9, 4, 3, 3, 4, 6, 5, 6, 5, 7, 1, 7, 2, 4, 7, 8, 9, 6, 6, 8];

#key= counting the value occurrence in the frequency_list, then sort the list based on count. 
result=sorted(frequency_list, key=frequency_list.count, reverse=True);
print(result);
  
#remove duplicates from sorted_frequency_list
frequency_without_duplicate = list(dict.fromkeys(result));

print(frequency_without_duplicate)

#sum of large numbers
str1="58973498573498600";
str2 = "4534635465654";
print(fp.sum_two_large_numbers(str1,str2));

#Convert list of string into sorted list of integer
list_of_string = ["2","6","8","1","3","5","132","34"];
list_of_integers = [int(x) for x in list_of_string]
list_of_integers.sort()
print("list of integers:",list_of_integers);

#15 Python program to create a list of tuples from given list having number and its cube in each tuple

list_of_numbers = [2,3,4,5,3,6,6,25]
#getting outcome from list then creating tuple(outcome,cube_of_outcome) e.g - (2,2*2*2) = 8
list_of_tuples = [(i, i ** 3) for i in list_of_numbers];
print(list_of_tuples);

#Program to convert a tuple to a string
languages = ("java","python","rust", "c-sharp")
int_tupl = (1,2,3,4,5)
int_to_string = ",".join(str(outcome) for outcome in int_tupl);
tuple_to_string = " ".join(languages);
print(tuple_to_string);
print(int_to_string);

#Merge list of tuple into list by joining the strings
lang = [('PHP', 'Laravel'), ('JavaScript', 'Node.js'), ('Java', 'Spring'), ('Python','Flask'), ('C#','ASP.NET')] 
#Joining the tuple elements with - seperator
output_lang = ["-".join(i) for i in lang]
print(output_lang);
#o/p- [PHP-Laravel, "JavaScript-Node.js", "Java-Spring", "Python-Flask", "C#-ASP.NET"]

#The original list 1 : [[1, 4, 5], [8, 7], [2]]
#The original list 2 : [[‘g’, ‘f’, ‘g’], [‘f’, ‘r’], [‘u’]]
#The paired list of tuple is : [(1, ‘g’), (4, ‘f’), (5, ‘g’), (8, ‘f’), (7, ‘r’), (2, ‘u’)] 

#Pair and combine nested list to tuple list

char = [['a', 's', 'c', 'i','i'], ['c','h', 'a', 'r'], ['c','o','d','e']]

values = [[97, 115, 99,105,105], [99, 104, 97,114], [99,111,100,101]]

#first loop for zipping/pairing together sub array of the both list. second loop for zipping/pairing the sub array's element togther.
pair_and_combine = [ (sub_index1, sub_index2) for (index1,index2) in zip(char,values) for (sub_index1,sub_index2) in zip(index1,index2)]

#print(pair_and_combine);


#The original list 1 : [('key1', 4), ('key3', 6), ('key2', 8)]
#The original list 2 : [('key2', 1), ('key1', 4), ('key3', 2)]
#The grouped summation tuple list is : [('key2', 9), ('key1', 8), ('key3', 8)]

list1=[('key1', 4), ('key3', 6), ('key2', 8)]
list2=[('key2', 1), ('key1', 4), ('key3', 2)]

#converting to dict to matching the keys.
dict_ = (dict(list1));



for i in list2:
  #checking if tuple key is present in dict
  if i[0] in dict_:
    #adding the dict value with tuple value 
    dict_[i[0]]=dict_.get(i[0]) + i[1]; 

dict_to_list_tuple = [ (x,y) for x,y in dict_.items()]
print(dict_to_list_tuple);


'''
The original list is : [(‘geeks’, ‘for’, ‘geeks’), (‘computer’, ‘science’, ‘portal’)]
The joined data is : [‘geeks for geeks’, ‘computer science portal’] 
'''
#Join tuple elements in a list
list_of_tuples = [("java","python","javascript"), ("spring","django","node.js")]
#seprating the tuples value using " "  
result = [" ".join(i) for i in list_of_tuples]
print(result);

'''
The original list : [(‘key1’, [3, 4, 5]), (‘key2’, [1, 4, 2]), (‘key3’, [9, 3])]
The list tuple attribute summation is : [(‘key1’, 12), (‘key2’, 7), (‘key3’, 12)] 
'''


orignal_list = [('rating1', [7, 4, 5]), ('rating2', [1, 4, 2,6]), ('rating3', [9, 3,5])]
#adding all sub array elements using sum function
result = [(i,sum(j)) for i,j in orignal_list]
print(result)

'''
Input : [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
Output : [(2, 1), (5, 4, 3), (9, 8, 7, 6)]
'''
_input = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
#passing the tuple outcome to the sorted method then reverse the tuple
reverse_tuple = [ tuple(sorted(i,reverse=True)) for i in _input]
print(reverse_tuple)
#print(dir(_input)) 

'''
The original list 1 : [('Geeks', 1), ('for', 2), ('Geeks', 3)]
The original list 2 : [4, 5, 6]
The modified resultant list of tuple : [('Geeks', 4), ('for', 5), ('Geeks', 6)]
'''
list1= [('Geeks', 1), ('for', 2), ('Geeks', 3)]
list2= [4, 5, 6]

#for list of tuples first argument(i.e. Geeks ...) setting as it is.
#for second argument of list of tuples(i.e 1,2,3) we zipping it to with list2 arguments.
returnList = [ (i[0],j) for i,j in zip(list1,list2)]
  
print(returnList)

dict_example = {
		"name" : "suresh",
		 "age" :  25,
		 "current city:" : "noida",
		 "Hometown:" : "Almora",
		 "contact no": 7982116616
            	 }

#storing key,value in list of tuples
result = [(i,j) for i,j in dict_example.items()]

print(result) #[('name', 'suresh'), ('age', 25), ('current city:', 'noida'), ('Hometown:', 'Almora'), ('contact no', 7982116616)]

'''
The original list is : [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)]
The Tuple List after removal of element : [(5, 7), (7, 2, 4), (7, ), (10, 8)]
'''
original_list = [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)]

original_list2 = [("hello","hi","there"), ("hello", "java", "python"),("google","hello")]

remove_element2 = "hello";

#suppose we want to remove 6 from all list of tuples
remove_element = 6;

result2 = [ tuple(j for j in i if j!=remove_element2) for i in original_list2]

#storing only those elements to tuple which is not equal to 6
result = [ tuple(j for j in i if j!= remove_element) for i in original_list]

'''
[('Python', 'tutorialspoints'), ('Management', 'other'), ('Django', 'tutorialspoints'), ('React',
'tutorialspoints'), ('Social', 'other'), ('Business', 'other')]

{'tutorialspoint': [('Python', 'tutorialspoints'), ('Django', 'tutorialspoints'), ('React', 'tutorialspoints')],
'other’: [('Management', 'other'), ('Social', 'other'), ('Business', 'other')]}

'''
tutorial=[('Python', 'it'), ('Management', 'other'), ('Django', 'it'), ('React',
'it'), ('Social', 'other'), ('Business', 'other')]

output={}

for (i,j) in tutorial:
  if j in output:
  #check if value is present as key in dict, append tuple to list.
    output[j].append((i,j))

  else:
  #assinging second value to as key and store list of tuple as value in dictionary.
    output[j]= [(i,j)]
    
print(output);

'''
Input: {34, 21, 56, 42, 89, 90, -1}
Output: {-1, 21}
'''
def find_n_minimumele(arg_list,N):
  output_list = [];
  #checking empty condition
  if len(arg_list) == 0:
    return output_list;
  
  #no of element we want to display from list
  for n in range(N):
    max_value = sys.maxsize; #return int max value: 9223372036854775807
    #iterating the list
    for list_index in range(len(arg_list)):
      # replacing with max value, if list element is less than max value 
      if arg_list[list_index] < max_value:
        max_value = arg_list[list_index]
    
    #storing the minnimum element to output list
    output_list.append(max_value)
    #removing the mininmum element from list, because it will occur in next iteration 
    arg_list.remove(max_value)
  return output_list;    

input_list = [34, 21, 56, 42, 89, 90, -1]
N=2
print(find_n_minimumele(input_list,N));

'''
Input : [(‘a’, ‘e’), (‘b’, ‘x’), (‘b’, ‘x’), (‘a’, ‘e’), (‘b’, ‘x’)]
Output :
(‘a’, ‘e’) – 2
(‘b’, ‘x’) – 3
'''
#list_of_tuples = [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x')]


def duplicate_list_of_tuples(list_of_tuples):
  #if no duplicate tuples there if will return "No Duplicate"
  flag = False;
  #iterate tuples, excluding duplicate
  for (i,j) in set(list_of_tuples):
    #it will count number of tuples present in the set
    count = list_of_tuples.count((i,j))
    if(count > 1):
      flag = True;
      print((i,j),"-",count)
  if flag is False:
    print("No Duplicate")

list_of_tuples = [('a', 'e'), ('b', 'x'), ('b', 'x'), ('a', 'e'), ('b', 'x')]   
duplicate_list_of_tuples(list_of_tuples);  

#method 2:
dict_res = {}
for i in list_of_tuples:
  dict_res[i] = dict_res.get(i,0) + 1;
    
    
print(dict_res)
