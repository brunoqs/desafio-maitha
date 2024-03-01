# desafio-maitha

## Tecnologias

- Python 3.10+
- FastApi
- SQLAlchemy
- Postgres
- Docker

## Execução

Utilize o arquivo .env.sample para criar o .env
```shell
cp .env.sample .env
```

Rodando a aplicação completa no docker:
```shell
docker compose up
open http://localhost:8000/docs
```

Rodando Fastapi local e postgres no docker:
```shell
docker compose up postgres
make run
open http://localhost:8000/docs
```

Rodando formatador, linst e tests antes de commitar
```shell
make before-commit
```

## Testes

```shell
docker compose up postgres
make test
```