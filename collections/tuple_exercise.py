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

