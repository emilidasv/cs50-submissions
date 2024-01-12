

file_name=input("Filename:")
file_name= file_name.lower()
file_name=file_name.strip()
number = file_name.find('.')
#get the extesnion name
lenth=len(file_name)
extension_name= file_name[number:lenth]
if extension_name == ".gif": print("image/gif")
elif extension_name == ".jpg": print("image/jpg")
elif extension_name == ".jpeg": print("image/jpeg")
elif extension_name == ".png": print("image/png")
elif extension_name == ".pdf": print("application/pdf")
elif extension_name == ".txt": print("text/plain")
elif extension_name == ".zip": print("application/zip")
else :print ("unknown")
