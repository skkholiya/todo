import collections
from collections import defaultdict
import itertools
import json
#Dictionary Question
#1. Write a Python program to sort (ascending and descending) a dictionary by value.
dict_ex = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
asc_order = sorted(dict_ex.items(),key = lambda x:x[1])
desc_order = sorted(dict_ex.items(),key = lambda x:x[1], reverse=True)
print(asc_order);
print(desc_order);




#2. Write a Python script to add a key to a dictionary.
dict_ex = {0: 10, 1: 20}
dict_ex.setdefault(1,20);
#dict_ex[2] = 30;
print(dict_ex);




#3. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d4 = {}
for i in (dic1,dic2,dic3):
  d4.update(i)
print(d4)




#4. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def check_key_present(x):
    print("Key Present in Dictionary") if x in d else print("Key Not Present")

check_key_present(3)
check_key_present(8)


#5. Write a Python program to iterate over dictionaries using for loops.

dic_ex = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for (key,value) in dic_ex.items():
  print("key:",key,"value:",value);
  
  
#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5;
return_dic = {}
for i in range(1,n+1):
  return_dic.setdefault(i,i*i);
print(return_dic);



#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
return_dict = {}
for i in range(1,16):
  return_dict[i]=i**2;
print("1 to 15 keys and values are square:",return_dict);  



#8. Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print("Merged Dictionary:",d);




#9. Write a Python program to iterate over dictionaries using for loops. 
dict_ex =  {'Red': 1, 'Green': 2, 'Blue': 3} 
for key,value in dict_ex.items():
  print("key:", key, " value:",value);




#10. Write a Python program to sum all the items in a dictionary.
sum_dic = {"apple":555,"oppo":400,"MI":300}
sum_values = 0;
for i in sum_dic.values():
  sum_values += i;
print("sum of dict values:",sum_values);



#11. Write a Python program to multiply all the items in a dictionary.
mul_dic = {"apple":555,"oppo":400,"MI":300}
multiply = 1;
for i in mul_dic.values():
  multiply *= i;
print("multiplication of dict values:", multiply);




#12. Write a Python program to remove a key from a dictionary. 
remove_dic = {"apple":555,"oppo":400,"MI":300}
#remove mi from dic
remove_dic.pop("MI");
print("mi brand removed from dict",remove_dic)




#13. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

dict_colors = dict(zip(keys,values))
print(dict_colors);




#14. Write a Python program to sort a dictionary by key. 
dict_sort = {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'};
dict_sort_key=sorted(dict_sort.items());
print(dict_sort_key)




#15. Write a Python program to get the maximum and minimum value in a dictionary. 
sample_dic = {"apple":555,"oppo":400,"MI":300}
print("max value", max(sample_dic.values()));
print("min value:", min(sample_dic.values()));



#16. Write a Python program to get a dictionary from an object's fields.
class Person:
  def __init__(this,name,age,city):
    this.name = name;
    this.age = age;
    this.city = city;
    
person = Person("rahul",24,"delhi")
print(person.__dict__);


#17 Write a Python program to remove duplicates from Dictionary. 
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

dic_return = {}
for k,v in student_data.items():
  if v not in dic_return.values():
    dic_return[k] = v;

print(dic_return);



#18. Write a Python program to check a dictionary is empty or not.
dic = {1:"ajay",2:"aamir",3:"bishu"}
#if not bool(my_dict)
print(dic.items()) if len(dic)>0 else print("Empty Dictionary")



#19. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = collections.Counter(d1)
d4 = collections.Counter(d2)
new_dic = d3+d4;
print(new_dic);




#20. Write a Python program to print all unique values in a dictionary.
value_in_dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}];
unique_value_dic = set(k for i in value_in_dic for j,k in i.items());
print("20.dict",unique_value_dic) #o/p {'S002', 'S007', 'S009', 'S001', 'S005'}



#21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
com_dic =  {'1':['a','b'], '2':['c','d']}
for i in itertools.product(*[com_dic[i] for i in com_dic.keys()]):
  print(''.join(i));



#22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary. 
dic = {1:3,2:4,6:4,3:9,5:3}
sort_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
for (i,j) in sort_dic[:3]:
 print(i)



#23. Write a Python program to combine values in python list of dictionaries.
list_of_dic = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
x=collections.Counter();
for i in list_of_dic:
  x[i['item']] += i['amount']

print(x);



#24. Write a Python program to create a dictionary from a string.
string_ex = 'w3resource'
to_dict = dict({i,string_ex.count(i)} for i in string_ex)
print("24.",to_dict);



#25. Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print ("{:<10} {:<10} {:<10}".format(*my_dict.keys()))
for k,v in my_dict.items():
  C1,C2,C3 = v;
  print("{:<10} {:<10} {:<10}".format(C1,C2,C3));




#26. Write a Python program to count the values associated with key in a dictionary. 
student = [
 {'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

print("count id values",sum(i['id'] for i in student))
print("count success value", sum(i['success'] for i in student));



#27. Write a Python program to convert a list into a nested dictionary of keys.
list_num = [1, 2, 3, 4]
convert_dic = current= {}
for i in list_num:
  current[i] = {}
  current = current[i]

print("27.",convert_dic);




#28. Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sort_num = {x : sorted(y) for x,y in num.items()}
print(sort_num)



#29. Write a Python program to remove spaces from dictionary keys.
dic_ex = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
return_dict = {}
for i,j in dic_ex.items():
  key_ = i.replace(" ","")
  return_dict[key_]=j;
  
print(return_dict);



#30. Write a Python program to get the top three items in a shop.
sample_data = {'item1': 45.50, 'item2':35,'item4':55, 'item3': 41.30,  'item5': 24}
x = sorted(sample_data.items(),key = lambda x:x[1],reverse= True);
print(x[:3]);



#31. Write a Python program to get the key, value and item in a dictionary. 
sample_data = {'item1': 45.50, 'item2':35,'item4':55, 'item3': 41.30,  'item5': 24}
for key,value in sample_data.items():
  print("item:",(key,value),"key",key,"value",value);
  
  
#32. Write a Python program to print a dictionary line by line.
nested_dic =  {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}  
        
for key,value in nested_dic.items():
  print(key);
  for i,j in value.items():
    print(i,j);
 
 
 
    
#33. Write a Python program to check multiple keys exists in a dictionary.
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

print(student.keys() >= {'name','class'});
print(student.keys() >= {'name','alex'});
print(student.keys() >= {'name','roll_id'});




#34. Write a Python program to count number of items in a dictionary value that is a list.
dict_ =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count = 0;
for value in dict_.values():
  for i in value:
    count +=1;
    
print(count);




#35. Write a Python program to sort Counter by value.
xx={'Math':81, 'Physics':83, 'Chemistry':87}
x= sorted(xx.items(),key= lambda x:x[1],reverse = True);
print(x)



#36. Write a Python program to create a dictionary from two lists without losing duplicate values.
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
d = defaultdict(set)
for i,j in zip(class_list,id_list):
  d[i].add(j);  
print(d)



#37. Write a Python program to replace dictionary values with their average.
score ={'Math':81, 'Physics':83, 'Chemistry':87}
avg = int(sum(score.values())/len(score))
return_lis = {}
for i in score.keys():
  return_lis[i] = avg;  
print(return_lis)




#38. Write a Python program to match key values in two dictionaries. 
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key,value in set(x.items()) & set(y.items()):
  print(key,"present in both dict.")
  
  

#39. Write a Python program to store a given dictionary in a json file.
d = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
"teachers":[{"firstName": "Amberly", "lastName": "Calico"},
         {"firstName": "Regine", "lastName": "Agtarap"}]}
         
         
to_json = json.dumps(d)
print(type(to_json))




#40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
eg_dic = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}

for value in eg_dic.values():
  if isinstance(value,list) and len(value)>=4:
    print(value[4])
    
    
#41. Write a Python program to drop empty Items from a given Dictionary.    
dic = {'c1': 'Red', 'c2': 'Green', 'c3': None}
return_dic = {k:v for k,v in dic.items() if v is not None}
print(dic)


#42. Write a Python program to filter a dictionary based on values.
name_dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
return_greater_175 = filter(lambda x: x[1]>170,name_dic.items())
print(dict(return_greater_175))



#43. Write a Python program to convert more than one list to nested dictionary.
l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]

dictionary = {k:{sk:sv} for k,sk,sv in zip(l1,l2,l3)}
print(dictionary);



#44. Write a Python program to filter the height and width of students, which are stored in a dictionary.
dic_of_tuple_value = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
filter_object = {k:v for k,v in dic_of_tuple_value.items() if v[0]>= 6.0  and v[1]>=70}
print(filter_object)



#45. Write a Python program to check all values are same in a dictionary.
check_value = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
specified_value = 12
equal_12 = all(True if v == specified_value else False for k,v in check_value.items())
print(equal_12);


#46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
lis_of_tuple = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
group_dic = {}

for i,k in lis_of_tuple:
  group_dic.setdefault(i,[]).append(k);

print(group_dic);



#47. Write a Python program to split a given dictionary of lists into list of dictionaries. 
def list_of_dic(dic):
  keys = dic.keys(); 
  values = zip(*[ dic[key] for key in keys])
  result = dict(zip(keys,v) for v in values )
  return result;

dic_ex = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(list_of_dic(dic_ex))


#48. Write a Python program to remove a specified dictionary from a given list. 
list_of_dic = [ {'id': '#800000', 'color': 'Maroon'}, {'id': '#FF0000', 'color': 'Red'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]

remove_id = '#FF0000';

def remove_item(lis,key):
  lis[:] = [dic for dic in lis if dic.get('id') != key]
  return lis;
print(remove_item(list_of_dic,remove_id));



#49. Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
original_list = [{'x': '10', 'y': '20', 'z': 30}, {'p': '40', 'q': '50', 'r': '60'}]

number_values = [{k:int(v) for i in original_list for k,v in i.items()}]
print(number_values);



#50. A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary.
dic_eg =  {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
clear_values = {}
for k,v in dic_eg.items():
  if isinstance(v,list):
    v = [];
print("50.",dic_eg);



#51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
dic = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

def update_dict(dic):
  dic['Math'] = [i+1 for i in dic['Math']]
  dic['Physics'] = [i-2 for i in dic['Physics']]
  return dic;

print(update_dict(dic));



#52. Write a Python program to extract a list of values from a given list of dictionaries.

list_of_dic = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
key = "Science"
def extract_value(lis, key):
  lis = [i[key] for i in lis if key in i]
  return lis;  

print(extract_value(list_of_dic, key));



#53. Write a Python program to find the length of a given dictionary values.
dic_value = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
return_dic = {v:len(v) for k,v in dic_value.items()}
print(return_dic)


# ! 54. Write a Python program to get the depth of a dictionary.
dic = {'a':1, 'b': {'c': {'d': {}}}}

def dic_depth(dic):
  if isinstance(dic,dict):
    
    return 1 #+ (max(map(dic_depth, dic.values())) if d else 0)
  else:
    return 0
    
print(dic_depth(dic));



#55. Write a Python program to access dictionary key's element by index. 
num = {'physics': 80, 'math': 90, 'chemistry': 86}
ls = list(num)
for i in range(0,len(ls)):
  print(ls[i]);
  
  
  
#56. Write a Python program to convert a given dictionary into a list of lists.
dic = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}  

def dic_to_list_of_lists(dic):
  return [[k,v] for k,v in dic.items()]  
print(dic_to_list_of_lists(dic));  





#57. Write a Python program to filter even numbers from a given dictionary values. 
filter_ex = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
res = {k:[s for s in v if s%2==0] for k,v in filter_ex.items()}
print(res)



#58. Write a Python program to get all combinations of key-value pairs in a given dictionary.
combination = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

for k in itertools.combinations(combination.items(),2):
  print(dict(k))
  

#59. Write a Python program to find the specified number of maximum values in a given dictionary.  
dic = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
sort = dict(sorted(dic.items(),key=lambda x : x[1],reverse= True))
print("#1 maximum value(s) in the said dictionary:")
print(list(sort)[:1]);
print("#2 maximum value(s) in the said dictionary:")
print(list(sort)[:2]);
print("#5 maximum value(s) in the said dictionary:")
print(list(sort)[:5]);


#60. Write a Python program to find shortest list of values with the keys in a given dictionary.
dictt = {
 'V': [10, 12],
 'VI': [10],
 'VII': [10, 20, 30, 40],
 'VIII': [20],
 'IX': [10,30,50,70],
 'X': [80]
 }

def shortest_list(dic):
  return [k for k,v in dic.items() if len(v) == 1 ]

print(shortest_list(dictt))



#61. Write a Python program to count the frequency in a given dictionary. 
dic = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
value_frequency = collections.Counter(dic.values())
print(value_frequency)



#62. Write a Python program to extract values from a given dictionaries and create a list of lists from those values.
ex = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

list_of_items = [ [v for k,v in i.items()]  for i in ex if i.keys() ] 
print(list_of_items)

list_of_values = [ [v for k,v in i.items() if k in('student_id','name')]  for i in ex if i.keys() ] 
print(list_of_values);

name_class = [ [v for k,v in i.items() if k in('class','name')]  for i in ex if i.keys() ] 
print(name_class);


#63. Write a Python program to convert a given list of lists to a dictionary.
lis_eg=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

def list_to_dic(lis):
  return {i[0]:i[1:] for i in lis}

print("63",list_to_dic(lis_eg))


#64. Write a Python program to create a key-value list pairings in a given dictionary.
dic_eg = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

def convert_to_dict(eg):
  eg_r = {}
  for k,v in dic_eg.items():
    eg_r[k] = "".join(v)
  return eg_r;

print(convert_to_dict(dic_eg))



#65. Write a Python program to get the total length of all values of a given dictionary with string values.
dic = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

def len_dic_value(dic):
  count = 0;
  for v in dic.values(): count += len(v)
  return count
  
print(len_dic_value(dic));



#66. Write a Python program to check if a specific Key and a value exist in a dictionary.


students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]


def check_dic_item(ex,key,value):
  
  return any([True for i in students if key in i.keys() and value in i.values()])

key = 'name'
value = 'Lynne Foster'
print(check_dic_item(students,key,value))
print(check_dic_item(students,'student_id', 1))
print(check_dic_item(students,'name', 'Brian Howell'))
print(check_dic_item(students,'class', 'VII'))
print(check_dic_item(students,'class', 'I'))
print(check_dic_item(students,'name', 'Brian Howelll'))
print(check_dic_item(students,'student_id', 11))
