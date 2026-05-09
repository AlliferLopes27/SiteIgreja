CREATE DATABASE igreja_db;

USE igreja_db;

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255)
);

CREATE TABLE eventos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150),
    descricao TEXT,
    data DATE,
    hora TIME
);

CREATE TABLE pedidos_oracao (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    pedido TEXT,
    data_envio DATETIME
);