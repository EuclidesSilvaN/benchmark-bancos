from pymongo import MongoClient
import time
import csv
import json

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["steam_db"]
colecao = db["games"]

# Resultados temporários
resultados = []

# Limpar a coleção antes do benchmark
colecao.delete_many({})

# 1. Inserção
novo_jogo = {
    "nome": "Cyberpunk 2077",
    "genero": ["RPG", "Ação"],
    "preco": 249.90,
    "avaliacoes": [
        {"usuario": "playerX", "nota": 4, "comentario": "Melhorou bastante"},
        {"usuario": "techboy", "nota": 5, "comentario": "Incrível com mods"}
    ],
    "empresa": "CD Projekt",
    "data_lancamento": "2020-12-10"
}
inicio = time.perf_counter()
colecao.insert_one(novo_jogo)
fim = time.perf_counter()
resultados.append(("Insercao", round(fim - inicio, 4)))

# 2. Consulta Simples
inicio = time.perf_counter()
list(colecao.find({"empresa": "Rockstar Games"}))
fim = time.perf_counter()
resultados.append(("Consulta_Simples", round(fim - inicio, 4)))

# 3. Consulta Complexa
inicio = time.perf_counter()
list(colecao.find({
    "preco": {"$lt": 300},
    "avaliacoes.nota": {"$gt": 4}
}))
fim = time.perf_counter()
resultados.append(("Consulta_Complexa", round(fim - inicio, 4)))

# 4. Atualização
inicio = time.perf_counter()
colecao.update_one({"nome": "Elden Ring"}, {"$set": {"preco": 249.90}})
fim = time.perf_counter()
resultados.append(("Atualizacao", round(fim - inicio, 4)))

# 5. Deleção
inicio = time.perf_counter()
colecao.delete_one({"nome": "FIFA 25"})
fim = time.perf_counter()
resultados.append(("Delecao", round(fim - inicio, 4)))

# 0. Inserção em Massa
with open("../steam_dataset.json", "r", encoding="utf-8") as f:
    jogos = json.load(f)
inicio = time.perf_counter()
colecao.insert_many(jogos)
fim = time.perf_counter()
resultados.append(("Insercao_Massa", round(fim - inicio, 4)))

# Salvar CSV
with open("results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Operacao", "Tempo_MongoDB"])
    writer.writerows(resultados)

print("Benchmark finalizado com sucesso! Resultados salvos em results.csv ✅") 