from copy import deepcopy

#Tuple Questions


#1. Write a Python program to create a tuple.
empty_tuple = tuple()
print(empty_tuple)


#2. Write a Python program to create a tuple with different data types.
ls = [3,4,5,6]
st = {4,5,True,"String"}
es = tuple(st)
print(es);



#3. Write a Python program to create a tuple with numbers and print one item.
tuple_ex = (1,2,3,4,5)
print(type(tuple_ex));
tuple_with_one_item = (1,);
print(tuple_with_one_item)



#4. Write a Python program to unpack a tuple in several variables.
unpack_ex = ("Ramish","delhi",35,"Male","Married")
name, city, age, *extra = unpack_ex;
print(name,city,age, extra);



#5. Write a Python program to add an item in a tuple.
add_list_tuple = 5
my_tuple = (7,8,9,10)
add_item = list(my_tuple)
add_item.append(add_list_tuple)
my_tuple = tuple(add_item)
print(my_tuple)



#6. Write a Python program to convert a tuple to a string.
my_tuple1= ('h','e','l','l','o')
tuple_to_string = "".join(my_tuple1);
print(tuple_to_string)


#7. Write a Python program to get the 4th element and 4th element from last of a tuple.
my_tuple2= (1,2,3,4,5,6)
#from first
print("fromfirst",my_tuple2[3])
#from last
print("from last",my_tuple2[-3])



#8. Write a Python program to create the colon of a tuple.
tuplex = ("HELLO", 5, [], True) 
copy_tuplex = deepcopy(tuplex)
print(copy_tuplex);


#9. Write a Python program to find the repeated items of a tuple.
tuple_x = 2, 4, 5, 6, 2, 3, 4, 4, 7;
ele = 4;
count_4 = tuple_x.count(ele);
print(count_4);



#10. Write a Python program to check whether an element exists within a tuple. 
tupley = 4,3,5,6,7,2,1,9
elem = 85;
print(elem,"present in tuple") if elem in tupley else print(elem,"not present in tuple")



#11. Write a Python program to convert a list to a tuple.
listx= ["raj",33,"Male","Delhi",True]
convert_to_tuple = tuple(listx)
print(convert_to_tuple);


#12. Write a Python program to remove an item from a tuple. 
tuplex = 4,3,5,6,7,2,1,9
remove_ele = 5
remove_item_from_tuple = tuple(i for i in tuplex if i!=remove_ele)
print(remove_item_from_tuple);


#13. Write a Python program to slice a tuple.
tuple_eg = ("raj",33,"Male","Delhi",True)
#print element after every two element
print(tuple_eg[::2])

#Slice through negative indexing.
print(tuple_eg[-3:])


#14. Write a Python program to find the index of an item of a tuple.
tuple_eg = ("raj",33,"Male","Delhi",True)
find_index_delhi = tuple_eg.index("Delhi");
print("14. index of delhi in tuple:",find_index_delhi)



#15. Write a Python program to find the length of a tuple.
tuple_eg = tuple("tuple_exercise")
print("15. length of tuple:",len(tuple_eg));



#16. Write a Python program to convert a tuple to a dictionary. 
tuple_ex = (("jay",43),("raj",43))
print(type(tuple_ex))
tuple_to_dic = {i:j for (i,j) in tuple_ex}
print(tuple_to_dic)



#17. Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))



#18. Write a Python program to reverse a tuple.
l = [(1,2), (3,4), (8,9)]
print(sorted(l,reverse=True))




#19. Write a Python program to convert a list of tuples into a dictionary.
list_of_dic = [("kaira",44),("tim",32)]
list_dic = {x:y for x,y in list_of_dic}
print(list_dic)



#20. Write a Python program to print a tuple with string formatting.
tuple_eg = (100, 200, 300)

print("This is a tuple {}".format(tuple_eg));



#21. Write a Python program to replace last value of tuples in a list. 
eg_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
replaced_value = (100,);
tuple_lis = [t[:-1] + replaced_value for t in eg_list]
print(tuple_lis)


#22. Write a Python program to remove an empty tuple(s) from a list of tuples.
lis_of_tupl = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
remove_empty = [i for i in lis_of_tupl if len(i) > 0]
print(remove_empty)



#23. Write a Python program to sort a tuple by its float element. 
sort_tuple_eg = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sort_tuple_eg.sort(key = lambda x:x[1], reverse = True);
print(sort_tuple_eg)



#24. Write a Python program to count the elements in a list until an element is a tuple. 
lst_tple = [10,20,30,(10,20),40]
count = 0;
for i in lst_tple:
  if isinstance(i,tuple):
    break
  count +=1;

print(count);


#25. Write a Python program convert a given string list to a tuple.
string = 'python 3.0'
string_to_tpl = tuple(i for i in string)
print(string_to_tpl)


#26. Write a Python program calculate the product, multiplying all the numbers of a given tuple.
tupl_multiply = (4, 3, 2, 2, -1, 18)

def multiplication(x):
  multiplication = 1;
  for i in tupl_multiply:
    multiplication *= i
  return multiplication; 
  
print(multiplication(tupl_multiply));



#27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.

def avg_of_tuples(tupl):
  tupl_list = [];
  for sub_tupl in zip(*tupl):
    tupl_list.append(sum(sub_tupl)/len(sub_tupl))
    
  return tupl_list;

avg_of_tuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

print(avg_of_tuples(avg_of_tuple));



#28. Write a Python program to convert a tuple of string values to a tuple of integer values.
tuples_of_string =  (('333', '33'), ('1416', '55'))
tuples_of_int = tuple(tuple(int(j) for j in i) for i in tuples_of_string )
print(type(tuples_of_int))
print(tuples_of_int);



#29. Write a Python program to convert a given tuple of positive integers into an integer.
tupl_of_int =  (10, 20, 40, 5, 70)
join_to_string = "".join(str(i) for i in tupl_of_int if isinstance(i,int))
print((join_to_string))




#30. Write a Python program to check if a specified element presents in a tuple of tuples.
tupl_of_tupls = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))


def isTuplePresent(tupls,value):
  return any(True for i in tupls if value in i)


print(isTuplePresent(tupl_of_tupls,"White"));



#31. Write a Python program to compute element-wise sum of given tuples.
l1 = (1, 2, 3, 4)
l2 = (3, 5, 2, 1)
l3 = (2, 2, 3, 1)

sum_of_cols = tuple(int(c1+c2+c3) for c1,c2,c3 in zip(l1,l2,l3))
print(sum_of_cols)



#32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
summation = [(1, 2), (2, 3), (3, 4)]
result = [ sum(i) for i in summation]
print(result);
