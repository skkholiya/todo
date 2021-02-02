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

#find(): 3-args(value(R),start(O),end(O)), return bool, return int, find first occurrence of the specified value.
print("find():", "hi there".find("t"));



