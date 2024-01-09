#!/usr/bin/mysql
-- Prepare a MySQL server for tha project 

-- Create the database if not existing
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;

CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
