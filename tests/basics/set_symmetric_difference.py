print({1,2}.symmetric_difference({2,3}))
print({1,2}.symmetric_difference([2,3]))
s = {1,2}
print(s.symmetric_difference_update({2,3}))
l = list(s)
l.sort()
print(l)
