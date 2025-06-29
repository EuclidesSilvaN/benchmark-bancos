from pymongo import MongoClient
import time

# Conectar ao MongoDB Atlas
cliente = MongoClient("mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cliente["steam_db"]
colecao = db["games"]

# Filtro da consulta complexa
filtro = {
    "preco": {"$lt": 300},
    "avaliacoes.nota": {"$gt": 4}
}

# Medição de tempo
inicio = time.perf_counter()
resultados = list(colecao.find(filtro))
fim = time.perf_counter()

# Exibir resultados
print("Jogos com preço < R$300 e nota > 4:")
for jogo in resultados:
    print(f"- {jogo['nome']} (R$ {jogo['preco']})")

print(f"Tempo de execução: {fim - inicio:.4f} segundos")