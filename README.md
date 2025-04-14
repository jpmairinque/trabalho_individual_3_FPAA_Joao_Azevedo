# Trabalho Individual 2 - Caminho Hamiltoniano - João Pedro Mairinque

## Algoritmo para Grafos 

Um caminho hamiltoniano é um percurso em um grafo G que visita todos os seus vértices exatamente uma vez, sem repetir nenhum. Se esse percurso formar um ciclo, ele é chamado de ciclo hamiltoniano (ou circuito hamiltoniano) em G. Um grafo que contém tal ciclo é conhecido como **grafo hamiltoniano**.

Neste trabalho, analiso a aplicação de um algoritmo em python para encontrar um caminho hamiltoniano em um grafo. A execução está contida no arquivo *main.py* e o grafo deve ser representado com a matriz na entrada do algoritmo, tal como: 

  ```python
  graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
  ```


## Classificação (P, NP, NP-Completo, NP-Difícil):

O Problema do Caminho Hamiltoniano é **NP-completo** para grafos dirigidos e não dirigidos. Isso significa que:

- A verificação de uma solução (um caminho que visita todos os vértices exatamente uma vez) pode ser feita em tempo polinomial (classe NP).

- Não existe algoritmo conhecido que resolva o problema em tempo polinomial para todos os casos (por isso não está em P).

- O problema está relacionado ao Problema do Caixeiro Viajante (TSP), que é NP-difícil. O TSP é uma generalização do problema do caminho Hamiltoniano com otimização de custo.

## Complexidade Temporal

- Complexidade do Algoritmo:

O algoritmo utiliza backtracking.

Complexidade: O(n!), onde n é o número de vértices. A cada vértice, tenta-se visitar todos os outros vértices ainda não visitados. O número de permutações de vértices é (n-1)!, com verificações adicionais.

- Método de Determinação:

A complexidade foi determinada por contagem de operações recursivas e análise combinatória dos caminhos possíveis.

## Aplicação do Teorema Mestre

O Teorema Mestre é aplicável a algoritmos recursivos que dividem o problema em subproblemas de tamanho menor, como em algoritmos de divisão e conquista. No backtracking do problema Hamiltoniano, não há subproblemas independentes do mesmo tamanho, e sim uma árvore de decisão com ramificações, o que invalida os critérios do Teorema Mestre.

## Análise dos Casos de Complexidade

- Melhor caso: Encontrar uma solução logo no início da árvore de recursão. Complexidade muito menor que O(n!).

- Pior caso: Percorrer todos os caminhos possíveis sem encontrar solução — ou encontrar apenas no último.

- Caso médio: Depende fortemente da estrutura do grafo; em geral, tende para o pior caso em grafos densos.

Em grafos grandes, o crescimento fatorial torna o algoritmo inviável em tempo hábil. Dessa forma, algoritmos exatos são úteis apenas para pequenos grafos ou em aplicações com restrições específicas.


## Execução


### Executando o projeto


Acesse a raiz do projeto no terminal e execute:

```bash
python3 main.py
```

### Caso não possua o python

### MacOS

Instale o python 3 com Homebrew

```bash
brew install python
```

### Windows

1. Baixe o instalador do Python no site oficial:  
   [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Durante a instalação, marque a opção **"Add Python to PATH"**.
3. Após a instalação, abra um novo terminal e confirme a instalação com:

```bash
python --version
```

## Documentação e links úteis

- [Caminho Hamiltoniano - Wikipedia](https://pt.wikipedia.org/wiki/Caminho_hamiltoniano)

## Licença

Este projeto está licenciado sob a Licença MIT. e execute:
