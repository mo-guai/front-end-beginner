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
    

@app.route("/signout")
def signout():
    session["status"]='fail'
    return redirect("/")


#方法ㄧ
#@app.route("/calculate")
# def calculate():
#     squareNumber=request.args.get("inputNumber","")
#     squareNumber=int(squareNumber)
#     squareNumber=squareNumber*squareNumber
#     return render_template("squareResult.html",result="運算的結果是"+str(squareNumber))

#方法二 動態路由 (Flask Dynamic Routing)
#Flask 中動態路由是指帶有引數的頁面路徑 將引數放置在符號 < > 之間
#動態路由的引數型別預設是string
@app.route("/calculate/<inputNum>")
def calculate(inputNum):
    inputNum=int(inputNum)
    squareNum=inputNum*inputNum
    
    return render_template("squareResult.html",result=str(squareNum)) #傳到index頁面
    



app.run(port=3000) #啟動網站伺服器，可透過port參數指定埠號