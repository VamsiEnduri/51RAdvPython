import pandas as p

# # data_frame=p.DataFrame([("vamsi","Trainer",29999,"Hyd"),("ravi","Dev",55555,"Chennai"),("raju","testing",8888,"Delhi"),("rakesh","CEO",100000,"Hyd")],columns=["name","Role","salary","location"])
# # # print(data_frame)

# # # data_frame.to_excel("data.xlsx",index=False)
# # # data_frame.to_csv("data2.csv",index=False)

# # # data_frame.to_json("data.json",index=False)
# # data_frame.to_sql("data.sql",index=False)
# # data_frame.to_html("data.html")


# # data_frame=p.DataFrame({"emp_id":range(1,3),"emps":["vamsi","ravi"],"role":["Trainer","dev"],"salary":[12345,34567]})
# # print(data_frame)


# data_frame=p.DataFrame({
#     "EmployeeID": range(1, 21),
#     "Name": [
#         "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack",
#         "Kathy", "Leo", "Mona", "Nina", "Oscar", "Paul", "Queen", "Raj", "Sophia", "Tom"
#     ],
#     "Department": [
#         "HR", "Finance", "IT", "Sales", "IT", "HR", "Finance", "Sales", "IT", "HR",
#         "Finance", "Sales", "IT", "Finance", "HR", "Sales", "IT", "Finance", "Sales", "HR"
#     ],
#     "Salary": [
#         50000, 60000, 55000, 45000, 70000, 48000, 62000, 47000, 72000, 51000,
#         59000, 46000, 75000, 61000, 53000, 48000, 77000, 64000, 49000, 52000
#     ],
# })
# data_frame.to_excel("empdata2.xlsx",index=False)



# storeData=p.read_excel("./data.xlsx")
# print(storeData)

# storeData2CSV=p.read_csv("./data2.csv")
# print(storeData2CSV)


storeData2Html=p.read_html("./data.html")
print(storeData2Html)