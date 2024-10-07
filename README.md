# Algoritmos de Ordenação e Recursão

Este repositório contém diversas implementações de algoritmos fundamentais de ordenação, busca, e recursão em Python. Estes algoritmos são comumente utilizados em diversas áreas da ciência da computação, como ordenação de listas, solução de problemas matemáticos e de busca, e manipulação eficiente de dados.

## Algoritmos Implementados

### 1. **BubbleSortIterativo**
   - **Descrição:** Implementação iterativa do algoritmo de ordenação Bubble Sort.
   - **Funcionalidade:** Ordena uma lista de números comparando elementos adjacentes e trocando-os de posição se estiverem na ordem errada. O processo é repetido até que a lista esteja ordenada.
   - **Complexidade:** O(n²).

### 2. **BubbleSortRecursivo**
   - **Descrição:** Implementação recursiva do algoritmo de ordenação Bubble Sort.
   - **Funcionalidade:** Realiza a mesma ordenação do Bubble Sort, mas de forma recursiva, chamando a função repetidamente até que a lista esteja ordenada.
   - **Complexidade:** O(n²).

### 3. **BuscaSequencial**
   - **Descrição:** Implementação de uma busca linear em um array.
   - **Funcionalidade:** Percorre a lista sequencialmente, comparando cada elemento com o valor buscado até encontrá-lo ou atingir o final da lista.
   - **Complexidade:** O(n).

### 4. **BuscaSequencialRecursiva**
   - **Descrição:** Implementação recursiva da busca sequencial.
   - **Funcionalidade:** Funciona de maneira semelhante à busca sequencial, mas utiliza recursão para realizar a busca ao longo da lista.
   - **Complexidade:** O(n).

### 5. **EncontraMajoritario**
   - **Descrição:** Algoritmo que encontra o elemento majoritário de uma lista (se existir).
   - **Funcionalidade:** Verifica se existe um elemento que aparece mais da metade das vezes na lista e retorna esse elemento.
   - **Complexidade:** O(n).

### 6. **GeraGraficos**
   - **Descrição:** Algoritmo responsável por gerar gráficos com base em dados.
   - **Funcionalidade:** Utiliza bibliotecas gráficas para gerar representações visuais de dados, como gráficos de barras, linhas, ou dispersão.

### 7. **MergeSort**
   - **Descrição:** Implementação recursiva do algoritmo Merge Sort.
   - **Funcionalidade:** Divide a lista ao meio repetidamente e, em seguida, mescla as partes de forma ordenada. É eficiente para listas grandes.
   - **Complexidade:** O(n log n).

### 8. **MergeSortIterativo**
   - **Descrição:** Implementação iterativa do algoritmo Merge Sort.
   - **Funcionalidade:** Utiliza uma abordagem de "baixo para cima", começando com sublistas pequenas e mesclando-as progressivamente até que a lista completa esteja ordenada.
   - **Complexidade:** O(n log n).

### 9. **MultiplicacaoRecursiva**
   - **Descrição:** Implementação de multiplicação recursiva entre dois números.
   - **Funcionalidade:** Multiplica dois números sem utilizar o operador de multiplicação diretamente, fazendo isso através de somas repetidas de forma recursiva.
   - **Complexidade:** O(n), onde n é o valor do menor dos dois números.

### 10. **QuickSortIterativo**
   - **Descrição:** Implementação iterativa do algoritmo QuickSort.
   - **Funcionalidade:** Utiliza uma pilha para simular a recursão do QuickSort, ordenando a lista de forma eficiente através de partições baseadas em um pivô.
   - **Complexidade:** O(n log n) em média, O(n²) no pior caso.

### 11. **QuickSortRecursivo**
   - **Descrição:** Implementação recursiva do algoritmo QuickSort.
   - **Funcionalidade:** Divide a lista em duas partes com base em um pivô e recursivamente ordena cada uma das sublistas.
   - **Complexidade:** O(n log n) em média, O(n²) no pior caso.

### 12. **SelectionSortIterativo**
   - **Descrição:** Implementação iterativa do algoritmo Selection Sort.
   - **Funcionalidade:** Encontra repetidamente o menor elemento da lista e o coloca na posição correta até que toda a lista esteja ordenada.
   - **Complexidade:** O(n²).

### 13. **SelectionSortRecursivo**
   - **Descrição:** Implementação recursiva do algoritmo Selection Sort.
   - **Funcionalidade:** Realiza a mesma ordenação do Selection Sort iterativo, mas de forma recursiva.
   - **Complexidade:** O(n²).

### 14. **TorreDeHanoi**
   - **Descrição:** Solução recursiva para o problema das Torres de Hanói.
   - **Funcionalidade:** Resolve o clássico problema das Torres de Hanói, movendo discos entre três torres de acordo com as regras do jogo.
   - **Complexidade:** O(2^n), onde n é o número de discos.

## Como Utilizar

Cada arquivo contém a implementação de um algoritmo específico. Para executar qualquer um dos algoritmos, basta clonar o repositório e rodar o script Python correspondente.

### Exemplo de Execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/nome_do_repositorio.git
    ```

2. Acesse o diretório clonado:
    ```bash
    cd nome_do_repositorio
    ```

3. Execute qualquer arquivo Python. Por exemplo, para rodar o `QuickSortRecursivo`:
    ```bash
    python quickSortRecursivo.py
    ```

## Contribuições

Contribuições são bem-vindas! Se você tem sugestões de melhorias ou deseja adicionar novos algoritmos, sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
