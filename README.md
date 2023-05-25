# desafio-gentil
Esse repositório representa o projeto de desafio para a empresa gentil negócios, o projeto consiste na :
- construção de um banco de dados com uma tabela, Pessoa, com a adição de atributos pós criação do banco bem como a utilização de Procedures para acesso de leitura e escrita às informações desse banco.
- Desenvolvimento de uma REST API que acessa esse banco e utiliza das suas procedures para fazer a persistência dos dados.

Nesse repositório, estão tanto o código da API como os scripts de criação do banco, com suas procedures e suas alterações necessárias para correto funcionamento.

O código do projeto se encontra na pasta gentil-api e os scripts do banco nos arquivos [Arquivo SQLServer](init%20db%20sqlserver.md) e [Arquivo Postgres](init%20db%20postgres.md), o banco de dados, bem como a criação de procedures, foi implementado tanto em sqlserver como em postgres, pequenas diferenças de sintaxe são notadas entre os bancos, principalmente em relação as procedures.