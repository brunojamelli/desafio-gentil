# Script Criação de banco de dados
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
ALTER TABLE Pessoas
ADD nomeMae VARCHAR(255),
    nomePai VARCHAR(255),
    cpf VARCHAR(11);
```
### Adição de indices para buscas mais rápidas
CREATE INDEX idx_nome ON Pessoas (nome);
CREATE INDEX idx_dataNascimento ON Pessoas (dataNascimento);



