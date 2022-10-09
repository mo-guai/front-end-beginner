# 要求一:Python 取得網路上的資料並儲存到檔案中
# 台北市政府提供景點公開資料連線網址如下:
# https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json
# 請撰寫一隻 Python 程式，能從以上網址取得資料，並且將景點資料用一行一筆資料，每個欄 位用逗號隔開的格式，輸出到 data.csv 的檔案中，請將生成的 data.csv 檔案包含在你的作業 資料夾中。
# 請根據 xpostDate 欄位，僅輸出 2015 年以後 ( 包含 2015 年 ) 的資料。
# 提醒:區域資料請參考原始資料的地址欄位，必須是三個字，並且為以下區域的其中一個:中 正區、萬華區、中山區、大同區、大安區、松山區、信義區、士林區、文山區、北投區、內湖區、 南港區。

from turtle import screensize
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式

clist=data["result"]["results"] #來自於json檔案中的設定 將全部資料存進clist
# print(clist) #確認

with open("data.csv", "w", encoding="utf-8") as file:#建立檔案 並存入資料
    for attraction in clist:
         if (attraction["xpostDate"])>="2015/01/01":
            allPic=attraction["file"] #全部照片
            firstPic=str(allPic.split("https:")[1]) #只要第一張照片 str()將資料轉換成字串  split()切割字串  [1]是因為切割後[0]是空的 
            
            file.write(attraction["stitle"]+","+attraction["address"][5:8]+","+attraction["longitude"]+","+attraction["latitude"]+","+"http:"+firstPic+"\n")
            #["address"][5:8]取第五個字到第七個字
