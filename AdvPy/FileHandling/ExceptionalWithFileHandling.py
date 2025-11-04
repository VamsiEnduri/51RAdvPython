# try:
#     with open("vamsi2.html","w") as v:
#         try:
#             noOfChars=int(input("enter charcters to be read :-- like 1 or  10 etc..")) # int("1") :-- 1
#             abc=v.read(1)
#             print(abc)
#         except ValueError :
#             print("enter proper values to be casting like 123 or 456 but not vamsi r hello")    
# except TypeError :
#     print("enter interger valuyes to read function but not str")    
# finally:
#     print("finally executed")


# create file and add new data 
# try:
#     with open("vamsi3.txt","w") as v3:
#         v3abc = v3.write("hello there today 04-11-25 and today is tuesday",123)
#         print(v3abc)
# except TypeError :
#     print("wtite function take sonly 1 arg but 2 were given")    

# creating , writing, reading and handling with w+ 

# try:
#     with open("vamsi3.txt","w+") as v3:
#         v3abc = v3.write("hello there today 04-11-25 and today is tuesday")
#         v3abc2=v3.read(1)
#         print(v3abc)
#         print(v3abc2)
# except TypeError:
#     print("wtite function take sonly 1 arg but 2 were given")




# with open("vamsi3.txt","a") as v3:
#     v3abc = v3.write("\nhello there today 04-11-25 and today is tuesday")
#     print(v3abc)

# try:
#     with open("vamsi3.txt","x") as v3:
#         v3abc=v3.write("hello")
#         print(v3abc)
# except  FileExistsError :
#     print("alredy file exists try to create a file with new name")   

import os 

# os.mkdir("../iterators&generators")

os.rmdir("./iteartors&generators")

# try:
#     operating_system.remove("vamsi.html")
# except FileNotFoundError:
#     print("no any such file existed to remove it")    


