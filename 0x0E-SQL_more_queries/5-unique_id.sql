-- Creates the table unique_id
-- With id default value = 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
	      	     	    		 name VARCHAR(256));
