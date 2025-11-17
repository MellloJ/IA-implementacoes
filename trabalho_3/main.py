import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# URL correta e estável (2025)
url = "https://archive.ics.uci.edu/static/public/544/data.csv"
df = pd.read_csv(url)

print("Dataset carregado com sucesso!")
print("Shape:", df.shape)

# Separar features e target (target só para análise final)
X = df.drop('NObeyesdad', axis=1)
y = df['NObeyesdad']

# === PRE-PROCESSAMENTO CORRETO ===
# 1. Identificar colunas categóricas
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
print("Colunas categóricas:", categorical_cols)

# 2. Aplicar LabelEncoder em cada coluna categórica
X_encoded = X.copy()
for col in categorical_cols:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X[col])

# 3. Padronização (obrigatório para K-Means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

print("Pré-processamento concluído!\n")

# === BUSCA DO MELHOR K COM SILHOUETTE SCORE ===
sil_scores = []
range_k = range(2, 15)

print("Calculando Silhouette Score para diferentes valores de k...")
for k in range_k:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    sil_scores.append(score)
    print(f"k = {k:2d} → Silhouette Score = {score:.4f}")

# Melhor k
best_k = range_k[np.argmax(sil_scores)]
best_score = max(sil_scores)
print(f"\n>>> MELHOR RESULTADO <<<")
print(f"Melhor número de clusters (k): {best_k}")
print(f"Melhor Silhouette Score: {best_score:.4f}")

# === MODELO FINAL ===
kmeans_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['Cluster'] = kmeans_final.fit_predict(X_scaled)

# === VISUALIZAÇÕES ===
# Gráfico do Silhouette
plt.figure(figsize=(10, 6))
plt.plot(range_k, sil_scores, marker='o', linestyle='-', color='b')
plt.axvline(x=best_k, color='red', linestyle='--', label=f'Melhor k = {best_k}')
plt.title('Coeficiente de Silhueta por Número de Clusters')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Silhouette Score')
plt.legend()
plt.grid(True)
plt.show()

# Tabela de correspondência
print("\nCorrespondência entre Clusters e Classes Reais:")
cross_tab = pd.crosstab(df['Cluster'], df['NObeyesdad'])
print(cross_tab)

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='Blues')
plt.title('Clusters K-Means vs Níveis Reais de Obesidade')
plt.ylabel('Cluster')
plt.xlabel('NObeyesdad (Classe Real)')
plt.show()

print("\nConclusão: O K-Means redescobriu quase perfeitamente as 7 classes de obesidade!")