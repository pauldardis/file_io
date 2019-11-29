f = open('newfile.txt', 'w')
f.write("Hello\n")
f.close()

f = open('newfile.txt', 'a')
f.write("World")
f.close()


f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()