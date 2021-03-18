#1. Write a Python program to calculate the length of a string.
def string_length(txt):
  count = 0;
  for i in txt:
    count+=1;
  return count;
  
print(string_length("vaco binary"))


#2. Write a Python program to count the number of characters (character frequency) in a string.
def num_of_char(txt):
  to_dic = {}
  for i in txt:
    count = 1;
    if i in to_dic:  
      to_dic[i] = to_dic.get(i) + 1;
    else:
      to_dic[i] = count;
  return to_dic;
  
txt = 'google.com'
print(num_of_char(txt))



#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def two_right_left(txt):
  if len(txt)<2:
    return "Empty String"; 
  start = txt[:2]
  end = txt[-2:]
  return start+end;  
txt = "john wick"
print(two_right_left(txt))



#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def replace_char(txt):
  result = txt[0]  
  txt = txt.replace(result,"$")
  result += txt[1:]
  return result;

print(replace_char("restart"))


#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

x = 'abc'
y = 'xyz'

def replace_first_two(x,y):
  k = y[:2] + x[2:]
  l = x[:2] + y[2:]
  return k+" "+l;
  
print(replace_first_two(x,y));


#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def update_string(txt):
  if len(txt) >= 3 and txt.endswith('ing'):
    return txt+'ly'
  
  elif len(txt) < 3:
    return txt;
  
  else:
    return txt+'ing'
  
x = "abc"
print(update_string(x))



#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

sample_str = 'The lyrics is not that poor!'
def check_in_substring(string):
  first = string.find("poor")
  last = string.find("not")

  if first>0 and last>0:
    string = string.replace(string[last:(first+4)],'good')
    return string
    
  else:
    return string
    
    
print(check_in_substring('The lyrics is not that poor!'))
print(check_in_substring('The lyrics is poor!'))



#8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one.
ls = ["PHP", "Exercises", "Backend"]
def longest_word_length(ls):
  res= [] 
  for i in ls:
    res.append(len(i))    
  return max(res);

print(longest_word_length(ls));


#9. Write a Python program to remove the nth index character from a nonempty string.
def remove_char(txt, index):
  if len(txt)<0 or index<0 or index>len(txt):
    return
  else:
    x = txt.replace(txt[index],"",1)
    return x;

print(remove_char('Python', 0))


#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 
def interchange_last_first(txt):
  first = txt[:1]
  last = txt[-1:]
  
  return last+txt[1:len(txt)-1]+first;
print(interchange_last_first("12345"));


#11. Write a Python program to remove the characters which have odd index values of a given string.
def remove_alternate(txt):
  return txt[::2]
  
print(remove_alternate("abcdef"))
  

#12. Write a Python program to count the occurrences of each word in a given sentence.
sen = 'the quick brown fox jumps over the lazy dog.'

def word_count(sen):
  res = {}
  for i in sen.split():
    count = 1;
    if i in res:
      res[i] = res.get(i) + 1;
    else:
      res[i] = count
  return res;
  

print(word_count(sen))


#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
def convert_to_cases(txt="defalut value"):
  print("toUppercase",txt.upper());
  print("toLowercase",txt.lower());
  
#user_input = str(input())
#convert_to_cases(user_input);


#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

def unique_sorted_list(txt):
  x = sorted(txt)
  return ",".join(x)

#x = input()
#print(unique_sorted_list(i for i in x.split(",")))


#15. Write a Python function to create the HTML string with tags around the word(s).
def create_html_tags(tag, body):
  return "<"+tag+">"+body+"</"+tag+">"
  
  
print(create_html_tags('i', 'Python'))
print(create_html_tags('b', 'Python Tutorial'))


#16. Write a Python function to insert a string in the middle of a string.
def insert_string_middle(input_string, word):
  return input_string[:2] +word+ input_string[-2:] 
print(insert_string_middle("[[]]","Python"))



#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def insert_end(txt):
  return txt[-2:] *4
  
print(insert_end("Exercises"));
