USE contabeis;

LOAD DATA INFILE 'Relatorio_cadop.csv'
INTO TABLE relatorio
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
SET 
    Registro_ANS = LEFT(TRIM(@Registro_ANS), 6);
