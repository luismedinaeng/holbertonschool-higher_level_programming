-- Creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user and set privileges
GRANT SELECT ON `hbtn_02_d`.* TO 'user_0d_2'@'localhost'
      IDENTIFIED BY 'user_0d_2_pwd';
-- Update privileges
FLUSH PRIVILEGES;
