#Demonstration of file handling operation in python 
file = open("sample.txt","w")
file.write("hello this is the first line in the file.\n")
file.write("python file handling demonstration.\n")
file.close()

print("data written successfully.\n")

file = open("sample.txt", "r")
print("reading file contents:")
content =file.read()
print(content)
file.close()

file=open("sample.txt","a")
file.write("this line is added later using append mode.\n")
file.close()

print("data appended successfully.\n")

#4.Read the file agin to see update
file=open("sample.txt","r")
print("Updated file contents:")
updated_content=file.read()
update_content=file.read()

print(updated_content)
file.close()