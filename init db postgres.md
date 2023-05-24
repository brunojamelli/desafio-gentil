# Script Criação de banco de dados para Postgres
## Desafio A - Banco de Dados
Script de desafio criação do banco de dados do desafio para vaga de desenvolvedor da gentil negocios.

### Criando a estrutura base do Banco
```sql
create database gentil_db;
```

```sql
CREATE TABLE Pessoas (
  idPessoa INT PRIMARY KEY,
  Objetivo VARCHAR(255),
  nome VARCHAR(255),
  dataNascimento DATE,
  salario DECIMAL(10, 2),
  observacoes TEXT
);
```

### Alteração da tabela Pessoas adicionando atributos

```sql
ALTER TABLE Pessoas ADD nomeMae VARCHAR(255);
ALTER TABLE Pessoas ADD nomePai VARCHAR(255);
ALTER TABLE Pessoas ADD cpf VARCHAR(11);
```

### Adição de indices para buscas mais rápidas

```sql
CREATE INDEX idx_nome ON Pessoas (nome);
CREATE INDEX idx_dataNascimento ON Pessoas (dataNascimento);
```
### Alteração do atributo cpf indice/chave única

```sql
ALTER TABLE Pessoas
ADD CONSTRAINT uq_cpf UNIQUE (cpf);
```
### Procedure para inserir Pessoa
```sql
CREATE OR REPLACE PROCEDURE inserir_pessoa(
  in_objetivo VARCHAR(255),
  in_nome VARCHAR(255),
  in_data_nascimento DATE,
  in_salario NUMERIC,
  in_observacoes TEXT,
  in_nome_mae VARCHAR(255),
  in_nome_pai VARCHAR(255),
  in_cpf VARCHAR(11),
  OUT out_id_pessoa INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO Pessoas (Objetivo, nome, dataNascimento, salario, observacoes, nomeMae, nomePai, cpf)
  VALUES (in_objetivo, in_nome, in_data_nascimento, in_salario, in_observacoes, in_nome_mae, in_nome_pai, in_cpf)
  RETURNING idPessoa INTO out_id_pessoa;
END;
$$;

```