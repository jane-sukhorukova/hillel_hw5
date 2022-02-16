set1 = {1, 2, 3}
# add
set1.add(4)

# copy
set2 = set1.copy()

# discard
set2.discard(2)

# remove
set1.remove(1)

# intersection
set3 = set1.intersection(set2)

# issubset
set4 = {3, 4, 5, 6}
set5 = set4.issubset(set3)
# set5 = False

# issuperset
set6 = set4.issuperset(set3)
# set6 = True

# pop
set4.pop()

# union
set7 = set1.union(set2, set3, set4)

# update
set8 = {7, 8, 9}
set7.update(set8)

# isdisjoint
set9 = set1.isdisjoint(set8)
# set9 = True

# difference
set10 = set4.difference(set3)

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
print(set8)
print(set9)
print(set10)


# clear
set1.clear()
print(set1)