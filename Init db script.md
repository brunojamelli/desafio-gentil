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
CREATE PROCEDURE InserirPessoa
(
  @Objetivo VARCHAR(255),
  @nome VARCHAR(255),
  @dataNascimento DATE,
  @salario DECIMAL(10, 2),
  @observacoes TEXT,
  @idPessoa INT OUTPUT
)
AS
BEGIN
  SET NOCOUNT ON;

  INSERT INTO Pessoas (Objetivo, nome, dataNascimento, salario, observacoes)
  VALUES (@Objetivo, @nome, @dataNascimento, @salario, @observacoes);

  SET @idPessoa = SCOPE_IDENTITY();
END;
```

### Procedure para atualizar Pessoa
```sql
CREATE PROCEDURE AtualizarPessoa
(
  @idPessoa INT,
  @Objetivo VARCHAR(255),
  @nome VARCHAR(255),
  @dataNascimento DATE,
  @salario DECIMAL(10, 2),
  @observacoes TEXT,
  @result VARCHAR(2) OUTPUT
)
AS
BEGIN
  SET NOCOUNT ON;

  UPDATE Pessoas
  SET Objetivo = @Objetivo,
      nome = @nome,
      dataNascimento = @dataNascimento,
      salario = @salario,
      observacoes = @observacoes
  WHERE idPessoa = @idPessoa;

  SET @result = 'OK';
END;
```