# Algoritmos de Ordena��o e Recurs�o

Este reposit�rio cont�m diversas implementa��es de algoritmos fundamentais de ordena��o, busca, e recurs�o em Python. Estes algoritmos s�o comumente utilizados em diversas �reas da ci�ncia da computa��o, como ordena��o de listas, solu��o de problemas matem�ticos e de busca, e manipula��o eficiente de dados.

## Algoritmos Implementados

### 1. **BubbleSortIterativo**
   - **Descri��o:** Implementa��o iterativa do algoritmo de ordena��o Bubble Sort.
   - **Funcionalidade:** Ordena uma lista de n�meros comparando elementos adjacentes e trocando-os de posi��o se estiverem na ordem errada. O processo � repetido at� que a lista esteja ordenada.
   - **Complexidade:** O(n�).

### 2. **BubbleSortRecursivo**
   - **Descri��o:** Implementa��o recursiva do algoritmo de ordena��o Bubble Sort.
   - **Funcionalidade:** Realiza a mesma ordena��o do Bubble Sort, mas de forma recursiva, chamando a fun��o repetidamente at� que a lista esteja ordenada.
   - **Complexidade:** O(n�).

### 3. **BuscaSequencial**
   - **Descri��o:** Implementa��o de uma busca linear em um array.
   - **Funcionalidade:** Percorre a lista sequencialmente, comparando cada elemento com o valor buscado at� encontr�-lo ou atingir o final da lista.
   - **Complexidade:** O(n).

### 4. **BuscaSequencialRecursiva**
   - **Descri��o:** Implementa��o recursiva da busca sequencial.
   - **Funcionalidade:** Funciona de maneira semelhante � busca sequencial, mas utiliza recurs�o para realizar a busca ao longo da lista.
   - **Complexidade:** O(n).

### 5. **EncontraMajoritario**
   - **Descri��o:** Algoritmo que encontra o elemento majorit�rio de uma lista (se existir).
   - **Funcionalidade:** Verifica se existe um elemento que aparece mais da metade das vezes na lista e retorna esse elemento.
   - **Complexidade:** O(n).

### 6. **GeraGraficos**
   - **Descri��o:** Algoritmo respons�vel por gerar gr�ficos com base em dados.
   - **Funcionalidade:** Utiliza bibliotecas gr�ficas para gerar representa��es visuais de dados, como gr�ficos de barras, linhas, ou dispers�o.

### 7. **MergeSort**
   - **Descri��o:** Implementa��o recursiva do algoritmo Merge Sort.
   - **Funcionalidade:** Divide a lista ao meio repetidamente e, em seguida, mescla as partes de forma ordenada. � eficiente para listas grandes.
   - **Complexidade:** O(n log n).

### 8. **MergeSortIterativo**
   - **Descri��o:** Implementa��o iterativa do algoritmo Merge Sort.
   - **Funcionalidade:** Utiliza uma abordagem de "baixo para cima", come�ando com sublistas pequenas e mesclando-as progressivamente at� que a lista completa esteja ordenada.
   - **Complexidade:** O(n log n).

### 9. **MultiplicacaoRecursiva**
   - **Descri��o:** Implementa��o de multiplica��o recursiva entre dois n�meros.
   - **Funcionalidade:** Multiplica dois n�meros sem utilizar o operador de multiplica��o diretamente, fazendo isso atrav�s de somas repetidas de forma recursiva.
   - **Complexidade:** O(n), onde n � o valor do menor dos dois n�meros.

### 10. **QuickSortIterativo**
   - **Descri��o:** Implementa��o iterativa do algoritmo QuickSort.
   - **Funcionalidade:** Utiliza uma pilha para simular a recurs�o do QuickSort, ordenando a lista de forma eficiente atrav�s de parti��es baseadas em um piv�.
   - **Complexidade:** O(n log n) em m�dia, O(n�) no pior caso.

### 11. **QuickSortRecursivo**
   - **Descri��o:** Implementa��o recursiva do algoritmo QuickSort.
   - **Funcionalidade:** Divide a lista em duas partes com base em um piv� e recursivamente ordena cada uma das sublistas.
   - **Complexidade:** O(n log n) em m�dia, O(n�) no pior caso.

### 12. **SelectionSortIterativo**
   - **Descri��o:** Implementa��o iterativa do algoritmo Selection Sort.
   - **Funcionalidade:** Encontra repetidamente o menor elemento da lista e o coloca na posi��o correta at� que toda a lista esteja ordenada.
   - **Complexidade:** O(n�).

### 13. **SelectionSortRecursivo**
   - **Descri��o:** Implementa��o recursiva do algoritmo Selection Sort.
   - **Funcionalidade:** Realiza a mesma ordena��o do Selection Sort iterativo, mas de forma recursiva.
   - **Complexidade:** O(n�).

### 14. **TorreDeHanoi**
   - **Descri��o:** Solu��o recursiva para o problema das Torres de Han�i.
   - **Funcionalidade:** Resolve o cl�ssico problema das Torres de Han�i, movendo discos entre tr�s torres de acordo com as regras do jogo.
   - **Complexidade:** O(2^n), onde n � o n�mero de discos.

## Como Utilizar

Cada arquivo cont�m a implementa��o de um algoritmo espec�fico. Para executar qualquer um dos algoritmos, basta clonar o reposit�rio e rodar o script Python correspondente.

### Exemplo de Execu��o

1. Clone o reposit�rio:
    ```bash
    git clone https://github.com/seu_usuario/nome_do_repositorio.git
    ```

2. Acesse o diret�rio clonado:
    ```bash
    cd nome_do_repositorio
    ```

3. Execute qualquer arquivo Python. Por exemplo, para rodar o `QuickSortRecursivo`:
    ```bash
    python quickSortRecursivo.py
    ```

## Contribui��es

Contribui��es s�o bem-vindas! Se voc� tem sugest�es de melhorias ou deseja adicionar novos algoritmos, sinta-se � vontade para abrir um pull request.

## Licen�a

Este projeto est� licenciado sob a Licen�a MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
