# sets are the unique collection of items. They are unordered, meaning that the items do not have a defined order, and they do not allow duplicate values. Sets are mutable, which means that you can add or remove items after the set has been created.
set1={12,34,56,78,90}
print("Original set:", set1)
# adding an element to the set
set1.add(100)       
print("Set after adding 100:", set1)
# removing an element from the set
set1.remove(34)
print("Set after removing 34:", set1)
# checking if an element is in the set
print("Is 56 in the set?", 56 in set1)
# iterating through the set
for item in set1:
    print(item)
# proving the unduplicate property of set
set1.add(12)    
print("Set after trying to add duplicate 12:", set1)
# set operations    
set2={56,78,90,110,120}
# union of two sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
# intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
# difference of two sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2 (set1 - set2):", difference_set)
# symmetric difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)
