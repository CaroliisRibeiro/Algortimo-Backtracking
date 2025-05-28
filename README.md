## Especificações do modelo treinado
### Modelo utilizado:
•	KNN (K-Nearest Neighbors)
Valor de K:
•	K = 5
### Variáveis utilizadas no vetor de entrada (na ordem):
[salario_anual, total_dividas, historico_pagamento, idade, credito_solicitado]
→ A variável idade foi utilizada no modelo.
Exemplo de previsão real realizada pelo modelo:
Entrada (X) = [68000, 12000, 0.89, 35, 15000]
Saída (y) = [3], onde 3 representa a categoria “Elegível”
### Arquivos a serem fornecidos:
### 1.	Modelo treinado (knn_model.pkl)
import joblib
joblib.dump(knn, 'knn_model.pkl')
### 2.	Scaler (caso tenha normalizado os dados — não foi usado neste caso)
Como não foi utilizada normalização, o modelo espera os dados na escala original, sem transformação.
### Mapeamento das classes:
### Com base na variável elegibilidade da base de dados:
•	1 = Não Elegível
•	2 = Análise
•	3 = Elegível


