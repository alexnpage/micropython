a = bytearray([1, 2, 200])
print(a[0], a[2])
print(a[-1])
a[2] = 255
print(a[-1])
a.append(10)
print(len(a))

s = 0
for i in a:
    s += i
print(s)
