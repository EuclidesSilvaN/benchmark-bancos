from pymongo import MongoClient
import time

# Conectar ao MongoDB Atlas
cliente = MongoClient("mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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