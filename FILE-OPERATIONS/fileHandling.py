#READ CSV FILE

f = open('contacts-basic.csv')
# x = f.read()
# print(x)

z = f.readline()

y = f.readline()
print(y)
print("-----------------------")
a = y.split(',')
print(a)
print("-----------------------")
b =a[3]
print("List index value = " ,b)
print("-----------------------")
c = b.strip('"\n')
print("List index value after strip = " ,c)