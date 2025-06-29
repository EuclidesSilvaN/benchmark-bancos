from pymongo import MongoClient
import time
import csv
import json
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME, BATCH_SIZE, MAX_DOCUMENTS

def run_benchmark():
    """Executa benchmark completo no MongoDB Atlas"""
    try:
        # Conectar ao MongoDB Atlas
        print("Conectando ao MongoDB Atlas...")
        cliente = MongoClient(MONGODB_URI)
        db = cliente[DATABASE_NAME]
        colecao = db[COLLECTION_NAME]
        
        print(f"✅ Conectado ao banco: {DATABASE_NAME}")
        
        # Resultados temporários
        resultados = []
        
        # Limpar a coleção antes do benchmark
        print("Limpando coleção...")
        colecao.delete_many({})
        
        # 1. Inserção em Massa do Dataset Steam
        print("\n=== 1. Inserção em Massa ===")
        try:
            with open("novos_jogos.json", "r", encoding="utf-8") as f:
                jogos = json.load(f)
            
            # Limitar documentos se necessário
            if len(jogos) > MAX_DOCUMENTS:
                jogos = jogos[:MAX_DOCUMENTS]
                print(f"Limitando a {MAX_DOCUMENTS} documentos")
            
            print(f"Inserindo {len(jogos)} jogos...")
            inicio = time.perf_counter()
            
            # Inserir em lotes para melhor performance
            for i in range(0, len(jogos), BATCH_SIZE):
                lote = jogos[i:i + BATCH_SIZE]
                colecao.insert_many(lote)
            
            fim = time.perf_counter()
            tempo_insercao = round(fim - inicio, 4)
            resultados.append(("Insercao_Massa", tempo_insercao))
            print(f"✅ Inserção concluída em {tempo_insercao}s")
            
        except Exception as e:
            print(f"❌ Erro na inserção: {e}")
            return
        
        # 2. Consulta Simples - Buscar por empresa
        print("\n=== 2. Consulta Simples ===")
        inicio = time.perf_counter()
        jogos_rockstar = list(colecao.find({"publisher": "Rockstar Games"}))
        fim = time.perf_counter()
        tempo_consulta_simples = round(fim - inicio, 4)
        resultados.append(("Consulta_Simples", tempo_consulta_simples))
        print(f"✅ Encontrados {len(jogos_rockstar)} jogos da Rockstar em {tempo_consulta_simples}s")
        
        # 3. Consulta Complexa - Jogos com preço < $30 e avaliação > 4
        print("\n=== 3. Consulta Complexa ===")
        inicio = time.perf_counter()
        jogos_baratos_bons = list(colecao.find({
            "price": {"$lt": 30},
            "positive_ratio": {"$gt": 80}
        }))
        fim = time.perf_counter()
        tempo_consulta_complexa = round(fim - inicio, 4)
        resultados.append(("Consulta_Complexa", tempo_consulta_complexa))
        print(f"✅ Encontrados {len(jogos_baratos_bons)} jogos baratos e bem avaliados em {tempo_consulta_complexa}s")
        
        # 4. Consulta de Agregação - Top 10 gêneros mais populares
        print("\n=== 4. Consulta de Agregação ===")
        inicio = time.perf_counter()
        pipeline = [
            {"$unwind": "$genres"},
            {"$group": {"_id": "$genres", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
        top_generos = list(colecao.aggregate(pipeline))
        fim = time.perf_counter()
        tempo_agregacao = round(fim - inicio, 4)
        resultados.append(("Agregacao", tempo_agregacao))
        print(f"✅ Top gêneros calculados em {tempo_agregacao}s")
        
        # 5. Atualização em Massa
        print("\n=== 5. Atualização em Massa ===")
        inicio = time.perf_counter()
        resultado_update = colecao.update_many(
            {"price": {"$lt": 10}},
            {"$set": {"price_category": "budget"}}
        )
        fim = time.perf_counter()
        tempo_atualizacao = round(fim - inicio, 4)
        resultados.append(("Atualizacao_Massa", tempo_atualizacao))
        print(f"✅ {resultado_update.modified_count} documentos atualizados em {tempo_atualizacao}s")
        
        # 6. Deleção em Massa
        print("\n=== 6. Deleção em Massa ===")
        inicio = time.perf_counter()
        resultado_delete = colecao.delete_many({"positive_ratio": {"$lt": 50}})
        fim = time.perf_counter()
        tempo_delecao = round(fim - inicio, 4)
        resultados.append(("Delecao_Massa", tempo_delecao))
        print(f"✅ {resultado_delete.deleted_count} documentos deletados em {tempo_delecao}s")
        
        # Salvar resultados em CSV
        print("\n=== Salvando Resultados ===")
        with open("results_atlas.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Operacao", "Tempo_MongoDB_Atlas"])
            writer.writerows(resultados)
        
        print("✅ Resultados salvos em results_atlas.csv")
        
        # Mostrar resumo
        print("\n=== RESUMO DO BENCHMARK ===")
        for operacao, tempo in resultados:
            print(f"{operacao}: {tempo}s")
        
        return resultados
        
    except Exception as e:
        print(f"❌ Erro durante o benchmark: {e}")
        return []
    finally:
        cliente.close()

if __name__ == "__main__":
    run_benchmark() 