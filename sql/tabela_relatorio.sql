CREATE DATABASE IF NOT EXISTS contabeis;

USE contabeis;

CREATE TABLE relatorio (
	id INT AUTO_INCREMENT PRIMARY KEY,
    Registro_ANS CHAR(6),
    CNPJ CHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255) DEFAULT "N/A",
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(100),
    Numero VARCHAR(100),
    Complemento VARCHAR(100) DEFAULT "NA",
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP CHAR(8),
    DDD CHAR(2) DEFAULT "00",
    Telefone VARCHAR(18) DEFAULT "N/A",
    Fax varchar(100) DEFAULT "N/A",
    Endereco_eletronico VARCHAR(255) DEFAULT "N/A",
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao CHAR(1) DEFAULT "0",
    Data_Registro_ANS DATE
);

