## CRIAÇÃO AMBIENTE DE DESENVOLVIMENTO POSTGRES COM DOCKER
> Criando a rede no docker para o ambiente do banco
```shell
docker network create --driver bridge postgres-network
```
> Criando o container do postgres conectado a rede
```shell
docker container run --name pgserver --network=postgres-network -e "POSTGRES_PASSWORD=pg123" -p 4001:5432 --memory=200M --cpus=0.2 -d postgres
```
> Criando o container do pgadmin (ferramenta grafica para acesso ao postgres) e o conectando a mesma rede
```shell
docker run --name my-pgadmin --network=postgres-network -p 15432:80 --memory=200M --cpus=0.2 -e "PGADMIN_DEFAULT_EMAIL=bruno@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=pgpwd123" -d dpage/pgadmin4
```

> Analisando o container do banco de dados em busca do seu endereço de IP
```shell
docker container inspect pgserver | grep -i IPaddress
```