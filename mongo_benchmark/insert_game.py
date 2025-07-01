from pymongo import MongoClient
import time

# Conectando ao MongoDB Atlas
cliente = MongoClient("mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cliente["steam_db"]
colecao = db["games"]

# Documento a ser inserido
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

# Medição do tempo de inserção
inicio = time.perf_counter()
resultado = colecao.insert_one(novo_jogo)
fim = time.perf_counter()

print(f"Inserção concluída. ID do documento: {resultado.inserted_id}")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")