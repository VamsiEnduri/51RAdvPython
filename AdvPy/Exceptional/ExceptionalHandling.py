# print("program started")
# input1=input("enter a digit for numerator") # 10
# input2=input("enter a digit for denominator") # 0
# result = int(input1)/int(input2) # 10/0  end
# print(result)
# print("program ended")

# exceptional scenarios :
print("program started")
try:
    #  code to excute 
    input1=input("enter a digit for numerator") # 10
    input2=input("enter a digit for denominator") # 0
    result = input1/input2 # 10/0  end
    print(result)
except ZeroDivisionError:
    print("numerator cant be divided by zero denominator")   
except ValueError:
    print("enter valid values")
except TypeError:
    print("enter proper datatypes for / opeartion")    
print("program ended")