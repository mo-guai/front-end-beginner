

要求三:SQL CRUD 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令:
使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
使用 SELECT 指令取得所有在 member 資料表中的會員資料。
        
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


使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

        SELECT * FROM member order by time desc;
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-2.png" width="50%">


使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

        SELECT * FROM member order by time desc limit 1, 3;
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-3.png" width="50%">


使用 SELECT 指令取得欄位 username 是 test 的會員資料。

        SELECT * FROM member WHERE username = 'test';
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-4.png" width="50%">

       
        
        
使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

         SELECT * FROM member WHERE username = 'test' and password='test';
         
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-5.png" width="50%">


使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改
成 test2。

        UPDATE member SET NAME = 'test2' WHERE username = 'test';
        
<img src="https://github.com/mo-guai/front-end-beginner/blob/main/week05/week05-img/Week05-3-6.png" width="50%">





要求四:
======
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
