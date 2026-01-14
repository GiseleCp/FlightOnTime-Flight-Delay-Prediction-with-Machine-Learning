# ✈️ FlightOnTime (anac-vra-2024-hackathon)
Dataset de voos ANAC + análise preditiva de atrasos (hackathon 2025 Alura/ Oracle Next Education)

### Previsão de Atrasos de Voos com Ciência de Dados

## 🎯 Objetivo do Projeto

Aplicar **Ciência de Dados na Aviação**, com foco na **antecipação de atrasos de voo**, por meio de um modelo preditivo confiável e integrado a uma API REST.

O objetivo final é permitir que sistemas e usuários consultem, em tempo real, o **status provável de um voo (Pontual ou Atrasado)** e sua **probabilidade associada**.

---

## 🧠 Visão Geral da Solução

O projeto é dividido em duas frentes principais:

- **Data Science**  
  Responsável por explorar os dados, criar features relevantes, treinar e validar o modelo preditivo e definir o threshold orientado ao negócio.

- **Back-End**  
  Responsável por expor uma API REST que consome o modelo preditivo e retorna a previsão em tempo real.

---

## 🔁 Arquitetura da Solução

[ Cliente / Front-end ]
|
v
POST /predict
|
v
[ API Java (Spring Boot) ]
|
| (OpenFeign)
v
[ Microsserviço Python ]
|
| (Modelo ML + Threshold fixo)
v
Probabilidade + Status
|
v
[ API Java ]
|
v
[ Cliente / Front-end ]

---


---

## 📊 Modelo Preditivo (Resumo Executivo)

- Modelo escolhido: **Random Forest**
- Métrica foco: **Recall da classe “Atrasado”**
- Recall final alcançado: **93%**
- Threshold fixado no modelo: **0.40**
- Saída do modelo:
  - Status: `PONTUAL` ou `ATRASADO`
  - Probabilidade associada (0 a 1)

O threshold foi **definido com base em ajustes**, evitando decisões arbitrárias na camada de Back-End.
O time de Back-end faz esse input na estrutura.

---

## 📦 Entregáveis

- Notebooks de Data Science (ETL, EDA e Modelagem)
- Modelo serializado (`.pkl`)
- API REST funcional
- Documentação mínima
- Demonstração via endpoint `/predict`

---

## 🛠️ Tecnologias Utilizadas

### Data Science
- Python
- Pandas, NumPy
- scikit-learn, CatBoost
- Jupyter / Google Colab

### Back-End
- Java
- Spring Boot
- OpenFeign
- API REST

---

## 👥 Time

Projeto desenvolvido de forma colaborativa entre as equipes de **Data Science** e **Back-End**, com integração contínua entre modelagem, arquitetura e entrega.
