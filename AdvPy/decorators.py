# what is decorator ?
# what is syntax of decorator ?
# how to use decorator ?
# what are main areas where we will use decorators ?

# def dec(param):
#     def wrapper():
#         a=10
#         print(a)
#         param()

#     wrapper();    

# def a():
#     print("a function at 11th line")

# dec(a)


# def decorator(mrg):
#     def marraigeDetails():
#         print("marriage is going to happen today 28-10-25")
#         mrg()
#         print("its all done marriage")

#     return marraigeDetails     

# def marriage():
#     date="29-10-25"
#     bride="abc"
#     groom="xyz"
#     print(f"{groom} is  got married with {bride} on {date}")

# abc123=decorator(marriage)
# abc123()

def salUpdation(a):
    def salDetails(nameEmp,salEmp):
        print("empy name ",nameEmp)
        print("emp sal in last month",salEmp)
        a()
    return salDetails;    


def currentSal():
    sal=15000
    print("current salary is ",sal)

abc123=salUpdation(currentSal)
abc123("vamsi",14000)