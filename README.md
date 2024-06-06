# Maze Solver

## Introdução
A solução proposta visa resolver um labirinto representado por uma matriz bidimensional onde cada célula pode ser o inicio ("🟩"), um caminho livre ("🟦"), uma parede ("⬛") ou o ponto de chegada ("🏁"). 

O algoritmo utilizado para encontrar o caminho do ponto inicial até o ponto final é a busca em profundidade (DFS - Depth First Search). Este relatório técnico descreve a lógica de implementação e a sequência de operações do algoritmo.

## Lógica de Implementação
A solução do labirinto é baseada em um algoritmo de busca em profundidade (DFS). O programa utiliza uma pilha para armazenar as coordenadas dos caminhos percorridos. 

A lógica de implementação da função `solveMaze` no `maze.py` é a seguinte:

1. Inicializa uma nova lista de caminho vazia.
2. Cria uma nova matriz com o mesmo tamanho do labirinto com todos os valores `False`.
3. Utiliza a função interna `search` para validar o caminho começando no bloco de inicio.
    1. Verifica se está "Out of Bounds" (fora do labirinto), caso esteja, retorne `Falso`.
    2. Verifica se já está em uma celula visitada, caso esteja, retorne `Falso`.
    3. Verifica se está em uma parede, se estiver, retorne `Falso`.
    4. Após essas verificações, verifique se chegou ao fim do labirinto, se estiver, retorne `Verdadeiro`.
    5. Se não houve um retorno anterior, marque a celula atual como visitada e adicione como parte do caminho de resolução.
    6. Chame essa função de forma recursiva para todos os lados possíveis.
        1. Caso haja um retorno `Verdadeiro` delas, continue.
        2. Caso não haja, retorne `Falso` e remova este caminho da fila.

Dessa forma o resultado final da implementacão trará corretamente o caminho tomado para chegar na resolução final, que não necessáriamente será a menor.

Caso o caminho seja vazio, não existe caminho possível para o final do labirinto.

## Exemplo de Uso
Aqui está um exemplo de como utilizar o `maze.py` para solucionar um labirinto:

```sh
$ python maze.py --size 15
```

Caso tenha dúvidas do comando pode utilizar o auxiliador `--help`

```sh
$ python maze.py --help
```

## Equipe:
- Arthur Oliveira Passos - 1272022772
- Kaled Freire Barreto - 1272023144
