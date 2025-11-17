# import pandas as pd

# data = {
#     "ID": list(range(1, 21)),
#     "Name": [
#         "John", "Mary", "Alex", "Sophia", "David", "Emma", "Daniel", "Olivia", "James", "Isabella",
#         "Michael", "Ava", "Alex", "Mia", "Ethan", "Amelia", "Benjamin", "Charlotte", "Lucas", "Harper"
#     ],
#     "Age": [28, 32, 26, 30, 35, 29, 31, 27, 40, 33, 45, 24, 38, 29, 36, 25, 41, 28, 34, 30],
#     "Department": [
#         "IT", "HR", "Finance", None, None, "Marketing", "HR", "Finance", "Sales", "IT",
#         "Finance", "HR", "Marketing", "Sales", "Finance", "IT", "HR", "Marketing", "Sales", "Finance"
#     ],
#     "Salary": [
#         60000, 55000, 52000, 48000, 75000, 50000, 58000, 62000, 70000, 64000,
#         72000, 47000, 68000, 51000, 56000, 73000, 49000, 66000, 58000, 54000
#     ]
# }

# df = pd.DataFrame(data)

# # print(df)




import pandas as pd

import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
               101, 102, 103, 111, 112, 113, 114, 115, 113, 114],  # duplicate IDs
    "Name": [" john  ", "MARY", "Alex", None, "sara ", "BOB", "john  ", "Meera", " ", "Venu",
             " john  ", "MARY", "Alex", "SITA", "meera", "bob ", "raj ", "sita", "bob ", "raj "],
    "Department": ["IT", "HR", "Finance", "finance", None, "IT", "HR", "finance", "Finance", "HR",
                   "IT", "HR", "Finance", "it", "HR", "Finance", "finance", "Finance", "finance", "Finance"],
    "Salary": [80000, 70000, 60000, None, 90000, 45000, 70000, None, 55000, 60000,
               80000, 70000, 60000, 95000, None, 50000, 40000, 75000, 50000, 40000],
    "Age": [28, 35, None, 40, 29, 30, 30, 1000, 38, 27,
            28, 35, None, 32, 45, 31, 200, 29, 31, 200],  # duplicates + outliers
    "Experience": [2, 5, 3, None, 7, 1, 5, 15, 8, 2,
                   2, 5, 3, 10, None, 6, 4, None, 6, 4],
    "City": ["Hyderabad", "VIZAG", "hyderabad", None, "Vizag", "Hyderabad", "vizag", "VIZAG", " ", "hyderabad",
             "Hyderabad", "VIZAG", "hyderabad", "vizag", "VIZAG", "vizag", "vizag", "vizag", "vizag", "vizag"],
    "Joining_Date": ["2020-01-01", "2021-06-10", "not_available", None, "2022-03-15", "2021-06-10",
                     "2020-01-01", None, "2021-06-10", "2020-01-01",
                     "2020-01-01", "2021-06-10", "not_available", "2022-03-15", None, "not_available",
                     "2021-06-10", "2020-01-01", "not_available", "2021-06-10"],
    "Rating": [4, None, 3, 5, 2, 3, None, 4, 5, 2,
               4, None, 3, 4, 5, 3, 5, None, 3, 5],
    "Email": ["john@example.com", "mary@example.com", "alex@company.com", " ", "sara@gmail.com", None,
              "john@example.com", "meera@company.com", " ", "venu@company.com",
              "john@example.com", "mary@example.com", "alex@company.com", None, "meera@company.com",
              "bob@company.com", "raj@company.com", "sita@gmail.com", "bob@company.com", "raj@company.com"]
}

df = pd.DataFrame(data)


# print(df[df["City"].str.contains("hyd",case=False,na=False)])
df["City"]=df["City"].str.replace("hyderabad","HYD",case=False)
df["City"]=df["City"].str.replace("vizag","VIZAG",case=False)
df["Department"]=df["Department"].str.replace("finance","Fin",case=False)
df["Name"]=df["Name"].str.strip()
df["Name"]=df["Name"].str.upper()
# print(df)


df["Joining_Date"] =pd.to_datetime(df["Joining_Date"],errors="coerce")


df["Year"]=df["Joining_Date"].dt.year.astype("Int64")
df["Month"]=df["Joining_Date"].dt.month.astype("Int64")
df["Day"]=df["Joining_Date"].dt.day.astype("Int64")
df["WeekDay"]=df["Joining_Date"].dt.day_name()
df["abc"]=df["Joining_Date"].dt.strftime("%a , %d  %b %y")

print(df)
# df.head(10)












