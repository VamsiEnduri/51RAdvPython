# # try :-- except :-- else
# # try:
# #     a=int("10")
# #     print(a)
# # except:
# #     print("enter proper value")    
# # else :
# #     print("no any errors")    


# # try :-- except :-- except :-- else 
# # research topic :-- 1
# # try:
# #     a=floa(input("hello enter value here :-- "))
# #     print(a)
# # except ValueError:
# #     print("enter proper value") 
# # except SyntaxError:
# #     print("enter proper syntax") 
# # except NameError:
# #     print("enetr proper name ")          
# # else :
# #     print("no any errors") 



# # - try 0:-- except :-- except :-- finally :-- else       
# # try
# # catch
# # finally :-- errors and no erroes :-- 

# try :
#     a=100
#     b=200
#     c=a==b
#     d+="vamsi"
#     print(d)
# except ValueError:
#     print("enetr proper values to do concatenation")  
# except TypeError :
#     print("enetrproper data types")
# except NameError:
#     print("try to access the names which are defined")   
# else:
#     print("no any errors")     
# finally:
#     print("finally executing")          


# nested try - except example :

try :
    a=int("123abc")
    b=0
    try:
        c=a/b
        print(c)
    except:
        print("enter proper values for denominator other than 0")  
except:
    print("entr proper value")
    
