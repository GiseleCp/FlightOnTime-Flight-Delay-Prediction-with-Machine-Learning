# anac-vra-2024-hackathon
Dataset de voos ANAC + análise preditiva de atrasos (hackathon 2025 Alura/ Oracle Next Education)

✈️ FlightOnTime — Previsão de Atrasos de Voos

📌 Descrição  
O FlightOnTime é um MVP de ciência de dados desenvolvido para prever a probabilidade de atraso de um voo **antes da decolagem**, utilizando exclusivamente informações disponíveis no planejamento do voo.

O projeto foi desenvolvido com foco em **recall da classe atraso**, priorizando a detecção antecipada de riscos operacionais.

---

🎯 Objetivo do Modelo

Classificar voos como:

- **0** → Provavelmente pontual  
- **1** → Provavelmente atrasado  

---

🧠 Modelagem

- Logistic Regression  
- Pipeline com ColumnTransformer  
- One-Hot Encoding para variáveis categóricas  
- Balanceamento de classes (`class_weight='balanced'`)  
- Ajuste de threshold (0.4)  

O modelo prioriza **Recall da classe atraso**, alcançando aproximadamente **84% de detecção de atrasos**.

---

📊 Métricas Principais (Classe Atraso)

- Recall: ~84%  
- F1-score: ~0.34  
- Accuracy: reduzida (esperada devido ao desbalanceamento)

---

📁 Estrutura de Arquivos Gerados

```text
├── notebooks/
│   └── 02_Modelo_Preditivo_FlightOnTime_v3.ipynb
├── models/
│   └── model_flightontime.pkl
├── app.py
├── requirements.txt
├── MODEL_EVALUATION.md
└── README.md

