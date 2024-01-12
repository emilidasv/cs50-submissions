

file_name=input("Filename:")
file_name= file_name.lower()
file_name=file_name.strip()
number = file_name.find('.')
#get the extesnion name
lenth=len(file_name)
extension_name= file_name[number:lenth]
if extension_name == ".gif": print("Image/gif")
elif extension_name == ".jpg": print("Image/jpg")
elif extension_name == ".jpeg": print("Image/jpeg")
elif extension_name == ".png": print("Image/png")
elif extension_name == ".pdf": print("application/pdf")
elif extension_name == ".txt": print("Document/txt")
elif extension_name == ".zip": print("Document/zip")
else :print ("unknown")
