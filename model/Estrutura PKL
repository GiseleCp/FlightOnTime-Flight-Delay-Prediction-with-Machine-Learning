📦 Estrutura dos Artefatos Entregues
entrega_modelo/
 ├── modelo_random_forest_atraso_voos.pkl
 └── ml_model/
      ├── __init__.py
      └── threshold_wrapper.py


⚠️ Importante
O arquivo threshold_wrapper.py deve estar disponível no ambiente onde o modelo for carregado, pois o joblib depende do path do módulo para reconstruir o objeto.

🚀 Orientações para Uso em Backend

Não aplicar threshold manualmente no backend

Utilizar:

model.predict(X) → decisão final (0 ou 1)

model.predict_proba(X) → probabilidade de atraso

Não modificar o wrapper sem versionar novamente o modelo

🧪 Boas Práticas e Versionamento

Qualquer alteração no threshold exige:

Nova versão do modelo

Novo arquivo .pkl

O nome do arquivo do modelo deve refletir a regra de negócio, por exemplo:

modelo_rf_atrasos_thr_0_4.pkl

✅ Benefícios da Abordagem

✔ Regra de negócio centralizada
✔ Menos acoplamento no backend
✔ Deploy previsível
✔ Evita erros de interpretação
✔ Padrão compatível com MLOps
