A solução envolve a análise da relação de toxicidade entre as plantas e o cálculo do tempo até a morte de cada planta. O algoritmo implementado utiliza uma abordagem de programação dinâmica para determinar o número máximo de dias para que todas as plantas parem de morrer.

## Etapas do Algoritmo

1. **Inicialização:**
   - **`vet`**: Vetor que armazena o número de dias até que uma planta morra, inicializado com `float('inf')`.
   - **`ind`**: Vetor que guarda o índice da planta que causou a morte da planta atual, inicializado com `-1`.
   - **`dias`**: Variável para armazenar o número máximo de dias até que todas as plantas parem de morrer.

2. **Iteração sobre as Plantas:**
   - Percorre cada planta a partir da segunda (`i = 1`).
   - Para cada planta, verifica as plantas anteriores para determinar se a planta atual morrerá devido à toxicidade.

3. **Verificação de Toxicidade:**
   - **Caso 1:** Se a planta anterior tem toxicidade maior ou igual à planta atual e já morreu, continua para a próxima planta anterior.
   - **Caso 2:** Se a planta anterior tem menor toxicidade, calcula o número de dias até a morte da planta atual com base no número de dias da planta anterior e atualiza o vetor `vet` e `ind`.

4. **Atualização do Resultado:**
   - Atualiza o valor máximo de dias (`dias`) com base no número de dias calculado para cada planta.

5. **Retorno do Resultado:**
   - O número máximo de dias necessários para que todas as plantas parem de morrer é retornado.
