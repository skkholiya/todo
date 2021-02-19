#1 zip(), multiple-args, zip(iterator1,iterator2..), return tuples of iterator, first item in each 
#passed iterator is paried together, and then the second item in each passed iterator is paired together, and so on and so forth.

#if passed iterator have different lengths, the iterator with the least items decides the length of the new iterator.

male = ("Rahul","Sameer","Yash");
female = ("Juli","Kiran","Wasu");

couple = zip(male,female);
print("1-zip():",tuple(couple));


#2 abs(): single-arg, abs(number(R)),returns number, return the absolute value of the number, absolute value(how far a number is from zero
num = -55;
print("2-abs():",abs(num)); #o/p- 55

#3 all(): single-arg all(iterator),returns bool, return true if all value present in specified iterator is true. in case of dict, it checks keys, for empty iterator also provides True.
dict_iterator = {0:"alpha",1:"Beta",2:"Gamma"}
print("3-all():",all(dict_iterator)) #o/p- False

#4 any(): single-arg any(iterator),returns bool, return True if any value present in specified iterator is true. empty iterator return False
print("4-any():",any(dict_iterator)) #o/p- True

#5 ascii(): single-arg ascii(object), returns string, return readable version of any object, replace all non-ascii char with escape character
obj = 5;
print("5-ascii():",ascii(obj));

#6 bin(): single-arg, bin(number), returns binary, return binary version of specified integer. always starts wit 0b
bin_example = 36;
print("6- bin():",bin(bin_example));

#7 bool(): single-arg, bool(object), returns bool, return boolean value of specified object. unless object is None, ([],{}..) ,0 ,False.
bool_ex = [({(0,0)})];
print("7- bool():",bool(bool_ex));

#8 bytearray(): 3-args,(x,encoding,errors), return bytearray, x or source to use to create bytearray object, encoding type for string, errors for if encoding fails. mutable in nature
byte_array = "my name is khan"
print("8 bytearray():", bytearray(byte_array,"UTF-8"))

#9 bytes(): 3-args,(x,encoding,erros), returns bytes, x or source to use to create bytes object, encoding type for string, errors for if encoding fails. Immutable in nature.
print("9 bytes():", bytes(byte_array,"ASCII"));

#10 callable(): 1-arg,(callableObj), returns bool, return True is callable object.
a=5;
def call():
  a=5;
#an object is created of call.
let = call;  
print("callable():",callable(let));
print("callable2():",callable(a));

#11 chr(): 1-arg chr(unicode), returns char, returns specified unicode number, character.
print("chr():", chr(97));


