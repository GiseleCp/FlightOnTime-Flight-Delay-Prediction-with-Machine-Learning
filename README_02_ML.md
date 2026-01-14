# ✈️ FlightOnTime — Previsão de Atrasos de Voos  
**Status:** Concluído ✅  

## 📋 Visão Geral do Projeto
O **FlightOnTime** é um projeto de *Machine Learning* desenvolvido para prever se um voo comercial irá decolar **no horário ou com atraso**, a partir de dados históricos operacionais.  
A solução tem como foco apoiar **decisões operacionais**, **gestão de riscos** e **melhoria da experiência do passageiro**, antecipando potenciais interrupções.

O modelo final foi ajustado estrategicamente para **maximizar a detecção de atrasos reais**, priorizando *Recall* em detrimento de pequenas perdas de precisão, o que está alinhado ao contexto de negócio.

---

## 🎯 Objetivo de Negócio
Atrasos aéreos geram:
- Custos operacionais adicionais  
- Efeitos em cascata na malha aérea  
- Insatisfação e perda de confiança dos clientes  

Diante disso, o desafio do projeto foi:
- Analisar dados históricos de voos (`voos_model.json`)
- Identificar padrões preditivos de atraso
- Desenvolver um modelo robusto, interpretável e generalizável

---

## 🧠 Abordagem Analítica

### 🔍 Análise Exploratória de Dados (EDA)
Durante o EDA, foram analisados:
- Distribuição de atrasos
- Relação entre **horário de partida**, **dia da semana**, **companhia aérea** e atrasos
- Correlações entre variáveis numéricas
- Balanceamento da variável alvo

Principais insights:
- Voos em determinados horários e dias apresentam maior propensão a atraso  
- O problema possui viés de classe, exigindo métricas além da acurácia  

---

## 🤖 Modelos de Machine Learning Testados
Foram avaliados diferentes algoritmos de classificação, com comparação baseada em *Recall*, *Precision*, *F1-Score* e *Curva Precision-Recall*:

- Regressão Logística  
- Decision Tree Classifier  
- Random Forest Classifier  

### 🏆 Modelo Selecionado
**Random Forest Classifier**  
Escolhido por apresentar:
- Melhor equilíbrio entre *Recall* e *Precision*
- Maior robustez a ruído
- Boa capacidade de capturar relações não lineares

---

## ⚙️ Ajuste de Threshold (Ponto de Corte)
Por padrão, classificadores utilizam **0.5** como limiar de decisão.  
Neste projeto, foi realizada uma análise estratégica da **Curva Precision-Recall**, levando à definição de:

- **Threshold final:** `0.4`

### 📌 Justificativa:
- O custo de um **Falso Negativo** (não prever um atraso real) é maior do que um **Falso Positivo**
- A redução do threshold aumentou a sensibilidade do modelo
- Resultado: maior capacidade de antecipar atrasos relevantes

---

## 📊 Resultados
O modelo final apresentou melhor desempenho geral após o ajuste do threshold:

- **Algoritmo:** Random Forest  
- **Threshold:** 0.4 (40%)  
- **Modelo exportado:** `modelo_random_forest_atraso_voos.pkl`  

O modelo mostrou boa generalização e aderência ao objetivo de negócio.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

**Linguagem**
- Python 3.x

**Análise e Manipulação de Dados**
- Pandas  
- NumPy  

**Visualização**
- Matplotlib  
- Seaborn  

**Machine Learning**
- Scikit-learn  

**Serialização**
- Joblib  

---

## 🚀 Pipeline do Projeto
1. Coleta e carregamento dos dados  
2. Limpeza e tratamento de valores nulos  
3. Engenharia de atributos (*Feature Engineering*)  
4. Análise Exploratória (EDA)  
5. Treinamento e comparação de modelos  
6. Avaliação com métricas apropriadas  
7. Ajuste de hiperparâmetros  
8. Calibração de threshold  
9. Exportação do modelo final  

---

## 📦 Como Executar o Projeto

### 🔧 Pré-requisitos
Instale as dependências necessárias:

```bash
pip install pandas numpy scikit-learn joblib matplotlib seaborn
```

### ▶️ Utilizando o Modelo Exportado
Exemplo de carregamento do modelo:

```python
import joblib
import pandas as pd

modelo = joblib.load("modelo_random_forest_atraso_voos.pkl")

# Exemplo de predição
probabilidades = modelo.predict_proba(X_novo)[:, 1]
predicao = (probabilidades >= 0.4).astype(int)
```

---

## 📌 Considerações Finais
Este projeto demonstra a aplicação prática de **Machine Learning orientado a negócio**, indo além da acurácia e focando em decisões estratégicas.  
A abordagem adotada pode ser facilmente adaptada para outros problemas de **classificação com custos assimétricos**.

---

📬 Em caso de dúvidas ou sugestões, fique à vontade para entrar em contato.
