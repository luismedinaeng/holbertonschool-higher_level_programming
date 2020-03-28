-- Creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table states
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT,
       	     	    	   	   name VARCHAR(256));
