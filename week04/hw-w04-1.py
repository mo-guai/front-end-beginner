from flask import Flask #載入Flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template
from flask import url_for #避免寫死路由

app = Flask(__name__
        #   static_folder="static",
        #   static_url_path="/"
        ) #建立App物件 可以設定靜態檔案的路徑

from flask import session #使用者狀態管理 
app.secret_key="any string but secret"


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/signin" ,methods=["POST"])
def signin():
    username=request.form["username"] #request.form[""] POST的寫法 
    password=request.form["password"]
   
    if (username == "test" and password =="test") :
        session["status"]='ok'
        return redirect("/member")
    if (username =="" and password=="") :
        session["status"]='fail'
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        session["status"]='fail'
        return redirect("/error?message=帳號、密碼錯誤")

@app.route("/member")
def member():
    if (session["status"]=='ok'):
        return render_template("member.html")
    else:
        return redirect("/") #防止直接用網址登入
   
@app.route("/error")
def error():
    session["status"]='fail'
    return render_template("error.html", message="帳號或密碼輸入錯誤")
    

@app.route("/calculate")
def calculate():
    squareNumber=request.args.get("inputNumber","")
    squareNumber=int(squareNumber)
    squareNumber=squareNumber*squareNumber
    return render_template("squareResult.html",data="運算的結果是"+str(squareNumber))

@app.route("/signout")
def signout():
    session["status"]='fail'
    return redirect("/")



app.run(port=3000) #啟動網站伺服器，可透過port參數指定埠號