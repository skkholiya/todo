#timestamp: Jan 29 11:22
import random
#Arithmatic Operation in python
#adding
add=5+4;
add1=6+add;
print(add);
print("addition",add1);

#subtraction
subtract= 340-3;
subtract1= subtract-54;
print("subtraction",subtract1);

#multiplication
multiply=44*3;
multiply_with_4=multiply*4;
print("multiplication",multiply_with_4);

#division
division=55/5;
division_by_two=division/2;
print("division",division);

#round off of a number
value=43;
round_off=value//2
print("round off:",round_off);

#find power of a number
Three_to_power_5= 3**5;
print("3 to power 5:",Three_to_power_5);

#strings in python
single_quote_string = 'hey, how are you';

double_quote_string = "hey, there";

string_inside_string = 'fine,"how about you"';

string_with_special_char = r'https://localhost:8080/api';

string_single_quote= 'hey, i\'m just text checking'

multiline_string = """Hey, How are you
			      I am fine what about you
		    """


#strings are array in python 

print("single quote string",single_quote_string);

print("double quote string",double_quote_string);

print("string inside string",string_inside_string);

print("string with special char",string_with_special_char);

print("string single quote", string_single_quote);

print("multilne string",multiline_string);

#Slicing in string(return range of characters)
slice_example = "hello, world";
print("start the string after 2nd index",slice_example[2:]); #o/p - llo,world

print("slicing between",slice_example[8:10]); #o/p - or

print("remove the last element",slice_example[:-2]); #o/p- hello, wor

last_half = int(len(slice_example)/2);
print("last half",last_half);

print("display the last half of total string length",slice_example[last_half:]);

print("negative indexing",slice_example[-9:-3]); # o/p = lo, wo



#in operator in python
print("in operator","you" in multiline_string); 

#Data Types in python
int_data_type=4;
float_data_type=5.4;
string_data_type="hello";
complex_data_type= 1j; #it is a combination of m+n where m is the int and n is the imaginary part
list_data_type= [4,3,5,8]; #list data type is mutable in nature
tuple_data_type= ("alex","tim","lee","steve"); # tuple is immutable in nature and we can use tuple in the dict as keys.
range_data_type= range(6) #takes three parameter, start(optional by default 0), end(required ), steps(optional by default 1)
set_data_type= {"john","will","pope","kim"} #set doesn't contain duplicate and mutable in nature
frozenset_data_type = frozenset({"luna","helan","smith"});
mapping_data_type = {3:"apple",4:"banana",1:"orange"};
bytes_data_type = b'hello'; #return the bytes object and immutable in nature
bytearray_data_type = bytearray(8); #return the bytesarray object takes 3 optional parameter(source,encoding,errors) also apply for bytes()
memoryview_data_type = memoryview(bytearray("abe",'utf-8'));
boolean_data_type = True;

print(*memoryview_data_type); #print the ascii index store by the bytearray



#if else 
a=2
b=5
if a>b:
  print(a," is greater than ",b);
else:
  print(b," is greater than ",a);  
  
  
