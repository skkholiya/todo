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





