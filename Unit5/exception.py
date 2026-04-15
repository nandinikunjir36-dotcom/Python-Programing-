import os

folder_path = "/users/pawar/OneDrive/Documents/"  # fixed folder
filename = input("Enter file name: ")
full_path = os.path.join(folder_path, filename)
try:
     with open (filename, "r") as file:
         content = file.read( )
         print("\nFile opened successfully!")
         print("File content: \n" )
         print ( content)

except FileNotFoundError:
     print("Error: The file does not exist. Please check the filename.")
except PermissionError:
     print("Error: You do not have permission to read this file.")