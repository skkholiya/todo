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

