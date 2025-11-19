import pandas as p 
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 20000],
    "Profit": [3000, 3500, 4200, 3900, 4500, 5000],
    "Customers": [120, 140, 160, 155, 180, 200],
    "Marketing_Spend": [2000, 2200, 2500, 2400, 2600, 3000],
    "Rating": [4.1, 4.3, 4.0, 4.2, 4.4, 4.5]
}
df=p.DataFrame(data)
# print(df)

# df.plot()
# plt.show()


# plt.bar(df["Month"],df["Sales"],color=["red","green","purple","black"])
# plt.bar(df["Month"],df["Profit"],color="yellow")
# plt.legend(["Sales","Profit"])
# plt.show()




# plt.barh(df["Month"],df["Sales"],color=["red","green","purple","black"])
# plt.barh(df["Month"],df["Profit"],color="yellow")
# plt.legend(["Sales","Profit"])
# plt.show()

# plt.pie(df["Sales"],labels=df["Month"],autopct="%1.0f%%")
# plt.title("Sales Distribution")
# plt.show()


# plt.fill_between(df["Month"], df["Sales"], alpha=0.3) 
# plt.title("Sales Area Chart")
# plt.show()



ig, axs = plt.subplots(2, 3, figsize=(14, 7))   # 2 rows, 3 columns

# 1️⃣ Line Chart
axs[0,0].plot(df["Month"], df["Sales"], marker="o")
axs[0,0].set_title("Line Chart - Sales")

# 2️⃣ Bar Chart
axs[0,1].bar(df["Month"], df["Sales"], color="skyblue")
axs[0,1].set_title("Bar Chart - Sales")

# 3️⃣ Pie Chart
axs[0,2].pie(df["Sales"], labels=df["Month"], autopct="%0.1f%%")
axs[0,2].set_title("Pie Chart - Sales")

# 4️⃣ Horizontal Bar Chart
axs[1,0].barh(df["Month"], df["Profit"], color="orange")
axs[1,0].set_title("Horizontal Bar Chart - Profit")

# 5️⃣ Area Chart
axs[1,1].fill_between(df["Month"], df["Sales"], alpha=0.5)
axs[1,1].set_title("Area Chart - Sales")

# 6️⃣ Keep last grid empty or use Profit Line Chart
axs[1,2].plot(df["Month"], df["Profit"], color="green", marker="o")
axs[1,2].set_title("Line Chart - Profit")

plt.tight_layout()
plt.show()
