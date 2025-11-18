import pandas as pd

data = {
    "ID": [1,2,3,None,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Name": ["Ram","Sita","Ravi","Teja","Priya","Kiran","Manoj","Asha","Vani","Raj",
             "Latha","Suresh","Swathi","Harsha","Sai","Divya","Karthik","Meena","Arun","Pooja"],
    "Age": [25,30,28,22,None,26,24,29,31,27,33,40,23,26,34,28,32,30,29,24],
    "Department": ["IT","Finance","IT","HR","Sales","Finance","IT","HR","Finance","IT",
                   "Sales","IT","HR","Finance","IT","Sales","HR","Finance","IT","Sales"],
    "Salary": [50000,60000,55000,45000,65000,62000,48000,52000,58000,54000,
               70000,73000,49000,61000,68000,64000,53000,60000,56000,None],
    "Gender": ["M",None,"M","M","F","M","M","F","F","M",
               "F","M","F","M","M","F","M","F","M","F"],
    "Experience": [2,4,3,1,6,5,2,3,4,3,7,10,2,5,8,6,4,5,3,2],
    "City": ["Hyderabad","Delhi","Hyderabad","Chennai","Mumbai","Delhi","Hyderabad","Chennai","Mumbai","Hyderabad",
             "Chennai","Delhi","Mumbai","Hyderabad","Delhi","Mumbai","Chennai","Hyderabad","Delhi","Hyderabad"],
    "Join_Date": ["2021-05-10","2020-07-15","2022-01-20","2023-03-01","2019-08-18","2018-11-25","2021-10-11",
                  "2020-06-14","2019-12-22","2021-04-09","2017-09-15","2016-10-05","2022-08-30","2019-01-10",
                  "2018-03-30","2020-11-19","2021-02-13","2018-06-09","2023-01-22","2022-12-01"],
    "Rating": [4.1,4.5,4.0,3.8,4.7,4.4,3.9,4.2,4.3,4.0,
               4.8,4.6,3.7,4.1,4.9,4.3,4.0,4.4,3.9,4.2]
}

df = pd.DataFrame(data)

# # print(df["Salary"]) # single c
# # print(df[["Salary","Rating","City"]]) # multuple columns
# # print(df.loc[17]) # row single
# # print(df.loc[17:19]) # multiple rows
# # print(df.loc[2,"Age"]) # specifc value

# # print(df.loc[17:19,["Age","City","Salary"]]) # specofic rows and columns

# # print(
# #     df.loc[
# #     ((df["Rating"] >=2.5) & (df["Rating"]<=4 ) )
# #     & 
# #     (df["City"] == "Hyderabad" )

# #     &
# #     (df["Department"] == "IT")
# #     ]
# #     )
# # print(df.query("Department == 'Finance' and City in ('Mumbai','Chennai') and Rating >=2.5 "))

# # print(df[df["City"].isin(["Chennai","Mumbai"])])
# # print(df.isnull().sum())
# # 
# # df["Salary"].fillna(df["Salary"].mean(),inplace=True)
# # df["Gender"].fillna("unknown",inplace=True)

# # print(df.duplicated())
# # df.drop_duplicates(keep="first")
# # df.drop_duplicates(keep="last")

# # df.rename(columns={"Name":"EmpName","City":"EmpCity"},inplace=True)
# # df.rename(index={0:"fisrtindex"},inplace=True)


# # print(df)




# df = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Math": [90, 80, 70],
#     "Science": [85, 75, 65]
# })

# df["Total"]=df["Math"]+df["Science"]
# df.drop("Total",axis=1,inplace=True)
# df.loc[3]=["Vamsi",88,66]
# df.drop(0,axis=0,inplace=True)

df["City"]=df["City"].replace("Chennai","cn")
print(df)


# outliner values :-- how can we handle :-- 