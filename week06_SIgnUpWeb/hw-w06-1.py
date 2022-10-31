from crypt import methods
from flask import Flask #載入Flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template
from flask import url_for #避免寫死路由
from flask import session

app = Flask(__name__,
            static_folder="static",
            static_url_path="/"
        ) #建立App物件 可以設定靜態檔案的路徑

from flask import session #使用者狀態管理 
app.secret_key="any string but secret"

import mysql.connector
import pymysql

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="week06"
)
# 使用cursor()方法获取操作游标 
cursor = mydb.cursor()


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    membername = request.form["membername"]
    username = request.form["username"]
    password = request.form["password"]
    
    member_search = "SELECT username FROM member WHERE username = %s"
    cursor.execute(member_search, (username,))
    userIsExist = cursor.fetchone()  #取得資料庫已有的相同名稱帳號

    if userIsExist:
        session["status"]='fail'
        return render_template("error.html", message="此帳號已被註冊")

    elif not membername or not username or not password:
        session["status"]='fail'
        return render_template("error.html", message="欄位不可為空白")
    else:
        session["name"] =  membername  
        session["username"] = username
        session["password"] = password
    #傳值到資料庫 方法一
    #sql=f"INSERT INTO member(name,username,password) VALUES ({membername},{username},{password})"
    #cursor.execute(sql)  #提交到資料庫
    #傳值到資料庫 方法二
        sql="INSERT INTO member(name,username,password) VALUES (%s, %s, %s)"
        val = (membername, username, password)
        cursor.execute(sql, val)
        mydb.commit()  # 提交到資料庫執行
        return redirect("/")

@app.route("/signin" ,methods=["POST"])
def signin():
    username=request.form["username"] #request.form[""] POST的寫法 
    password=request.form["password"]
    session["username"] = username #用session記錄資訊
    session["password"] = password
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password,))
    member_data=cursor.fetchone() #把抓到的資料存到member_data裡
    #print(type(member_data))

    if member_data:
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
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (username, password,))
    member_data=cursor.fetchone() #把抓到的資料存到member_data裡

    if (session["status"]=='ok'):
        return render_template("member.html", membername=member_data[1])
    else:
        return redirect("/") #防止直接用網址登入


   
@app.route("/error")
def error():
    session["status"]='fail'
    return render_template("error.html", message="帳號或密碼輸入錯誤")
    

@app.route("/signout")
def signout():
    session["status"]='fail'
    return redirect("/")



app.run(port=3000) #啟動網站伺服器，可透過port參數指定埠號
