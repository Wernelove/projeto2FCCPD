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
('Usuário 1', 'usuario1@email.com'),
('Usuário 2', 'usuario2@email.com'),
('Usuário 3', 'usuario3@email.com');

INSERT INTO livros (titulo, autor, status) VALUES
('Livro 1', 'Autor 1', 'Disponível'),
('Livro 2', 'Autor 2', 'Disponível'),
('Livro 3', 'Autor 3', 'Disponível');

INSERT INTO alugueis (usuario_id, livro_id, data_aluguel) VALUES
(1, 1, '2023-11-23'),
(2, 2, '2023-11-24'),
(3, 3, '2023-11-25');