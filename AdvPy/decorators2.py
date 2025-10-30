# decorator is a function which takes another function as value and it returns new function
# decorator func will give new behaviour for our code without change of ori code by adding extras behaviour

# def decorator(z):
#     def b():
#         print("vamsi")
#         z()
#     return b; 

# def a():
#     print("a function")
# abc=decorator(a)
# abc()    


# 2nd example :-- args

# def decorator(z):
#     def b(m,n,o):
#         print(m,n,o)
#         z()
#     return b; 

# def a():
#     print("a function")
# abc=decorator(a)
# abc("vamsi","trainer","hyd")  


# -- 3rd example :-- * args

# def decorator(z):
#     def b(*m):
#         print(m)
#         for i in m:
#             print(i)
#         z()
#     return b; 

# def a():
#     print("a function")
# abc=decorator(a)
# abc("vamsi","trainer","hyd") 


# -- 4th example **args

# def decorator(z):
#     def b(**m):
#         z()
#         z()
#         print(m)
#         for i,j in m.items():
#             print(i,j)
#         # z()
#     return b; 

# def a():
#     print("a function")
# abc=decorator(a)
# abc(name="vamsi",role="trainer",loc="hyd") 


# 5th example :- python way decorator 

# def salIncre(hikeFunc):
#     def wrapper(salary,name):
#         hikeFunc(salary,name)
#         print(f"the empc {name} initial salary was",salary)
        
#     return wrapper

# @salIncre
# def hike(sal,name):
#     hikePercentageSal=sal*0.1
#     print("sal increments by 10%",f"and that is {hikePercentageSal}")
#     print("now {name} sal is ",sal+hikePercentageSal)

# hike(15000,"vamsi")



#6th example :-- 
from datetime import datetime

def loggingCapture(hyd):
    def wrapper(user_name,opeartion):
        if opeartion == 1:
            print(f"{user_name} you are about to login....")
            hyd(user_name)
        if opeartion == 2:
            print(f"{user_name} you are about to loggedout....")
            hyd(user_name)

    return wrapper;    

def login(user_name):
    if user_name:
        print(f"{user_name } has been loggedin at {datetime.now()}")

def logout(user_name):
    print(f"{user_name } has been loggedout at {datetime.now()}")
    break


while True:
    print("1.login")
    print("2.logout")
    i=input("choose option :-- ")
    if i == "1":
        abc123=loggingCapture(login)
        un=input("enter user name to login :-- ")
        abc123(un,1)

    if i == "2":
        abc123=loggingCapture(logout)
        un=input("enter user name to login :-- ")
        abc123(un,2)


          







