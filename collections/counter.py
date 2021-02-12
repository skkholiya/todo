#Counter is the sub-class of the dictionary class. return no of times value occur in the container object(implicity implements hashtable)
#three ways to initialize Counter
#1 using sequence of items
import collections as c

#empty counter
cnt = c.Counter();
for i in ["hello","hi","hello","hey","hello","hi"]:
  cnt[i] += 1;
print("default Counter():", cnt);

list_ex = [21,42,32,21,21,42]
print("initaialization 1 using sequence", c.Counter(list_ex));

#2 dict contaning key & value
dict_ = {"a":4,"b":3,"c":2};
print("# 2 dict way", c.Counter(dict_));

#3 keyword argument
print("# 3 keyword argument:", c.Counter(a=4,b=3,c=2));

#Counters method: most_common(n), return list of tuples n most common elements and their counts from the counter
print("most_common()",c.Counter(dict_).most_common(2));

#elements(): return an iterator over elements repeating each, as many times as its count.
print("elements()",list(c.Counter(dict_).elements()));

