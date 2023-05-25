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

### Deixando o atributo idPessoa como autoincremento
- Crie uma nova sequência (sequence) no PostgreSQL:
```sql
CREATE SEQUENCE idPessoa_seq;
```
- Atualize o valor da coluna idPessoa na tabela Pessoas para usar a sequência criada:
```sql
ALTER TABLE Pessoas ALTER COLUMN idPessoa SET DEFAULT nextval('idPessoa_seq');
```
- Defina a sequência como a propriedade de autoincremento da coluna **idPessoa**:
```sql
ALTER SEQUENCE idPessoa_seq OWNED BY Pessoas.idPessoa;
```
Agora, sempre que um novo registro for inserido na tabela Pessoas sem especificar um valor para a coluna idPessoa, o PostgreSQL irá gerar automaticamente um valor incrementado com base na sequência idPessoa_seq.
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

### Procedure para atualizar Pessoa
```sql
CREATE OR REPLACE PROCEDURE atualizar_pessoa(
  in_id_pessoa INTEGER,
  in_objetivo VARCHAR(255),
  in_nome VARCHAR(255),
  in_data_nascimento DATE,
  in_salario NUMERIC,
  in_observacoes TEXT,
  in_nome_mae VARCHAR(255),
  in_nome_pai VARCHAR(255),
  in_cpf VARCHAR(11),
  OUT out_resultado VARCHAR(2)
)
LANGUAGE plpgsql
AS $$
BEGIN
  UPDATE Pessoas
  SET
    Objetivo = in_objetivo,
    nome = in_nome,
    dataNascimento = in_data_nascimento,
    salario = in_salario,
    observacoes = in_observacoes,
    nomeMae = in_nome_mae,
    nomePai = in_nome_pai,
    cpf = in_cpf
  WHERE idPessoa = in_id_pessoa;
  
  out_resultado := 'OK';
END;
$$;

```

### Procedure para remover Pessoa

```sql
CREATE OR REPLACE PROCEDURE remover_pessoa(
  in_id_pessoa INTEGER,
  OUT out_resultado VARCHAR(2)
)
LANGUAGE plpgsql
AS $$
BEGIN
  DELETE FROM Pessoas
  WHERE idPessoa = in_id_pessoa;
  
  out_resultado := 'OK';
END;
$$;

```
### Procedure para listar todos os registros da tabela 'Pessoa'

```sql
CREATE OR REPLACE PROCEDURE selecionar_todas_pessoas(
  OUT out_resultado REFCURSOR
)
LANGUAGE plpgsql
AS $$
BEGIN
  OPEN out_resultado FOR SELECT * FROM Pessoas;
END;
$$;
```
### Procedure para obter um registro por Id da pessoa

```sql
CREATE OR REPLACE PROCEDURE obter_pessoa_por_id(
  in_id_pessoa INTEGER,
  OUT out_resultado Pessoas%ROWTYPE
)
LANGUAGE plpgsql
AS $$
BEGIN
  SELECT * INTO out_resultado FROM Pessoas WHERE idPessoa = in_id_pessoa;
END;
$$;
```

### Inserção de dados na tabela de Pessoas através da procedure 
```sql
DO $$
DECLARE
  id_pessoa INTEGER;
BEGIN
  CALL inserir_pessoa('Objetivo novo', 'Oscar Ramirez', '1990-01-01', 1000.00, 'Observações exemplo', 'Nome da Mãe', 'Nome do Pai', '12345678921', id_pessoa);
  -- O valor do campo idPessoa será armazenado na variável id_pessoa
  -- Você pode utilizar esse valor conforme necessário na sua aplicação
END;
$$;
```
### Atualização de dados na tabela de Pessoas através da procedure 
```sql
DO $$
DECLARE
  resultado VARCHAR(2);
BEGIN
  CALL atualizar_pessoa(1, 'Novo objetivo', 'Novo nome', '1990-01-01', 2000.00, 'Novas observações', 'Nova mãe', 'Novo pai', '98765232109', resultado);
  -- O valor "OK" será armazenado na variável resultado
  -- Você pode utilizar esse valor conforme necessário na sua aplicação
END;
$$;
```
### Remoção de dados na tabela de Pessoas através da procedure 

```sql
DO $$
DECLARE
  resultado VARCHAR(2);
BEGIN
  CALL remover_pessoa(1, resultado);
  -- O valor "OK" será armazenado na variável resultado
  -- Você pode utilizar esse valor conforme necessário na sua aplicação
END;
$$;
```
### Selecionando registros na tabela de Pessoas através da procedure
```sql
DO $$
DECLARE
  resultado REFCURSOR;
  pessoa Pessoas%ROWTYPE;
BEGIN
  CALL selecionar_todas_pessoas(resultado);
  
  LOOP
    FETCH resultado INTO pessoa;
    EXIT WHEN NOT FOUND;
    
    -- Utilize os valores dos campos da tabela conforme necessário
    -- Exemplo de exibição do nome de cada pessoa
    RAISE NOTICE 'Nome: % | Objetivo: %', pessoa.nome, pessoa.objetivo;
  END LOOP;
  
  CLOSE resultado;
END;
$$;
```
### selecionando um registro na tabela de Pessoas através da procedure
```sql
DO $$
DECLARE
  pessoa_resultado Pessoas%ROWTYPE;
BEGIN
  CALL obter_pessoa_por_id(2, pessoa_resultado);
  
  -- Exemplo de exibição do nome da pessoa
  RAISE NOTICE 'Nome: %', pessoa_resultado.nome;
END;
$$;
```