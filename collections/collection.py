#4 types of collection in python (list,tuple,set,dict)
#list: store multiple values in a single variable.
#list is a collection which is ordered,changable,mutable,allows duplicate)

list_ex=["ordered","changable", "mutable", "allow duplicate"]


#List comprehension: provieds shorter syntax if we want to create a new list with an existing list.
new_list = [ outcome for outcome in list_ex if outcome !="mutable"]
print(new_list);

#Loop through a list
for index in range(len(new_list)):
  print(new_list[index]);
  
  
#List methods:

#append(): 1-args,append(element(R)), return list, add a new element at the end of the list.
list_industry = ["hollywood", "bollywood"]
list_industry.append("tollywood");
print("append():",list_industry);

#clear(): no-args, return list, return a empty list
clear_list= list_industry.clear();
print("clear():", clear_list);

#count(): 1-args, list.count(element(R)), return int, number of times occur the specified element in a list
list_count = [1,2,3,6,8,5,7,8,9];
print("count():",list_count.count(8));

#extend(): 1-args, list.extend(iterable(R)(list,tuple,set etc.)), return list, add element to current list at the end.
print("extends()",list_count.extend("string"));

#index(): 1-args, list.index(element(R)), return int, first occurrence of the element into the list.
list_lang = ["python", "java", "rust", "javascript"]
print("index():",list_lang.index("rust"));

#insert(): 2-args, list.insert(position(R),element(R)), return list, insert specified element to specified position
list_lang.insert(2,"c-sharp")
print("insert():", list_lang);

#pop(): 1-args, list.pop(index(O)), return removed element, remove element based on specified index, by default -1
print("pop():",list_lang.pop());

#remove(): 1-args, list.remove(element(R)), return none, remove elment based on specifed value/element.
print("remove()",list_lang.remove("rust"));

#copy(): create a copy of existing list
copy_list= list_lang.copy();
print("copy():",copy_list);

#reverse(): reverse order of element in the list.
copy_list.reverse();
print("reverse()", copy_list);

#sort(): 2-args, list.sort(reverse = True/False(default False), key= any function), return sorted list
#sort the list asc order by default
#customzied sorting done by the key(pass any function)

#sort the string list based on length
def sort_len(x):
  return len(x)
  
sort_names = ["Kaira will","Harvey V","Jason Roy","Carey S"]
sort_names.sort(key=sort_len);

print("sort():", sort_names);


'''
collection part 2 - Tuple: is a collection which is sorted, immutable and allows duplicates.

define, access, change, update, delete, unpack, join, multiply, methods tuple.
'''
#Defining a tuple
languages = ("java","python","c-sharp","rust")

#Accessing elements from tuple
print("Accessing second and third element from tuple:",languages[-3:-1]);

#changing values of tuple
tuple_integers = (1,3,5,6,4,3);
print("orginal tuple:",tuple_integers);
tuple_to_list = list(tuple_integers);
tuple_to_list.append(8);
tuple_integers = tuple(tuple_to_list);
print("append items to tuple:",tuple_integers);

#removing element from tuple
remove_tuple_item = list(tuple_integers);
remove_tuple_item.pop();
tuple_integers = tuple(remove_tuple_item);
print("removing last element from tuple:", tuple_integers);

#changing values of tuple
update_tuple = list(tuple_integers);
update_tuple[1] = 2;
tuple_integers = tuple(update_tuple);
print("second elmenent update in tuple:", tuple_integers);

#deleting the tuple
tuple_delete_ex = ("tim", "lee", "susan")
print("before deleting the tuple:",tuple_delete_ex);
del tuple_delete_ex;


#unpacking tuples elements: allows you to extract values from tuple to variables
technologies = ("spring", "react","angular","vue.js","django");
backend_java, *frontend, backend_python = technologies;

print("java backend:",backend_java);
print("frontend technologies:", frontend);
print("backend_python:", backend_python);
i=0;
print("loop through a tuple using while");  
while i < len(technologies):
  print(technologies[i]);
  i+=1;

#joining tuples
tuple_of_integers = (1,2,3,4,5,5)
tuple_of_txt = ("one","two","three","four","five")
joining_tuples = tuple_of_integers + tuple_of_txt;

print("joining tuples:",joining_tuples);

#multiplying tuples elements(2 time's)
print("multiplying tuples elements 2 times:", tuple_of_integers *2);

#tuple methods: 2 built-in python method's

#1- count(): 1-args, tuple.count(element(R)), return int, count number of times element occurs in tuple
print("count(), number of times 5 occurs in tuple:",tuple_of_integers.count(5));

#2- index(): 1-args, tuple.index(element(R)), return int, return the first index position of specified value occurs in tuple.
print("index(), element 5 index position:",tuple_of_integers.index(5));







