CREATE DATABASE
IF NOT EXISTS test_db;
USE test_db;

CREATE TABLE
IF NOT EXISTS TpTable
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    value VARCHAR(255)

);


-- Insérer des données dans la table TpTable
INSERT INTO TpTable
    (value)
VALUES
    ('data1'),
    ('data2'),
    ('data3'),
    ('data4');
