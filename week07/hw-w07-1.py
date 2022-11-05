from crypt import methods
import json
from unittest import result
from flask import Flask #載入Flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template
from flask import url_for #避免寫死路由
from flask import session
from flask import jsonify

app = Flask(__name__,
            static_folder="static",
            static_url_path="/"
        ) #建立App物件 可以設定靜態檔案的路徑

from flask import session #使用者狀態管理 
app.secret_key="any string but secret"


import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="week07"
)
# 使用cursor()方法获取操作游标 
cursor = mydb.cursor()


#設置API
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    membername = request.form["membername"]
    username = request.form["username"]
    password = request.form["password"]
    
    cursor.execute("SELECT username FROM member WHERE username = %s", (username,))  #(username,)是tuple
    userIsExist = cursor.fetchone()  #取得資料庫已有的相同名稱帳號

    if userIsExist:
        session["status"]='fail' 
        return render_template("error.html", message="此帳號已被註冊")

    elif not membername or not username or not password:
        session["status"]='fail'
        return render_template("error.html", message="欄位不可為空白")
    else:
        session["membername"] =  membername  #紀錄註冊資訊
        session["username"] = username
        session["password"] = password
    #傳值到資料庫 方法一
    #sql=f"INSERT INTO member(name,username,password) VALUES ({membername},{username},{password})"
    #cursor.execute(sql)  #提交到資料庫
    #傳值到資料庫 方法二
        cursor.execute("INSERT INTO member(name,username,password) VALUES (%s,%s,%s)", (membername,username,password))
        mydb.commit()  # 提交到資料庫執行
        return redirect("/")

@app.route("/signin" ,methods=["POST"])
def signin():
    username=request.form["username"] #request.form[""] POST的寫法 
    password=request.form["password"]
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password,)) 
    member_data=cursor.fetchone() #把抓到的資料存到member_data裡  (username, password,)是tuple
    print(type(member_data))
    print((member_data))


    if member_data: #註冊成功後
        session["username"] = username #用session記錄登入資訊
        session["password"] = password
        session["id"]=member_data[0] #用session記錄成功登入時的ID
        session["membername"]=member_data[1] 
        session["status"]='ok'
        #return render_template("member.html",)
        
        return redirect("/member")

    #if (username =="" and password=="") :
    elif not username or not password:
        session["status"]='fail'
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        session["status"]='fail'
        return redirect("/error?message=帳號、密碼錯誤")
        
@app.route("/member")
def member():
    username=session["username"] #用session記錄資訊
    password=session["password"]
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s",(username, password,))
    member_data=cursor.fetchone() #把抓到的資料存到member_data裡
    session["membername"] = member_data[1]
    # print(type(member_data[1]))
    # print(member_data[1])
    cursor.execute("SELECT member.name, message.message FROM member INNER JOIN message on member.id = message.member_id ORDER BY message.time desc") #選取會員名稱 及留言內容
    all_message=cursor.fetchall()
    # print(all_message)
    # print(all_message[0])
    # print(all_message[1])


    if (session["status"]=='ok'):
        if("newmembername" in session):
            session["membername"]=session["newmembername"]
        return render_template("member.html", membername=session["membername"], all_message = all_message,)
    else:
        return redirect("/") #防止直接用網址登入

@app.route("/api/member",methods=["GET","PATCH"])
def api_member():
    if request.method =="GET":
        searchmembername=(request.args.get("username"),) #是tuple  取得用會查詢的名子
        cursor.execute("SELECT id, name, username FROM member WHERE username = %s" , (searchmembername)) #比對資料庫是否有此人(seachername,)是tuple
        userIsExist=cursor.fetchone()
        print(type(userIsExist))
        print(userIsExist)
        # result={"data":userIsExist}

        if userIsExist != None:
            return jsonify({
                #json格式設定
                "data":{
                    "id":userIsExist[0],
                    "name":userIsExist[1],
                    "username":userIsExist[2],
                }
            })
        return jsonify({
            "data":None
        })

    if request.method =="PATCH":
        if("username" in session): #如果用戶有登入
            membername = session["membername"]
            username =session["username"]
            request_data=request.get_json("name") #request.get_json()將 JSON 對象轉換為 Python 數據
            if 'name' in request_data:
                newmembername = request_data["name"]

                cursor.execute("UPDATE member SET name = %s WHERE username = %s",(newmembername,username))
                mydb.commit() 
                session[membername]= newmembername
                session[newmembername]= newmembername
                
            return jsonify({"ok":True})
        return  jsonify({"error":True})


        
# 連線到【留言功能網址】，後端程式接收使用者輸入的資料，並根據登入時在
# Session 紀錄的使用者編號，將留言內容紀錄到 message 資料表。  
@app.route("/message" ,methods=["POST"])
def message():
    member_id=session["id"]
    print(member_id)
    new_message = request.form["message"]
    cursor.execute("INSERT INTO message(member_id,message) VALUES(%s,%s)", (member_id, new_message)) #new_message是str（字串）
    mydb.commit()  # 提交到資料庫執行

    return redirect("/member")


@app.route("/error")
def error():
    session["status"]='fail'
    return render_template("error.html", message="帳號或密碼輸入錯誤")
    

@app.route("/signout")
def signout():
    session["status"]='fail'
    return redirect("/")





app.run(port=3000) #啟動網站伺服器，可透過port參數指定埠號