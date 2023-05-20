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
ADD nomeMae VARCHAR(255), nomePai VARCHAR(255), cpf VARCHAR(11);
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

### Procedure para remover Pessoa

```sql
CREATE PROCEDURE RemoverPessoa
(
  @idPessoa INT,
  @result VARCHAR(2) OUTPUT
)
AS
BEGIN
  SET NOCOUNT ON;

  DELETE FROM Pessoas
  WHERE idPessoa = @idPessoa;

  SET @result = 'OK';
END;
```
### Procedure para listar todos os registros da tabela 'Pessoa'

```sql
CREATE PROCEDURE SelecionarTodasPessoas
AS
BEGIN
  SET NOCOUNT ON;

  SELECT * FROM Pessoas;
END;
```
### Procedure para obter um registro por Id da pessoa

```sql
CREATE PROCEDURE ObterPessoaPorId
(
  @idPessoa INT
)
AS
BEGIN
  SET NOCOUNT ON;

  SELECT * FROM Pessoas WHERE idPessoa = @idPessoa;
END;
```
### Inserção de dados na tabela de Pessoas através da procedure 

```sql
DECLARE @outputIdPessoa INT;
EXEC InserirPessoa 'objetivo de teste', 'Oscar Ramires', '2000-01-01', 1000.00, 'Observações Exemplo', @outputIdPessoa OUTPUT;
SELECT @outputIdPessoa AS 'idPessoa';
```
### Atualização de dados na tabela de Pessoas através da procedure 
```sql
DECLARE @outputResult VARCHAR(2);
EXEC AtualizarPessoa 1, 'Novo Objetivo', 'Novo Nome', '2000-01-01', 2000.00, 'Novas Observações', @outputResult OUTPUT;
SELECT @outputResult AS 'Result';
```
### Remoção de dados na tabela de Pessoas através da procedure 
```sql
DECLARE @outputResult VARCHAR(2);
EXEC RemoverPessoa 1, @outputResult OUTPUT;
SELECT @outputResult AS 'Result';
```

### Selecionando registros na tabela de Pessoas através da procedure

```sql
EXEC SelecionarTodasPessoas;
```

### Selecionando um registro na tabela de Pessoas através da procedure

```sql
EXEC ObterPessoaPorId 1;
```

