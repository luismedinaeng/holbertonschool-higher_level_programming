-- Creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Set password for user
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
-- set privileges for user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- Update privileges
FLUSH PRIVILEGES;
