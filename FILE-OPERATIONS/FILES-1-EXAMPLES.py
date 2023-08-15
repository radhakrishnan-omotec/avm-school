#################################
### FILE OPEN 

# f = open('test.txt',mode = 'r')
# print(f.name)
# print(f.mode)
# f.close()

#################################
### FILE READ

# f = open('test.txt','r')
# x = f.read()
# print(x)
# f.close()

#################################
### FILE READLINE

# f = open('test.txt','r')
# x = f.readline()
# print(x)
# f.close()

#################################
### FILE READLINES TO LIST

# f = open('test.txt','r')
# x = f.readlines()
# print(x)
# f.close()

#################################
### FILE SELECTIVE LINES USING FOR LOOP

# f = open('test.txt','r')
# for i in range(0,5):
#     x = f.readline()
#     print(x)
    
# f.close()

#################################
### ISSUE WHEN USING TWO PRINT STATEMENTS

f = open('test.txt','r')
x = f.read()
print(x)
y = f.read()
print(y)
f.close()

#################################

### RESOLVING ABOVE PROBLEM USING TELL() and SEEK() 

# with open('test.txt') as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
    
#################################
### FILE WRITE TO NEW FILE
# r = open('test.txt',mode = 'r')
# w = open('test_new.txt',mode = 'w')
# x = r.read()
# w.write(x)
# r.close()
# w.close()

#################################
# READ CSV FILE

# f = open('contacts-basic.csv')
# x = f.read()
# print(x)

#################################
# READ FIRST RECORD IN CSV FILE

# f = open('contacts-basic.csv')
# # discarding the first line as it is the columns
# x = f.readline()
# y = f.readline()
# print(y)

#################################
### STORING TO LIST 

# f = open('contacts-basic.csv')
# # discarding the first line as it is the columns
# x = f.readline()
# y = f.readline()
# print(y)

# # STORING TO LIST 
# a = y.split(',')
# print(a)

#################################
### RETRIEVING VALUE FROM THE LIST
### CHANGE VALUE TO INTEGER WITHOUT ""

f = open('contacts-basic.csv')
# discarding the first line as it is the columns
x = f.readline()
y = f.readline()
print(y)

# STORING TO LIST 
a = y.split(',')
print("STORING TO LIST ")
print(a)
b =a[3]
print("RETRIEVING VALUE FROM THE LIST ")
print(b)

# CHANGE VALUE TO INTEGER WITHOUT ""
c = b.strip('"\n')
print("STRIP VALUE FROM THE LIST ")
print(c)


# d = int(c)
# print(d)

#################################

