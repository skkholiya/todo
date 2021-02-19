import re
#Regex check if string contain specified search pattern.
# 4 methods: search(), sub(),finall(),split()

#findall(): return a list containing all matches,if no match found return empty list.
txt = "as soon as possible"
x = re.findall("as",txt)
print("findall():",x) #o/p: ['as','as']

#search(): search string for a match, return a matched object, if more than one match return first occurrence, if no match return none
search_example = re.search("\s",txt)
print("search():", search_example.start());

#split(): split the string specifying the seperator, return list of split items
split_example = re.split("\s",txt)
print("split():",split_example);


#sub(): replace the matches with text of your choice. return string
txt = "ooooooooooooooooperate"
sub_example = re.sub("o{1,}","o",txt)
print(sub_example)
