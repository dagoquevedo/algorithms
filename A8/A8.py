from BTrees.OOBTree import OOBTree
t = OOBTree()
t.update({1: "red", 2: "green", 3: "blue", 4: "spades"})
print len(t)
s=t.keys()
print(s)
print(s[-2])
