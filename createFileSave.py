import os.path

save_path = '/mnt'
file_name = "prueba1.txt"

completeName = os.path.join(save_path, file_name)
print(completeName)

file1 = open(completeName, "w")
file1.write("It works")
file1.close()
