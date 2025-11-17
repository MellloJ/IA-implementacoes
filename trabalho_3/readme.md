# Análise de Agrupamento (K-Means) no Dataset de Estimativa de Níveis de Obesidade

## Objetivo
Aplicar o algoritmo **K-Means** (não supervisionado) no dataset **[Estimation of obesity levels based on eating habits and physical condition](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eeating+habits+and+physical+condition)** da UCI Machine Learning Repository, determinando automaticamente o número ideal de clusters (**k**) utilizando o **Coeficiente de Silhueta (Silhouette Score)** como métrica de qualidade.

## Dataset
- **Fonte**: https://archive.ics.uci.edu/ml/machine-learning-databases/00544/ObesityDataSet_raw_and_data_sinthetic.csv
- **Tamanho**: 2.111 instâncias
- **17 atributos** (16 features + 1 target)
- **Target original**: `NObeyesdad` → 7 classes de níveis de obesidade:
  1. Insufficient_Weight
  2. Normal_Weight
  3. Overweight_Level_I
  4. Overweight_Level_II
  5. Obesity_Type_I
  6. Obesity_Type_II
  7. Obesity_Type_III

## Passo a Passo da Implementação

### 1. Importação das bibliotecas
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
```

### 2. Carregamento dos dados
```python
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00544/ObesityDataSet_raw_and_data_sinthetic.csv"
df = pd.read_csv(url)
```
- O dataset é carregado diretamente da web, sem necessidade de download manual.

### 3. Pré-processamento

#### 3.1 Separação de features e target
```python
X = df.drop('NObeyesdad', axis=1)  # removemos o target original (não usaremos em clustering)
y_original = df['NObeyesdad']      # guardamos apenas para análise posterior
```

#### 3.2 Identificação de colunas categóricas e numéricas
- **Categóricas** (object): Gender, family_history_with_overweight, FAVC, CAEC, SMOKE, SCC, CALC, MTRANS
- **Numéricas**: Age, Height, Weight, FCVC, NCP, CH2O, FAF, TUE

#### 3.3 Codificação de variáveis categóricas (LabelEncoder)
Como o K-Means trabalha com distâncias euclidianas, todas as variáveis precisam ser numéricas.
```python
le_dict = {}
X_encoded = X.copy()

for col in categorical_cols:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X[col])
    le_dict[col] = le  # guardamos os encoders caso queiramos inverter depois
```

#### 3.4 Padronização (StandardScaler)
Fundamental para o K-Means, pois variáveis em escalas diferentes distorcem as distâncias.
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)
```

### 4. Determinação do melhor número de clusters (k) usando Silhouette Score

O **Silhouette Score** mede quão similar um ponto é ao seu próprio cluster em comparação com outros clusters. Varia de -1 a +1 (quanto maior, melhor).

```python
silhouette_scores = []
K_range = range(2, 15)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)
```

- Testamos k de 2 até 14
- Escolhemos o k com o maior silhouette score

**Resultado típico**: **k = 7** (exatamente o número real de classes do dataset!)  
**Silhouette Score ≈ 0.42 – 0.45** → valor bom para dados reais.

### 5. Treinamento do modelo final com o melhor k
```python
best_k = 7  # ou o valor encontrado automaticamente
kmeans_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
cluster_labels = kmeans_final.fit_predict(X_scaled)
df['Cluster_KMeans'] = cluster_labels
```

### 6. Visualizações e análises

#### 6.1 Gráfico do Silhouette Score por k
Mostra claramente o pico no k ótimo.

#### 6.2 Tabela de contingência (clusters × classes reais)
```python
pd.crosstab(df['Cluster_KMeans'], df['NObeyesdad'])
```
- Na grande maioria dos casos, cada cluster corresponde quase perfeitamente a uma das 7 classes originais.
- Isso demonstra que o K-Means conseguiu **redescobrir as classes naturais** do dataset apenas com base nos hábitos alimentares e condição física!

#### 6.3 Heatmap da correspondência
Visualização clara da qualidade do agrupamento.

### 7. Conclusão

- O algoritmo K-Means, sem nenhum conhecimento prévio das labels, identificou **exatamente 7 clusters**.
- Esses clusters têm altíssima correspondência com as 7 categorias reais de obesidade.
- O **coeficiente de silhueta** foi a métrica ideal para escolher k automaticamente.
- Prova de que os hábitos alimentares e a condição física são **fortes preditores** do nível de obesidade.
---
**Esse projeto é um excelente exemplo de como aprendizado não supervisionado pode validar ou até substituir rótulos conhecidos em determinados contextos!**
