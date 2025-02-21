a = 7
print(a)

a, b = 1, 2
print(a, ' ', b)
a, b = b, a
print(a, ' ', b)
print (id(a), ' ', id(b))

m = 4
n = m
print(id(m), ' ', id(n))