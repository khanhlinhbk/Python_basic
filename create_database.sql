DROP DATABASE IF EXISTS demo;

CREATE DATABASE demo;

CREATE TABLE demo.students (
    id INT(3) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(50) NOT NULL,
) ENGINE=InnoDB AUTO_INCREMENT=101;

INSERT INTO demo.students (name, dob, email)
VALUES ("Ba Nguyễn", "1992-05-24", "ba@techmaster.vn");