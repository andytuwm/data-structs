__author__ = 'Andy'

import hashset

set = hashset.HashTableSet()
print(set.size())
set.put(123)
set.put(123)
set.put(1234)
set.put("HI")
print("Should be True: ", set.contains(1234))
print("Should be True: ", set.contains(123))
print("Should be True: ", set.contains("HI"))
print("Should be False: ", set.contains("hi"))
print(set.size())

set.delete(123)
print(set.size())
print("Should be False: ", set.contains(123))
print("Should be True: ", set.contains(1234))