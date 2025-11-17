import pandas as pd

data = {
    "Emp_ID": [
        None,102,103,104,105,
        106,107,108,109,110,
        111,112,113,114,115,
        116,117,118,119,120
    ],
    
    "Name": [
        None,"        Megha Sharma      ","Ravi Kumar","Sneha Patel","Vikram Singh",
        "    Anita Joshi","Harsha Vardhan","Priya Shetty","Manoj Varma","Divya Kaur",
        "Kiran Rao","     Neha Mehta","Sandeep Das       ","Lakshmi Nair","Rohit Agarwal",
        "Pooja Desai","       Farhan Shaikh","Anjali Verma","Gopi Krishna","Sai Teja"
    ],
    
    "Join_Date": [
        "2019-01-15","2020-03-10","2021-07-21","2018-11-05","2022-06-01",
        "2017-09-13","2020-12-07","2019-05-22","2021-10-30","2022-04-11",
        "2018-03-19","2020-08-14","2021-02-09","2019-12-28","2022-07-17",
        "2018-10-23","2020-05-30",None,"2019-06-18","2022-09-08"
    ],
    
    "Department": [
        "IT","HR","Finance","Marketing","IT",
        "Operations","IT","finance","HR","Marketing",
        "Operations","IT","FINANCE","HR","Marketing",
        "Operations",None,"IT","HR","Marketing"
    ],
    
    "Age": [
        29,32,27,30,25,
        38,28,31,26,33,
        40,29,34,28,300,
        41,35,27,None,None
    ],
    
    "Salary": [
        55000,48000,62000,50000,45000,
        70000,58000,61000,47000,52000,
        69000,56000,63000,49000,54000,
        72000,64000,60000,None,None
    ]
}

df = pd.DataFrame(data)
# print(df.head(7))
# print(df.tail(3))
# print(df.info())
# print(df.shape)
# print(df.describe())
# print(df.columns)
# print(df.dtypes)

# print(df.nunique())
# print(df.sample(3))
# print()

# print(df)

# print(df["Name"].str.lower())
# print(df)
df["Name"]=df["Name"].str.lower().str.strip()
# df["Name"]=df["Name"].str.strip()
df["Department"]=df["Department"].str.upper()

df["Department"]=df["Department"].str.replace("Finance","fin",case=False)


df["Department"].str.contains("fin",case=False,na=False)





# print(df[df["Department"].str.contains("fin",case=False,na=False)])
# df["Join_Date"]=pd.to_datetime(df["Join_Date"])

df["year"]=df["Join_Date"].dt.year.astype("int64")
# df["mnth"]=df["Join_Date"].dt.month.astype("Int64")
# df["date"]=df["Join_Date"].dt.day.astype("Int64")
# df["day"]=df["Join_Date"].dt.day_name()

# print(df)
# print(df["Salary"].max())
# print(df["Salary"].min())
# print(df["Salary"].mean())
# print(df["Salary"].sum())
# print(df["Salary"].count())


# print(df["Age"].min())
# print(df["Age"].max())

# print(df["Age"].mean())
a=df.pivot_table(
    values="Salary",
    index="Department",
    aggfunc=["mean","max","min","sum","count"]
).astype("int64")

print(a)


# viewing functions
# str functions
# datetime functions
# aggregation functions

