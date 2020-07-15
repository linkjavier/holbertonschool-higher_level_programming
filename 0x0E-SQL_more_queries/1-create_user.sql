-- Script that creates the MySQL server user user_0d_1:
-- User_0d_1  have all privileges on your MySQL server
-- The user_0d_1 password is set to user_0d_1_pwd
-- If the user user_0d_1 already exists, this script do not fail.
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
