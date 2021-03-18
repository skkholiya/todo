#Set Questions

#1. Write a Python program to create a set.
x = set();
print("empty set:",x);
x.update({2,3,2,4,1});
print("update set:",x);



#2. Write a Python program to iterate over sets.
set_ex = {1,2,3,4,5,6,8}
for i in set_ex:
  print(i);




#3. Write a Python program to add member(s) in a set.
set_ex = {1,2,3,4,5,6,8}
set_ex.add(9)
print("add 9 to the set",set_ex);




#4. Write a Python program to remove item(s) from set
set_ex = {1,2,3,4,5,6,8};
set_ex.discard(8);
print("8 remove from the set",set_ex);




#5. Write a Python program to remove an item from a set if it is present in the set. 
set_ex = {1,2,3,4,5,6,8};
remove_item = 9
set_ex.remove(remove_item) if remove_item in set_ex else print("Item not present in the set")




#6. Write a Python program to create an intersection of sets.
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
insersection_ex = setx.intersection(sety);
#insersection_ex = setx & sety
print("intersection of set",insersection_ex);




#7. Write a Python program to create a union of sets. 
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
union_ex = setx.union(sety);
#union_ex = setx | sety
print("union of set:",union_ex)



#8. Write a Python program to create set difference. 
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
#set difference : is the set of elements which are in either of the sets, but not in their intersection.
#For example, the symmetric difference of the sets \{1,2,3\} and \{3,4\} is \{1,2,4\}.

#difference_ex = setx.difference(sety);

intersection = setx & sety

difference_ex = setx - intersection
print("set difference:",difference_ex);


#9. Write a Python program to create a symmetric difference.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
#Symmetric Difference: element present in both set, avoid duplicates.
z = x ^ y;
#z = x.symmetric_difference(y)
print("symmetric difference:", z);





#10. Write a Python program to check if a set is a subset of another set.
x1 =  {'mango', 'apple'}
y1 =  {'mango', 'orange'}
z1 =  {'mango'} 

result1 = True if z1.issubset(x1) else False
result2 = True if y1.issubset(x1) else False
result3 = True if z1.issubset(y1) else False
print("x:",x1)
print("y:",y1)
print("z:",z1)

print("z subset of x:",result1)
print("y subset of x:",result2)
print("z subset of y:",result3)


#11. Write a Python program to create a shallow copy of sets.
org_set = {1,2,3,4,5,6}
shallow_copy = org_set.copy();
print(shallow_copy);


#12. Write a Python program to clear a set. 
set_ex = {1,2,3,4,5,6}
print(set_ex)
set_ex.clear()
print(set_ex);


#13. Write a Python program to use of frozensets. 
frozen_set = frozenset({1,2,3,4,5,9});
frozen_set1 = frozenset([3,4,5,9]);
#difference of two frozen sets
print(frozen_set.difference(frozen_set1));
#frozen_set1 is subset of frozen_set
print(frozen_set1.issubset(frozen_set));


#14. Write a Python program to find maximum and the minimum value in a set.
set_ex = {1,2,3,4,5,6}
print("min value in set", min(set_ex), " max value in set", max(set_ex));




#15. Write a Python program to find the length of a set. 
set_ex = {1,2,3,4,5,6}
print("length of set:",len(set_ex));



#16. Write a Python program to check if a given value is present in a set or not. 
given_value = "google"
set_com = {"apple","facebook","microsoft","google"}
print(given_value) if given_value in set_com else print("Not Present");




#17. Write a Python program to check if two given sets have no elements in common.
set1= {1,2,3,4}
set2= {4,6,7,8}
diff = set1.isdisjoint(set2);
print("No Elements Present") if diff else print("Common Elements Present in both set");



#18. Write a Python program to check if a given set is superset of itself and superset of another given set.
set1 = {1,2,3,4}
set2 = {2,3,4}
set3 = {4}

print("superset of itself:",set2.issuperset(set2));
print("set2 superset of set3:",set2>set3);



#19. Write a Python program to find the elements in a given set that are not in another set.
set1 = {1,2,3,4}
set2 = {2,3,4}
set3 = {4,5}
#finding unique elements of set1 compare to set2
print(set1.difference(set2));

#finding unique elements of set2 compare to set3
print(set2-set3);




#20. Write a Python program to check a given set has no elements in common with other given set.
set1 = {1,2,3,4}
set2 = {2}
print(True) if set1.isdisjoint(set2) else print(False)




#21. Write a Python program to remove the intersection of a 2nd set from the 1st set. 
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
res = set1.difference_update(set2)
print(set1);

