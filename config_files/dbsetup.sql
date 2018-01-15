-- create user credentials for flask and database
CREATE USER IF NOT EXISTS 'flask'@'%' IDENTIFIED BY 'f1ask';
CREATE DATABASE IF NOT EXISTS url_db;
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON url_db.* TO 'flask'@'%';
FLUSH PRIVILEGES;
