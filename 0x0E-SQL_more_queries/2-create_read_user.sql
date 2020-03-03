-- Creates the database hbtn_0d_2 and user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_d0_2_pwd';
GRANT SELECT ON `hbtn_02_d`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
