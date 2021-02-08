#4 types of collection in python (list,tuple,set,dict)
#list: store multiple values in a single variable.
#list is a collection which is ordered,changable,mutable,allows duplicate)

print("---------------------- list collection ------------------------------")
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
print("--------------------------- tuple collection -------------------------");
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


#python collections part(3) set: is a collection which is unorderd, mutable(but can add items once declared), allows duplicate.
print("------------------------------ set collection -------------------------------");

#set constructor
language_set = set(("java","python","c#"));
print("set constructor",language_set);

#add items to set
language_set.add("javaScript");
print("adding items to set:",language_set);

#add items from another set
frameworks = {"spring", "django", "flask"}
language_set.update(frameworks);
print("add frameworks:", language_set);

#set methods python

#clear(): no-args, return empty set
print("clear():",frameworks.clear());

#copy(): no-args, copies orignal set items to current set
copy_set = language_set.copy()
print("copy():",copy_set)

#differece: one-arg set.difference(set(R)), return set, return a new set contains items that exists in first set, duplicate items removed.
fruits = {"apple","cherry","banana"}
it = {"google","apple","microsoft"}
difference_set = fruits.difference(it)
print("difference():", difference_set);

#difference_update: one-arg, set.difference_update(set(R)), return set, update the first set remove elements present in both set.
copy_set = fruits.copy();
copy_set.difference_update(it);
print("difference update", copy_set);

#discard: one-arg, set.discard(element(R)), return set, remove item from set if present, otherwise return none.
copy_set.discard("banana")
print("discard():",copy_set);

#remove: one-arg, set.remove(element(R)), return set, remove item from set if present, otherwise return exception.
copy_set.remove("cherry");
print("remove():",copy_set);

#intersection: one-arg, set.intersection(set(R)), return a new set, return elements present in both set.
intersect = fruits.intersection(it);
print(intersect);

#intersection_update: multiple-args, set.intersection_update(set1(R),set2(O).....), return set, update the first set, contains
#items present in both set.
copy_fruits = fruits.copy()
copy_fruits.intersection_update(it);
print("intersection_update():",copy_fruits);

#isdisjoints(): one-arg, set.isdisjoints(set1(R)), return boolean, return true if both set doesn't have any common items present.
x={"a","b","c"}
y={"c","f","e","d","a","x","b","c"};
print("isdisjoint():",x.isdisjoint(y));

#issubset(): one-arg, set.issubset(set1(R)), return boolean, return true if all items in the set exists in specified set.
print("issubset():", x.issubset(y));

#issuperset():one-arg, set.issuperset(set1(R))), return boolean, return true if all items in the sepecifed set exists in the original set.
print("issuperset():", y.issuperset(x));

#pop(): no-arg, return none, remove random element from the set.
y.pop();
print("pop():", y);

#symmetric_difference(): one-arg,symmetric_difference(set1(R)), return a new set contain element that are not present in both set, 
first_set = x.copy()
y_copy = y.copy()
symmetric_difference = first_set.symmetric_difference(y);
print("symmertric_differece():", symmetric_difference);

#symmetric_difference_update(): one-arg, set.symmetric_difference_update(set1(R)), return a first set elements not present in both set.
first_set.symmetric_difference_update(y_copy)
print("symmetric_difference_update():",first_set);

#union(): multiple-arg, set1.union(set2(R)), set1.union(set2(R),set2(O)...), return a new set of all elements present in original set and all elements present in specified set,if duplicate, will appear only once (Join two sets).
union_set = x.union(y);
print("union():",union_set);


