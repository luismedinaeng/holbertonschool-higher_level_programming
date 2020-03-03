-- Creates the database hbtn_0d_2 and user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_02_d`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
