from pymongo import MongoClient
import time

# Conectar ao MongoDB Atlas
cliente = MongoClient("mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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