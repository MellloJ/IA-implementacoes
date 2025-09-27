import random
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
pesos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Pesos dos itens
valores = [60, 100, 120, 140, 150, 160, 170, 180, 190, 200]  # Valores dos itens
capacidade = 300  # Capacidade da mochila
n_itens = len(pesos)  # Número de itens (10)

# Parâmetros do AG
tamanho_populacao = 100
n_geracoes = 100
taxa_mutacao = 0.01
prob_crossover = 0.8

def fitness(individuo):
    """Calcula o fitness: valor total se peso <= capacidade, senão penalizado."""
    peso_total = sum(pesos[i] for i in range(n_itens) if individuo[i] == 1)
    valor_total = sum(valores[i] for i in range(n_itens) if individuo[i] == 1)
    if peso_total > capacidade:
        return valor_total - (peso_total - capacidade) * 10
    return valor_total

def criar_individuo():
    """Cria um indivíduo aleatório (vetor binário)."""
    return [random.randint(0, 1) for _ in range(n_itens)]

def inicializar_populacao():
    """Inicializa a população."""
    return [criar_individuo() for _ in range(tamanho_populacao)]

def selecao_roleta(populacao):
    """Seleção por roleta: proporcional ao fitness (ajustado para não-negativo)."""
    fitnesses = [fitness(ind) for ind in populacao]
    min_f = min(fitnesses)
    fitnesses_ajustados = [f - min_f for f in fitnesses]
    total_f = sum(fitnesses_ajustados)
    
    if total_f == 0:
        return random.choice(populacao)
    
    r = random.uniform(0, total_f)
    acum = 0
    for i, f in enumerate(fitnesses_ajustados):
        acum += f
        if acum >= r:
            return populacao[i]
    return populacao[-1]

def crossover(pai1, pai2):
    """Crossover de ponto único."""
    ponto = random.randint(1, n_itens - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(individuo):
    """Mutação: inverte bit com probabilidade taxa_mutacao."""
    for i in range(n_itens):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico():
    """Executa o AG principal e rastreia a evolução."""
    populacao = inicializar_populacao()
    melhor_fitness = 0
    melhor_individuo = None
    historico_fitness = []  # Armazena melhor fitness por geração
    
    for geracao in range(n_geracoes):
        # Ordena população por fitness
        populacao_ordenada = sorted(populacao, key=fitness, reverse=True)
        fitness_atual = fitness(populacao_ordenada[0])
        historico_fitness.append(fitness_atual)
        
        # Atualiza melhor solução
        if fitness_atual > melhor_fitness:
            melhor_fitness = fitness_atual
            melhor_individuo = populacao_ordenada[0].copy()
        
        # Imprime progresso (opcional)
        print(f"Geração {geracao + 1}: Melhor fitness = {fitness_atual}")
        
        # Gera nova população
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            pai1 = selecao_roleta(populacao)
            pai2 = selecao_roleta(populacao)
            
            if random.random() < prob_crossover:
                filho1, filho2 = crossover(pai1, pai2)
            else:
                filho1, filho2 = pai1.copy(), pai2.copy()
            
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao[:tamanho_populacao]
    
    # Plota evolução do fitness
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n_geracoes + 1), historico_fitness, label='Melhor Fitness')
    plt.xlabel('Geração')
    plt.ylabel('Fitness (Valor Total)')
    plt.title('Evolução do Melhor Fitness por Geração')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return melhor_individuo, melhor_fitness, historico_fitness

# Execução
melhor_solucao, melhor_valor, historico = algoritmo_genetico()
print("\nResultados Finais:")
print("Melhor solução (itens selecionados):", melhor_solucao)
print("Valor total:", melhor_valor)

# Verificação
peso_selecionado = sum(pesos[i] for i in range(n_itens) if melhor_solucao[i] == 1)
print("Peso total:", peso_selecionado)
print("Viável?", "Sim" if peso_selecionado <= capacidade else "Não")