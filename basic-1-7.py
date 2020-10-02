file_name = input("provide filename : ")
# file name can be anything exept special signs such as !@#$ etc. "." - dot is one of them,
# exept it is a way to say " hire name ends, and type of file starts"
# we can just read everything behind "." and it is a file file file_type
dot_index = file_name.find(".")
print(file_name[dot_index+1:])
