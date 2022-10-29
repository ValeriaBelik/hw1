print("Hello world")

first_value = 6
second_value = 12
a1 = 6
b2 = 12
c3 = a1
print(a1, c3, b2)
a1 = b2
print(a1, c3, b2)
b2 = c3
print(a1, c3, b2)


c3 = a1
print(a1, b2)
a1 = b2
print(a1, b2)
b2 = c3
print(a1, b2)


a1, b2 = b2, a1
print(a1, c3, b2)

var = 12 + b2 - 233 + a1
print(var)