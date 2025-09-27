# Explicação do Código do Algoritmo Genético para o Problema da Mochila Binária

Este documento explica o código Python que implementa o **algoritmo genético** (AG) para resolver o problema da mochila binária. O código utiliza **seleção por roleta**, rastreia a evolução das gerações e exibe um gráfico para acompanhar os fitness de cada geração. Abaixo, temos os pontos principais do código, incluindo a estrutura, os componentes e como eles funcionam para encontrar uma solução otimizada.

---

## 1. Problema da Mochila Binária

O problema da mochila binária consiste em selecionar um subconjunto de itens, cada um com um **peso** e um **valor**, para **maximizar o valor total** sem exceder a **capacidade** da mochila.

### Parâmetros do Problema
- **Pesos**: Lista `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]` representa o peso de cada item.
- **Valores**: Lista `[60, 100, 120, 140, 150, 160, 170, 180, 190, 200]` representa o valor de cada item.
- **Capacidade**: `300` é o limite de peso da mochila.
- **Número de Itens**: `n_itens = len(pesos) = 10`.

### Codificação
Cada solução (indivíduo) é representada por um **vetor binário** de tamanho `n_itens`. Por exemplo, `[1, 0, 1, 1, 0, 0, 0, 1, 0, 0]` indica que os itens nos índices 0, 2, 3 e 7 estão na mochila (`1`), enquanto os demais não estão (`0`).

---

## 2. Parâmetros do Algoritmo Genético

Os parâmetros controlam o comportamento do AG:
- `tamanho_populacao = 100`: Quantidade de indivíduos na população.
- `n_geracoes = 200`: Número de iterações (gerações).
- `taxa_mutacao = 0.01`: Probabilidade de mutação por bit (1%).
- `prob_crossover = 0.8`: Probabilidade de crossover entre dois pais (80%).

---

## 3. Estrutura do Código

O código é modular, com funções específicas para cada etapa do AG. Abaixo, explico as principais funções e suas responsabilidades.

### 3.1. Função `fitness(individuo)`
- **Objetivo**: Avalia a qualidade de uma solução (indivíduo).
- **Funcionamento**:
  - Calcula o **peso total** e o **valor total** dos itens selecionados (onde `individuo[i] == 1`).
  - Se o peso total exceder a capacidade (`300`), aplica uma **penalidade**: `valor_total - (peso_total - capacidade) * 10`.
  - Exemplo: Para um indivíduo com valor total 500 e peso 320, o fitness é `500 - (320 - 300) * 10 = 300`.
- **Importância**: O fitness determina quais indivíduos têm maior chance de serem selecionados, guiando o AG para soluções melhores.

### 3.2. Função `criar_individuo()`
- **Objetivo**: Gera um indivíduo aleatoriamente.
- **Funcionamento**: Cria um vetor binário de tamanho `n_itens` com valores `0` ou `1` aleatórios (ex.: `[0, 1, 1, 0, ...]`).
- **Uso**: Utilizado para inicializar a população inicial.

### 3.3. Função `inicializar_populacao()`
- **Objetivo**: Cria a população inicial.
- **Funcionamento**: Gera uma lista de `tamanho_populacao` (100) indivíduos usando `criar_individuo()`.

### 3.4. Função `selecao_roleta(populacao)`
- **Objetivo**: Seleciona indivíduos para reprodução com base em seu fitness.
- **Método**: Seleção por roleta, onde a probabilidade de seleção é proporcional ao fitness.
- **Funcionamento**:
  1. Calcula o fitness de todos os indivíduos.
  2. Ajusta os valores de fitness subtraindo o menor fitness (para evitar valores negativos devido à penalidade).
  3. Normaliza os fitness ajustados para criar uma "roleta" (soma total dos fitness).
  4. Gera um número aleatório entre 0 e a soma total, selecionando o indivíduo cuja faixa cumulativa contém esse número.
  5. Se a soma dos fitness for zero (caso raro), escolhe aleatoriamente.
- **Importância**: Favorece indivíduos com maior fitness, mas permite diversidade ao dar chance a indivíduos menos aptos.

### 3.5. Função `crossover(pai1, pai2)`
- **Objetivo**: Combina dois indivíduos (pais) para gerar dois novos (filhos).
- **Método**: Crossover de ponto único.
- **Funcionamento**:
  - Escolhe um ponto de corte aleatório entre 1 e `n_itens - 1`.
  - Troca os genes após esse ponto entre os pais.
  - Exemplo: Para `pai1 = [1, 0, 1, 0]`, `pai2 = [0, 1, 0, 1]`, ponto = 2:
    - `filho1 = [1, 0, 0, 1]`
    - `filho2 = [0, 1, 1, 0]`
- **Probabilidade**: Ocorre se um número aleatório for menor que `prob_crossover` (0.8); caso contrário, os pais são copiados diretamente.

### 3.6. Função `mutacao(individuo)`
- **Objetivo**: Introduz pequenas alterações aleatórias em um indivíduo.
- **Funcionamento**:
  - Para cada bit do indivíduo, inverte o valor (`0` → `1` ou `1` → `0`) com probabilidade `taxa_mutacao` (0.01).
  - Exemplo: `[1, 0, 1, 0]` pode virar `[1, 0, 0, 0]` se o terceiro bit mutar.
- **Importância**: Garante diversidade genética, evitando convergência prematura para soluções ruins.

### 3.7. Função `algoritmo_genetico()`
- **Objetivo**: Executa o AG completo e rastreia a evolução.
- **Funcionamento**:
  1. Inicializa a população com `inicializar_populacao()`.
  2. Para cada geração (1 a `n_geracoes`):
     - Calcula o fitness de todos os indivíduos e armazena o melhor fitness em `historico_fitness`.
     - Atualiza a melhor solução (indivíduo e fitness) se uma melhor for encontrada.
     - Imprime o melhor fitness da geração (ex.: `Geração 1: Melhor fitness = 450`).
     - Gera uma nova população:
       - Seleciona pares de pais com `selecao_roleta`.
       - Aplica `crossover` (com probabilidade 0.8) ou copia os pais.
       - Aplica `mutacao` nos filhos.
       - Adiciona os filhos à nova população.
     - Substitui a população antiga pela nova, mantendo o tamanho fixo (`tamanho_populacao`).
  3. Plota um gráfico com matplotlib:
     - Eixo x: Número da geração (1 a 200).
     - Eixo y: Melhor fitness (valor total, com penalidade se inviável).
  4. Retorna a melhor solução, seu fitness e o histórico de fitness.

---

## 4. Acompanhamento da Evolução

O código inclui funcionalidades para acompanhar a evolução do AG:
- **Histórico de Fitness**: A lista `historico_fitness` armazena o melhor fitness de cada geração.
- **Impressão no Console**: Exibe o melhor fitness de cada geração (ex.: `Geração 1: Melhor fitness = 450`). Pode ser comentado para reduzir a saída.
- **Gráfico de Evolução**:
  - Usa a biblioteca matplotlib para plotar `historico_fitness` em função do número da geração.
  - O gráfico mostra como o fitness melhora ao longo do tempo, indicando convergência (ex.: sobe rápido nas primeiras gerações e estabiliza).

---

## 5. Saída e Verificação

No final, o código exibe:
- **Melhor Solução**: O vetor binário do melhor indivíduo (ex.: `[1, 0, 1, 1, 1, 0, 0, 1, 0, 0]`).
- **Valor Total**: O fitness da melhor solução (ex.: `550`).
- **Peso Total**: Soma dos pesos dos itens selecionados (ex.: `280`).
- **Viabilidade**: Confirma se o peso total é ≤ `capacidade` (ex.: `Viável? Sim`).


### Gráfico
Um gráfico de linha é exibido, com:
- **Eixo x**: Gerações (1 a 200).
- **Eixo y**: Melhor fitness por geração.
- **Visualização**: Mostra a evolução, geralmente com um aumento rápido no início e estabilização.

---

# Video de referencia: https://youtu.be/FYF6lS_BHKA?si=H0njNsJdE-ARJxn-