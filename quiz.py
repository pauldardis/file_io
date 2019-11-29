f = open('data.txt', "r")
lines = f.readlines()
f.close()
print(lines)

f = open('data.txt', "r")
lines_v2 = f.read()
f.close()
print (lines_v2)