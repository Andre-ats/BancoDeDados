# Projeto Banco de Dados

![Diagrama Relacional](https://github.com/Andre-ats/BancoDeDados/blob/df8fd47dd0167cb60f2bdf60ac1cedd36379bbb0/diagrama_relacional.drawio.png)

## Geração de arquivo .sql
O arquivo `file_generator.py` é utlizado para gerar um arquivo `sql` de inserção de fictícios dados no banco.

### Instalção de dependências
O script utiliza uma biblioteca externa para geração de dados ficticios 

`pip install Faker`

### Execeucção do script
Dentro da pasta onde o script está localizado, você deve rodar o mesmo utilizando a seguinte linha de comando:

`python ./file_generator.py`

ou

`python3 ./file_generator.py`

Na mesma pasta onde o código executado se encontra, será criado um arquivo chamado `seeder.sql` que sera utilizado para inserir os dados nas tabelas. Neste repositorio há um arquivo de mesmo nome, que é um exemplo de como deve ficar.

## Integrantes do Grupo

| Nome  | RA |
| ------------- | ------------- |
| André Alves Toledo Silva  | 22.122.020-5  |
| Thiago Monteiro Tinonin  | 22.122.044-5  |
