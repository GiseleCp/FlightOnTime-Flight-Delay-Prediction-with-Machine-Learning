✈️ FlightOnTime — Previsão de Atrasos de Voos
Status: Concluído ✅

📋 Sobre o Projeto
O FlightOnTime é uma solução de Machine Learning desenvolvida para prever a probabilidade de atrasos em voos comerciais. O objetivo é permitir que companhias aéreas e passageiros antecipem interrupções, otimizando a logística operacional e melhorando a experiência do cliente.

O modelo final foi calibrado não apenas para acurácia, mas para maximizar a detecção de atrasos reais (foco no Recall), ajustando o limiar de decisão (threshold) para 0.4.

💼 Contexto de Negócio
Atrasos de voos geram prejuízos financeiros significativos e danos à reputação das companhias. O desafio consistia em:

Analisar dados históricos de voos (voos_model.json).

Identificar padrões que precedem um atraso.

Entregar um modelo preditivo capaz de generalizar bem para novos dados.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Análise de Dados: Pandas, NumPy

Visualização: Matplotlib, Seaborn

Machine Learning: Scikit-Learn (Random Forest)

Serialização: Joblib

🚀 Metodologia
O projeto seguiu as seguintes etapas:

Coleta e Limpeza: Tratamento de valores nulos, conversão de tipos e engenharia de atributos (feature engineering).

Análise Exploratória (EDA): Identificação de correlações entre variáveis (ex: horário de partida, dia da semana) e o atraso.

Modelagem: Teste comparativo entre diversos algoritmos.

Modelo Vencedor: Random Forest Classifier.

Otimização de Hiperparâmetros: Ajuste fino para evitar overfitting.

Calibragem de Threshold:

Por padrão, modelos classificam com base em probabilidade > 0.5.

Após análise da curva Precision-Recall, definiu-se um threshold de 0.4.

Motivo: É mais custoso para o negócio deixar de prever um atraso (Falso Negativo) do que prever um atraso que não ocorre (Falso Positivo). O threshold de 0.4 aumentou a sensibilidade do modelo.

📊 Resultados
O modelo final (modelo_random_forest_atraso_voos.pkl) apresentou a melhor performance geral, equilibrando precisão e recall após o ajuste do ponto de corte.

Algoritmo: Random Forest

Threshold Definido: 0.4 (40%)

📦 Como Executar o Projeto
Pré-requisitos
Certifique-se de ter o Python instalado e as bibliotecas necessárias:

Bash

pip install pandas numpy scikit-learn joblib matplotlib seaborn
Utilizando o Modelo Exportado
O modelo foi exportado com uma classe personalizada (ou requer ajuste manual) para respeitar o threshold de 0.4. Exemplo de uso:

Python

import joblib
import pandas as pd

# 1. Carregar o modelo
modelo = joblib.load('modelo_random_forest_atraso_voos.pkl')

# 2. Dados de exemplo (mesma estrutura do treinamento)
novos_dados = pd.DataFrame({
    'dia_semana': [1],
    'mes': [12],
    'hora_partida_prevista': [14]
    # ... outras colunas necessárias
})

# 3. Predição considerando o threshold de 0.4
# Se a classe wrapper foi usada na exportação:
predicao = modelo.predict(novos_dados)

# Se for aplicar manualmente:
# probs = modelo.predict_proba(novos_dados)[:, 1]
# predicao = (probs >= 0.4).astype(int)

print("Previsão (1 = Atraso, 0 = No Horário):", predicao)
📂 Estrutura de Arquivos
FlightOnTime/
│
├── 01_Analise_Exploratoria.ipynb    # Análise inicial dos dados
├── 02_Modelo_Preditivo.ipynb        # Treinamento e validação do modelo
├── modelo_random_forest.pkl         # Arquivo binário do modelo treinado
├── voos_model.json                  # Dataset original
└── README.md                        # Documentação do projeto
