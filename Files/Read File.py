# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open(r"D:\My_Progict\Software & Programming\Python\Files\tareq.txt", "r")

#print(myFile) # File Data Object
#print(myFile.name)
#print(myFile.mode)
#print(myFile.encoding)

#print(myFile.read())
#print(myFile.read(5))

# print(myFile.readline(5))
# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines()) 
# print(myFile.readlines(50)) 
# print(type(myFile.readlines())) 

for line in myFile:
    print(line)

    if line.startswith("07"):
        break

# Close The File
myFile.close()


