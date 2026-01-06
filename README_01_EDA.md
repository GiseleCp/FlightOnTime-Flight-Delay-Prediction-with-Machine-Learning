# 01_EDA_FlighOnTime_v5_(1).ipynb — Análise Exploratória de Dados (EDA)
## Projeto: Flight On-Time Prediction

## 1. Objetivo do Notebook
Este notebook tem como objetivo realizar uma **Análise Exploratória de Dados (EDA)** sobre o dataset de voos,
buscando compreender os fatores que influenciam atrasos e preparar os dados para a etapa de modelagem preditiva.

## 2. Principais Etapas
- Download e leitura dos dados
- Padronização de nomes de colunas
- Tratamento de valores ausentes
- Análise de variáveis categóricas e numéricas
- Geração de estatísticas descritivas
- Visualizações exploratórias (distribuições, correlações e comparações)

## 3. Estrutura do Dataset
- Variáveis temporais (data, horário, dia da semana)
- Variáveis operacionais do voo
- Variáveis categóricas (companhia aérea, aeroporto, etc.)
- Variável alvo relacionada a atraso / pontualidade

## 4. Principais Insights Gerados
- Identificação de padrões de atraso por período
- Impacto de variáveis categóricas no atraso
- Avaliação da qualidade e balanceamento da variável alvo

## 5. Bibliotecas Utilizadas
- Python 3.11.2
- pandas 2.2.3
- numpy 1.24.0
- matplotlib 3.7.5
- seaborn 0.11.2
- gdown n/a
- json (stdlib)
- os (stdlib)
- zipfile (stdlib)

## 6. Saída do Notebook
- Dataset analisado e compreendido
- Base preparada conceitualmente para modelagem
- Diretrizes para engenharia de atributos no 02_Modelo_Preditivo_FlightOnTime_ok3.ipynb
