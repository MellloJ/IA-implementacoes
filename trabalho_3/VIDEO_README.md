# Guia de Gravação de Vídeo — K‑Means no Dataset de Obesidade

Este arquivo reúne o roteiro palavra-a-palavra (teleprompter), a shot list com tempos estimados e instruções práticas para rodar o demo presente em `trabalho_3/main.py`.

---

**Objetivo do vídeo**
- Mostrar a implementação de K‑Means aplicada ao dataset *Estimation of obesity levels* (UCI) e demonstrar como o coeficiente de Silhouette é usado para escolher o número ótimo de clusters.

**Duração alvo:** máximo 5 minutos.

---

## Começando (Quick Start)

Recomenda-se usar um ambiente virtual e instalar as dependências listadas em `trabalho_3/requirements.txt`.

Comandos sugeridos:

```bash
python -m venv venv
source venv/bin/activate
pip install -r trabalho_3/requirements.txt
python trabalho_3/main.py
```

O script irá imprimir mensagens de progresso, os silhouette scores por k, o melhor k encontrado e a tabela de contingência (`crosstab`). Além disso, gera dois gráficos: o gráfico de silhouette por k e o heatmap da correspondência clusters × classes reais.

---

## Teleprompter (texto palavra-a-palavra)

0:00 – 0:10 — Abertura

"Olá — eu sou [seu nome]. Neste vídeo vou mostrar uma implementação de K‑Means para o dataset de estimativa de níveis de obesidade."

[Mostrar slide/título com `K‑Means — Obesity dataset` e link para o repositório]

0:10 – 0:25 — Objetivo

"O objetivo é aplicar K‑Means para identificar agrupamentos naturais nos dados e usar o coeficiente de silhueta para escolher automaticamente o número ideal de clusters."

[Mostrar `readme.md` objetivo ou bullets rápidos]

0:25 – 0:45 — Dataset

"O dataset vem da UCI — 'Estimation of obesity levels'. São 2.111 instâncias e 17 atributos. A variável alvo original é `NObeyesdad`, com 7 classes de obesidade."

[Mostrar a URL do dataset e o trecho no `main.py` com `pd.read_csv(...)`]

0:45 – 1:10 — Visão geral do código

"O código principal está em `trabalho_3/main.py`. Uso pandas para manipular dados, scikit‑learn para K‑Means e métricas, e seaborn/matplotlib para visualizações. Vamos abrir o arquivo e ver os principais blocos."

[Abrir `main.py`, destacar imports e `X = df.drop('NObeyesdad', axis=1)` / `y = df['NObeyesdad']`]

1:10 – 1:40 — Pré‑processamento

"Antes do K‑Means, identificamos colunas categóricas e aplicamos `LabelEncoder` para transformá‑las em números. Em seguida padronizamos tudo com `StandardScaler`, porque K‑Means usa distância euclidiana."

[Mostrar o loop `for col in categorical_cols: le = LabelEncoder() ...` e `X_scaled = scaler.fit_transform(...)`]

1:40 – 2:10 — Seleção de k com Silhouette

"Para escolher o número de clusters, testamos k de 2 a 14 e calculamos o Silhouette Score. O k ótimo é o que maximiza esse score — valores próximos a 1 indicam clusters bem definidos."

[Mostrar o trecho do loop que calcula `silhouette_score` e, em seguida, o gráfico `Silhouette Score por Número de Clusters`]

2:10 – 2:40 — Resultado principal

"No meu teste, o script imprime o melhor k que foi encontrado e o silhouette correspondente. Em muitos casos observamos k = 7, que coincide com as 7 classes reais do dataset."

[Mostrar a saída do terminal com `Melhor número de clusters (k):` e o `cross_tab = pd.crosstab(...)`]

2:40 – 3:10 — Visualização de correspondência

"Construí um heatmap que mostra a correspondência entre os clusters do K‑Means e as classes reais `NObeyesdad`. Ele facilita ver se cada cluster corresponde a uma classe."

[Mostrar o heatmap (`sns.heatmap`) e comentar rapidamente onde há um mapeamento claro]

3:10 – 3:40 — Demo rápido: rodando o script

"Agora vou rodar o script para mostrar a execução ao vivo. No terminal eu uso: `python trabalho_3/main.py`. O script carrega os dados, faz o pré‑processamento, calcula os silhouette scores, e imprime o melhor k e a tabela de contingência."

[Gravar o terminal executando `python trabalho_3/main.py`. Mostrar as mensagens: carregamento, pré‑processamento concluído, lista de scores, melhor k, e a tabela `crosstab`. Pause nos gráficos por 2–4 segundos.]

3:40 – 4:10 — Pontos chave do código

"Os blocos essenciais são: leitura do CSV, codificação das categorias, padronização, loop de seleção de k com silhouette, e o treinamento final do `KMeans` com o melhor k. Esses passos são suficientes para reproduzir os resultados."

[No `main.py`, destacar cada bloco rapidamente enquanto lista cada passo em 1–2 frases.]

4:10 – 4:40 — Conclusão

"Conclusão: mesmo sem rótulos, o K‑Means pode redescobrir as classes naturais quando os atributos são informativos. A métrica de Silhouette é útil para escolher k automaticamente. Isso mostra que hábitos e condição física realmente informam níveis de obesidade."

[Mostrar `readme.md` seção conclusão e resultados numéricos principais, ex.: `k = 7; silhouette ≈ 0.42` se aplicável]

4:40 – 5:00 — Encerramento

"Obrigado por assistir. O código e instruções estão no repositório. Se quiserem, posso deixar um passo a passo para executar localmente ou uma versão em inglês do roteiro. Comentem abaixo o que gostariam de ver em seguida!"

[Mostrar link do repositório, `trabalho_3/readme.md` e créditos]

---

## Shot list e tempos (para edição)

- 0:00–0:10 — Abertura: slide/título (take 1)
- 0:10–0:25 — Objetivo: bullets (take 2)
- 0:25–0:45 — Dataset: mostrar URL e `main.py` (take 3)
- 0:45–1:10 — Visão código: destacar imports e separação X/y (take 4)
- 1:10–1:40 — Pré‑processamento: mostrar loop de encoders e scaler (take 5)
- 1:40–2:10 — Seleção de k: mostrar loop de silhouette e gráfico (take 6)
- 2:10–2:40 — Resultado: terminal com melhor k e crosstab (take 7)
- 2:40–3:10 — Visualização: heatmap (take 8)
- 3:10–3:40 — Demo: gravação do terminal rodando `main.py` (take 9)
- 3:40–4:10 — Walkthrough: zoom nos blocos do código (take 10)
- 4:10–4:40 — Conclusão: readme + resultados (take 11)
- 4:40–5:00 — Encerramento: call to action e créditos (take 12)

Cada take pode ter 1–3 cortes internos; mantenha cada seção concisa e grave duas tomadas quando possível para segurança.

---

## Instruções detalhadas para o demo (o que mostrar/esperar)

- Passo 1: instalar dependências (se necessário): `pip install -r trabalho_3/requirements.txt`.
- Passo 2: executar: `python trabalho_3/main.py`.
- Saída esperada:
  - Mensagem: `Dataset carregado com sucesso!`
  - Mensagem: `Pré-processamento concluído!`
  - Lista de `Silhouette Score` por valores de `k` (2–14).
  - Impressão: `Melhor número de clusters (k): <valor>` e `Melhor Silhouette Score: <valor>`.
  - Impressão da tabela de contingência (`crosstab`) mostrando correspondência entre `Cluster` e `NObeyesdad`.
  - Dois gráficos abrem: (1) gráfico de Silhouette vs k, (2) heatmap clusters × classes.

Dica: maximize a janela do gráfico e pause a gravação quando o gráfico estiver visível por 2–4 s para que o espectador leia os valores.

---

## Dicas rápidas de gravação e edição

- Use fonte grande ao mostrar código (ex.: 16–20 pt) e destaque no máximo 10 linhas por tomada.
- Grave áudio em ambiente silencioso; fale de forma pausada e natural.
- Faça cortes curtos entre seções e adicione legendas com os comandos mostrados.
- Inclua um slide final com link para o repositório e comando rápido de execução.

---

## Checklist antes de subir o vídeo

- [ ] Código funcionando localmente (rodar `python trabalho_3/main.py`).
- [ ] Dependências instaladas em `venv` e testadas.
- [ ] Capturas dos gráficos salvas se preferir inserir imagens estáticas na edição.
- [ ] Teleprompter testado com ritmo natural (fazer uma gravação teste).

---

## Créditos

Projeto e código: repositório `IA-implementacoes` — pasta `trabalho_3`.

Dataset: UCI Machine Learning Repository — "Estimation of obesity levels based on eating habits and physical condition".
