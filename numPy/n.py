import numpy as n 
# a=[1,2,3]
# b=[10,20,30]
# xyz=n.array(a)
# xyz2=n.array(b)
# print(xyz+xyz2)

# sals=[15000,20000,25000,30000]
# salariesNumPy=n.array(sals)

# salAfterHike=salariesNumPy * 1.10
# print(salAfterHike)

# studs=["ravi","sowmya","srilekha","srinu"]
# marks=[[20,30,19],[24,88,77],[33,55,77],[98,45,77]]
# mNumPy=n.array(marks)

# # result=mNumPy.sum()
# result=mNumPy.sum(axis=1)
# # print(result)

# for name,totalMarks in zip(studs,result):
#     print(name,totalMarks)

# print(n.array(0))
# print(n.array([1,2,3]))
# print(n.array([[1,2,3],[4,5,6],[7,8,9]]))
# print(n.array([[[1,2,3]]]))




# try:
#     a=n.array([124,350,2],dtype=n.int8)
#     print(a)
#     print("vamsi")
# except OverflowError:
#     print("enter values in int size range ")

n.array([1,2,3,4]) # vector 1 d
a=n.array([[1,2,3,4]])
b=n.array([[1,2],[2,2],[3,2],[4,2]])
print(a.shape)
print(b.shape)