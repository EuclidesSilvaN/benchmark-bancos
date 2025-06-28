from pymongo import MongoClient
import time

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["steam_db"]
colecao = db["games"]

# Filtro da consulta simples
filtro = {"empresa": "Rockstar Games"}

# Medição de tempo
inicio = time.perf_counter()
resultados = list(colecao.find(filtro))
fim = time.perf_counter()

# Exibir resultados
print(f"Jogos encontrados da Rockstar Games:")
for jogo in resultados:
    print(f"- {jogo['nome']}")

print(f"Tempo de execução: {fim - inicio:.4f} segundos")