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






def sum_two_large_numbers(str1,str2):
  str1_len = len(str1)-1;
  str2_len = len(str2)-1;

  result="";

  carry =0;

  while str1_len >= 0 or str2_len >=0:
  
    #ternary operator: a if condition else b
  
    digit1 = (ord(str1[str1_len]) - 48) if str1_len > -1 else 0;
    digit2 = (ord(str2[str2_len]) - 48) if str2_len > -1 else 0;
  
    sum = digit1 + digit2 + carry;
  
    add = int(sum%10);
  
    result += str(add);
  
    carry = int(sum / 10);
  
    str1_len -= 1;
    str2_len -= 1;

  if carry!=0:
    result += str(carry);


  return result[::-1];


str1="58973498573498600";

str2 = "4534635465654";
print(sum_two_large_numbers(str1,str2));
