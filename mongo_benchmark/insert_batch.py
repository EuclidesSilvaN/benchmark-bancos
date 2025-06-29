from pymongo import MongoClient
import json
import time
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME, BATCH_SIZE, MAX_DOCUMENTS

def insert_large_dataset(file_path):
    """Insere um dataset grande em lotes"""
    try:
        # Conectar ao MongoDB Atlas
        cliente = MongoClient(MONGODB_URI)
        db = cliente[DATABASE_NAME]
        colecao = db[COLLECTION_NAME]
        
        print(f"Conectado ao MongoDB Atlas: {DATABASE_NAME}")
        
        # Limpar coleção antes da inserção
        print("Limpando coleção existente...")
        colecao.delete_many({})
        
        # Ler o arquivo JSON em lotes
        print(f"Carregando dataset de: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Limitar o número de documentos se necessário
        if len(dados) > MAX_DOCUMENTS:
            dados = dados[:MAX_DOCUMENTS]
            print(f"Limitando a {MAX_DOCUMENTS} documentos")
        
        total_docs = len(dados)
        print(f"Total de documentos a inserir: {total_docs}")
        
        # Inserir em lotes
        inicio_total = time.perf_counter()
        documentos_inseridos = 0
        
        for i in range(0, total_docs, BATCH_SIZE):
            lote = dados[i:i + BATCH_SIZE]
            
            inicio_lote = time.perf_counter()
            resultado = colecao.insert_many(lote)
            fim_lote = time.perf_counter()
            
            documentos_inseridos += len(resultado.inserted_ids)
            tempo_lote = fim_lote - inicio_lote
            
            print(f"Lote {i//BATCH_SIZE + 1}: {len(lote)} documentos inseridos em {tempo_lote:.4f}s")
        
        fim_total = time.perf_counter()
        tempo_total = fim_total - inicio_total
        
        print(f"\n✅ Inserção concluída!")
        print(f"Total de documentos inseridos: {documentos_inseridos}")
        print(f"Tempo total: {tempo_total:.4f} segundos")
        print(f"Taxa de inserção: {documentos_inseridos/tempo_total:.2f} docs/segundo")
        
        return documentos_inseridos, tempo_total
        
    except Exception as e:
        print(f"❌ Erro durante a inserção: {e}")
        return 0, 0
    finally:
        cliente.close()

if __name__ == "__main__":
    # Inserir dataset grande
    print("=== Inserção do Dataset Steam ===")
    insert_large_dataset("novos_jogos.json") 