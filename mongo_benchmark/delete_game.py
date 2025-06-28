from pymongo import MongoClient
import time

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["steam_db"]
colecao = db["games"]

# Filtro de deleção
filtro = {"nome": "FIFA 25"}

# Medir tempo
inicio = time.perf_counter()
resultado = colecao.delete_one(filtro)
fim = time.perf_counter()

# Exibir resultado
print(f"Documentos removidos: {resultado.deleted_count}")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")