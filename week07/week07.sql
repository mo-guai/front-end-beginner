SHOW DATABASES;
CREATE DATABASE week07;
USE week07;
SHOW TABLES;
CREATE TABLE member(id bigint PRIMARY KEY AUTO_INCREMENT,
name varchar(255) NOT NULL,
username varchar(255) NOT NULL,
password varchar(255) NOT NULL,
time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
SELECT*FROM member;
INSERT INTO member(name,username,password)VALUES('TEST','test','test');
SELECT name FROM member WHERE username ='123';
DROP DATABASE week07;
DROP TABLE member;
alter table member add comment varchar(255);


CREATE TABLE message(id bigint PRIMARY KEY AUTO_INCREMENT,
member_id bigint NOT NULL,
message varchar(255),
FOREIGN KEY (member_id) REFERENCES member(id),
time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
INSERT INTO message(member_id,message)VALUES(1,'I am test');
SELECT*FROM message;

DROP TABLE message;


