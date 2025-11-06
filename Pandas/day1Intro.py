import pandas as p
# # # print(pandas.Series()) ([],dtype:Object)

# # # data=p.Series(["10","20"],index=["a","b","c"]) # (data,dType:Object)
# # # print(data)


# # # data=p.Series(["10","20",1,2,3,4,5],index=["a","b","c"]) # (data,dType:Object)
# # # print(data)


# # # data=p.Series(["10","20",1,2,3,4,5],index=["a","b","c"]) # (data,dType:Object)
# # # print(data)

# # # data=p.Series(10,index=["a","b","c"]) # (data,dType:Object)
# # # print(data)


# # # data=p.Series((10,20,30),index=["a","b","c"]) # (data,dType:Object)
# # # print(data)




# # # data=p.Series({"id":1,"name":"vamsi"}) # (data,dType:Object)
# # # print(data)


# # # data=p.Series({"id":1,"name":"vamsi"},index=["id","name"]) # (data,dType:Object)
# # # print(data)
# # data=p.Series([1,2,3,4,5,6],index=[1,2,3,4,5,6]) # (data,dType:Object)
# # print(data)
# # # print(data.index)
# # # print(data["a"])
# # # print(data["c"])
# # # print(data[["a","c"]])

# # # print(data["a":"d"])
# # # print(data[0:3])
# # print(data[0:5]) # 1 2 3 4 5



# data=p.Series([1,2,3],index=["a","a","b"],columns=["age"])
# print(data)

# # print(data % 5)


# data=p.Series(["Vamsi","Ravi",True,100],index=["a","b","c","d"])
# # print(list(data.items())[2][1])
# data["e"]="10000coders"
# data[["f","g"]]=10,20
# print(data)


data=p.DataFrame([("vamsi",11,"trainer"),("ravi",10),("raju",22)],index=["a","b","c"],columns=["name","age","role"])
print(data)



