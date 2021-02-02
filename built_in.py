txt = " Hello, world ";
txt_str = "hello";
txt_with_number = "{1} dollar price is {0} INR";
dollar=2
price=75.00*dollar;

#multiplication of string
print(txt_str*3);

#format method used include numbers in string
print(txt_with_number.format(price,dollar));

#uppar: convert string to upper case
print(txt.upper());

#lower: convert string to lower case
print(txt.lower());

#strip: remove whitespaces from both end of string;
print(txt.strip());

#split: split string into substring using separator if available and reutrn list.
print(txt.split(","));

#replace: replace the character within a string,return string
print(txt.replace("H","K"));

print("after case fold"+txt);

#concatenation: combine two or more string together.return string object
a="how"
b="are"
c= a+" "+b+" "+"you";
print(c);

#capitalize(): no-args, return string, convert first letter of the string in capital letter
print(a.capitalize());

#casefold(): no-args, return string, simmilar to lower() but more powerfull and strongly convert string to lower
print("casefold", a.casefold()); 

#center(): no-args, return string, set string to center.
print("center():", a.center(5));

#count(): takes three args count(value(R),start(O),end(O)),return int, count number of element in specified value.
print("count():", a.count("hello how are you",5,9));

#encode(): 2-args,(encode(O default utf-8),errors(O)), return bytes, encode the string by specified encoding type.
print("encode()", (a.encode()));

#endswith(): 3-args,(value(R),start,end),return bool, check specified value ends with string value.
print("endswith()","how are you".endswith("you"));

#expandtabs(): 1-args(tabsize(O default 8), retrun string, add tabs to specified tabbed string.
print("expandtabs():","how\t are\t you".expandtabs(10));

#find(): 3-args(value(R),start(O),end(O)),return int, find first occurrence of the specified value. -1 if not found.
print("find():", "hi there".find("z"));

#index(): 3-args(value(R),start(O),end(O)), return int, find first occurrence of the specified value. exception if not found.
print("index():","hi there".index("e"));

#isalnum(): no-args, return bool, true if string contains alpha numeric values(a-zA-Z 0-9)
print("isalnum():","Password123".isalnum());

#isalpha(): no-arg, return bool, true, if string only contains characters.
print("isalpha():","abcdefgh".isalpha());

#isdecimal(): no-arg, return bool, true, if all characters are decimal or int or (numbers).
print("isdecimal():","4.4".isdecimal());

#isdigit(): no-arg, return bool, true, if string contains only digits.
print("isdigit()::","444".isdigit());

#isprintable(): no-agrs,return bool, true, if all charcters in string printable(except carriage return,line feed)
print("isprintable", "is printable \r check?".isprintable());

#istitle(): no-args, return bool, true, if all word in string start with upper case rest with lowercase
print("isTitle():","Is Satisfy Title Case Ys112?".istitle());

#isspace(): no-args, return bool, true, if string contains only spaces.
print("isspace():",'    '.isspace());


#isidentifier(): no-args, return bool. True, if string contains valid identifiers(can have only a-z0-9_)
print("isidentifier():","_isidentifier007".isidentifier());

#islower(): no-args, return bool, true, if string contains all lower case characters.
print("islower():","isLower".islower());

#isnumeric(): no-args, return bool, true, if string contains int.
print("isnumeric()::","3.9".isnumeric());

#isupper(): no-args, return bool, true, if string contains only uppercase letters
print("isupper():","STRING CONTAINS UPPERCASE".isupper());

#join(): 1-args,(iterable(R)) usually take collection,string as iterable, return str, takes all item in iterable and join them into one string
list_of_integers = [3,4,5,6,7,2,34,3];
list_of_str = ["hi","hello","bye"];
print(" ".join(list_of_str));

#lstrip(): one-args,(chars(O) default " "), return str, remove/trim specified value from string at left side
print("lstrip()::","  ,,,,.....pppp hello   ".lstrip(" ,.p"));

#ljust(): 2-args, (length(R), characters(O bydefault " ")), return str, align string to left with specifed value(default " ") upto length.
print("ljust():","banana".ljust(14)+"is my fav food");

#maketrans(): 3-args, (x(R), y(O), z(O)) return a dict of ascii code then translate method replace with specified value.
dict_ = {112:32};
txt="hey kigson";
tbl= txt.maketrans("k"," ","ig");
print("maketrans():", txt.translate(tbl));

#partion(): 3-args, (value(R),start,end), return 3 tuples, 1-left side string of specified value 2- matched value 
# 3- right string of matched value. if value not matched return 1- whole string 2-empty string 3- empty string
print("partition","what is the color of banana? the color of banana is yellow".partition("banana"));

#rfind(): 3-args, (value(R), start, end), return int, search for specified value occurrence at the last of the string. -1 if not found.
print("rfind():","apple is good for health".rfind("e"));

#rindex(): 3-args, value(R),start, end), return int, search for specified value last occurrence in the string. exception if not found
print("rindex():", "apple is good for health".rindex("a"));

#rjust(): 2-args, (length,char), return string, align the string to right, fill the specified value/char upto the length.
print("rjust():", "kiwi ".rjust(8)+"is a energy booster food");

#rpartion(): 3-args, (value(R),start,end), return 3 tuple, checks last occurrence of specified string
print("rpartion:","what is the color of banana? the color of banana is yellow".rpartition("banana"));

#rspllit(): 2-args, (separator(R),maxsplit(O)), return list, maxsplit is number of element plus one. start from the end of the string.
print("rsplit():", "hello, hey, bye".rsplit(",",1));

#rstrip(): 1-args, (char(O)), return string, trim the string with specified value from end of the string
print("rstrip():","  hiii there    ".rstrip());

#splitlines(): 1-args, (keybreaks(O default false), return list if \n is there in a string it will break the string.
print("splitlines():","welcome to the \n jungle".splitlines());

#startswith(): 3-args, (value(R),start(O),end(O)), return bool, true if specified value matched with the string
print("startswith():","simar kiran".startswith("k",6));

#swapcase(): no-args, return string, if string is in upper case it will convert to lower case & vice versa.
print("swapcase():","Simar kiran".swapcase());

#translate(): 1-args,(table(dict)) return string, it will replace string value to specified values
dict_={83:80};
print("Hello Sam!".translate(dict_));

#zfill(): 1-args,(len) it will fill the values with the 0 at the starting of string.until it reaches to the specified length.
print("hello".zfill(10));



