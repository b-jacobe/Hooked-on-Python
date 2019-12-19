"""
Excercise to writing / reading files

(Jypter Notebook ver.)
%%writefile myFile.txt
Hello World
This is the second line
This is the third line

File Paths:
Windows - myfile = open("C:\\Users\\UserName\\Folder\\text.txt")
MacOS = myfile = open("/Users/UserName/Folder/text.txt")

a = append
w = write
r = read
r+ = read + write
w+ = write and read (overwrite or create new)
"""

# read() / seek()
myfile = open('test.txt')
print(myfile.read()) # Reads from beginning to the end, stored as a string
myfile.seek(0) # Resets the cursor to the beginning of the file

with open('test.txt',mode='w+') as w:
    w.write('Hello World!')
    w.close()

# readlines()
print(myfile.readlines()) # Stores each line as individual elements in a list.
myfile.close()