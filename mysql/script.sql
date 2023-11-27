-- Nome do banco de dados
USE banco_blibli;

-- Script de criação de tabelas

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    status ENUM('Disponível', 'Alugado') NOT NULL
);

CREATE TABLE alugueis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    livro_id INT,
    data_aluguel DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Script de inserção de dados

INSERT INTO usuarios (nome, email) VALUES
('lucas', 'usuario1@email.com'),
('fernando', 'usuario2@email.com'),
('jose', 'usuario3@email.com');

INSERT INTO livros (titulo, autor, status) VALUES
('romeu e julieta', 'Shakespeare', 'Disponível'),
('assim falou zaratrusta', 'Nietzsche', 'Disponível'),
('diario de um banana', 'Jeff', 'Disponível');
