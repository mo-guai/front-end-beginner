# 要求二:Python 網頁爬取資料並儲存到檔案中 (Optional) PTT 電影版的網址如下:
# https://www.ptt.cc/bbs/movie/index.html
# 請撰寫一隻 Python 程式，從以上網頁爬取每一篇文章的標題，並且能持續往上一頁爬取，總 共爬取十頁。本題開放使用 BeautifulSoup 這個第三方套件。
# 程式在取得標題後，以一行一標題的格式，輸出到 movie.txt 中，將生成的 movie.txt 檔案包含 在你的作業資料夾中，並符合以下規範:
# 1. 僅輸出開頭為 [好雷]、[普雷]、[負雷] 的文章標題。
# 2. 輸出時，先輸出 [好雷] 開頭的所有標題，然後依序輸出 [普雷] 和 [負雷] 開頭的所有標題。

from urllib import response
import urllib.request as req

goodList=[]
notbadList=[]
badList=[]

def getData(url):

    #-----要假裝自己是一般使用者 建立Request物件，附加Request Headers 的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)#抓到網站原始碼
        
        
    #-----解析原始碼 取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")

    # print(root.title) #標題
    # print(root.title.string) #標題文字

    #-----抓到所有標題    
    titles=root.find_all("div", class_="title")  #尋找所有 class="title"的div標籤
    # print(titles) #會看到中括號 代表是一個列表

   
    for title in titles:
        if title.a != None:
            # print(title.a.string)
            titleText=title.a.string[1:3] #[好雷] 取 好雷 兩個字
            if (titleText == "好雷" or titleText =="普雷" or titleText =="負雷"):
                if titleText == "好雷":
                    goodList.append(title.a.string)
                if titleText == "普雷":
                    notbadList.append(title.a.string)
                if titleText == "負雷":
                    badList.append(title.a.string)
               
    #-----抓上一頁網址
    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]

#-----抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/movie/index.html"
print(pageURL)

#-----抓上10頁的網址
count=0
while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1

#-----存入movie.txt檔案
with open("movie.txt", "w", encoding="utf-8") as file:
    for titleData in goodList:
        file.write(titleData+"\n")
    for titleData in notbadList:
        file.write(titleData+"\n")
    for titleData in badList:
        file.write(titleData+"\n")










# with open("movie.txt ", "w", encoding="utf-8") as file:

                
                 

            

