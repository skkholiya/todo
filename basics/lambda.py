#lambdas are anonynomous function can have multiple arguments but only one expression
#syntax: lambda argument1,argument2: expresssion
#common use of lambda as anonynomous function inside a function.

#Lambda Exercise

#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

x= lambda x: x+15;

y= lambda x,y: x*y;

print("add 15",x(10));
print("multiply two nums:", y(12,4))


#2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

def multiply(num):
	return lambda x:x*num;

number = multiply(15);
double_number = number(2);
print("double of number",double_number);
print("triple of number",number(3));
print("Quadtriple of number", number(4));
print("Quintuple of number", number(5));

'''3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
orignal_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)];
orignal_list = sorted(orignal_list, key= lambda x:x[1])
print("sort list of tuples marks in asc order:", orignal_list);

'''
4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''
list_of_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

list_of_dict = sorted(list_of_dict,key= lambda x:x['color'])
print(list_of_dict);

'''
5. Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
eg_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
even_numbers = list(filter(lambda x:x%2==0,eg_list))
odd_numbers = list(filter(lambda x:x%2!=0,eg_list));

print(even_numbers)
print(odd_numbers)

#6. Write a Python program to square and cube every number in a given list of integers using Lambda.

list_of_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
cube_of_everyNum = list(map(lambda x: x**3,list_of_int));
print("cube:",cube_of_everyNum);
square = list(map(lambda x:x*x,list_of_int));
print("square:",square);

#7. Write a Python program to find if a given string starts with a given character using Lambda. 
inp_str = "suresh"
start_with_s = lambda x:True if x.startswith("c") else False
print(start_with_s(inp_str))

#9. Write a Python program to check whether a given string is number or not using Lambda.
isdigit_ex = "12345z"
outPut = lambda x:True if x.isdigit() else False
print(outPut(isdigit_ex));

#10. 10. Write a Python program to create Fibonacci series upto n using Lambda.
n = 9
list_=[]
a=0;
b=1;
list_.append(a)
list_.append(b)
for i in range(n-2):
  c = a+b;
  list_.append(c);
  a=b;
  b=c;
print(list_)
#print("fibonacci:",fibonacci)
