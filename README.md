# aa-project03

## Most Frequent Letters

Este trabalho procura mostrar através de diferentes abordagens algorítmicas como contar o número de vezes
que uma determinada letra aparece numa determinada obra litetária. Todos os algoritmos forame scritos em Python (3.10),
e serão feitas analíses sobre a complexidade computacional, os erros relativos e absolutos das contagens entre outros tipos
de comparação entre os algoritmos.

## Código

O código do projeto pode ser consultado na direrório [src](./src). 
Foram criados as seguintes classes, para fazer a geração de dados:
- [Vertex](./src/vertex.py) 
- [Point](./src/vertex.py) 

A resolução do problema a partir dos 2 algoritmos distintos é feita no ficheiro [generator.py](./src/generator.py)

## Como correr

Instalar um virtual enviroment no diretório [src](./src):

```bash
python3 -m venv venv
```

Instalar as dependências:
```bash
pip install -r requirements
```

Para correr o pre-processamento das obras literárias:
```bash
python3 process_data.py
```

Para fazer a contagem das letras nas obras literárias:

```bash
python3 main.py
```

## Resultados

A tabelas dos resultados pode ser consultada no diretório [results](./results)

## Relatório

O projeto é acompanahdo por um relatório e o memso pode ser consultado no diretório [report](./report/relatorio.pdf)

