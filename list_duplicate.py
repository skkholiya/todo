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





