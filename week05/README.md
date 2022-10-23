第五週作業
======
作業繳交方式:
1. 透過 mysqldump 工具，將資料庫中的資料匯出到檔案 data.sql，並繳交此檔案。
2. 要求三、四、五的部份:請建立 / 編輯 GitHub Repository 資料夾 week-5 中的
README.md 檔案，把你寫的每個 SQL 指令，以及各指令執行畫面的截圖呈現出 來。

要求一:安裝 MySQL 伺服器
請至官方網站下載，並安裝 MySQL 8.0 以上版本的伺服器在電腦中，注意安裝時設定的帳 號、密碼等關鍵資訊。

要求二:建立資料庫和資料表
透過任何方式 ( 建議使用終端機 Command Line 介面，為第二階段操作 Linux 系統打基礎 )， 連結到 MySQL 伺服器中進行管理，完成以下動作:

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-2-0.png" width="50%">

要求三:
------
SQL CRUD 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令:
● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
        
        CREATE TABLE member(id bigint PRIMARY KEY AUTO_INCREMENT,
        name varchar(255) NOT NULL,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL,
        follower_count int NOT NULL DEFAULT 0,
        time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);

        INSERT INTO member(name,username,password) VALUES('test','test','test');
        INSERT INTO member(name,username,password) VALUES('Ken','KenAccount','KenKey');
        INSERT INTO member(name,username,password) VALUES('Joe','JoeAccount','JoeKey');
        INSERT INTO member(name,username,password) VALUES('Zoe','ZoeAccount','ZoeKey');
        INSERT INTO member(name,username,password) VALUES('Amy','AmyAccount','AmyKey');

        SELECT* FROM member;
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-1.png" width="50%">


● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

        SELECT * FROM member order by time desc;
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-2.png" width="50%">


● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

        SELECT * FROM member order by time desc limit 1, 3;
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-3.png" width="50%">


● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

        SELECT * FROM member WHERE username = 'test';
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-4.png" width="50%">

       
        
        
● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

         SELECT * FROM member WHERE username = 'test' and password='test';
         
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-5.png" width="50%">


● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

        UPDATE member SET NAME = 'test2' WHERE username = 'test';
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-6.png" width="50%">





要求四:
------
SQL Aggregate Functions 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令:
● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

        SELECT COUNT(*) from member;

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-4-1.png" width="50%">



● 取得 member 資料表中，所有會員 follower_count 欄位的總和。

        SELECT SUM(follower_count) from member;

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-4-2.png" width="50%">



● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

        SELECT AVG(follower_count) from member;

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-4-3.png" width="50%">


        

要求五:SQL JOIN (Optional)
------
在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以
下欄位設定:
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-5-0.png" width="50%">

        CREATE TABLE message(id bigint PRIMARY KEY AUTO_INCREMENT,
        member_id bigint NOT NULL,
        content varchar(255) NOT NULL,
        like_count int NOT NULL DEFAULT 0,
        time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(member_id) REFERENCES member(id));
        
        SHOW COLUMNS FROM message;

● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

        SELECT member.name , message.content FROM message INNER JOIN member ON message.member_id = member.id
        

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-5-1.png" width="50%">




● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

        SELECT member.name , message.content FROM message INNER JOIN member ON message.member_id = member.id WHERE member.username = 'test';

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-5-2.png" width="50%">
 

● 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。

        SELECT member.username , avg(message.like_count) FROM message INNER JOIN member ON message.member_id = member.id WHERE member.username = 'test';

<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-5-3.png" width="50%">


