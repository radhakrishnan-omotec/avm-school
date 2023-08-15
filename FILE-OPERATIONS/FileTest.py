### ISSUE WHEN USING TWO PRINT STATEMENTS

with open('test.txt') as f:
    print(f.tell())
    print(f.read())
    print(f.tell())
    f.seek(20)
    print(f.tell())
    print(f.read())
    # print(f.tell())