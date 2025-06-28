from pymongo import MongoClient
import time

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["steam_db"]
colecao = db["games"]

# Filtro e atualização
filtro = {"nome": "Elden Ring"}
nova_info = {"$set": {"preco": 249.90}}

# Medir tempo da operação
inicio = time.perf_counter()
resultado = colecao.update_one(filtro, nova_info)
fim = time.perf_counter()

# Exibir resultado
print(f"Documentos modificados: {resultado.modified_count}")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")