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
        
        # Carregar dataset do CSV
        jogos = []
        with open("steam_games.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Converta o preço para float
                try:
                    price = float(row['original_price']) if row['original_price'] else 0.0
                except ValueError:
                    price = 0.0
                # Converta gêneros para lista
                genres = row['genre'].split(',') if row['genre'] else []
                jogos.append({
                    'name': row['name'],
                    'publisher': row['publisher'],
                    'price': price,
                    'genres': genres
                })
        if len(jogos) > MAX_DOCUMENTS:
            jogos = jogos[:MAX_DOCUMENTS]
            print(f"Limitando a {MAX_DOCUMENTS} documentos")

        # Limpar a coleção antes do benchmark
        print("Limpando coleção...")
        colecao.delete_many({})

        # 1. Inserção Simples
        print("\n=== 1. Inserção Simples ===")
        jogo_simples = jogos[0].copy()
        inicio = time.perf_counter()
        resultado_insercao_simples = colecao.insert_one(jogo_simples)
        fim = time.perf_counter()
        tempo_insercao_simples = round(fim - inicio, 4)
        resultados.append(("Insercao_Simples", tempo_insercao_simples))
        print(f"✅ Inserção simples concluída em {tempo_insercao_simples}s")

        # 2. Inserção em Massa (exceto o primeiro)
        print("\n=== 2. Inserção em Massa ===")
        jogos_massa = jogos[1:]  # exceto o primeiro
        print(f"Inserindo {len(jogos_massa)} jogos...")
        inicio = time.perf_counter()
        for i in range(0, len(jogos_massa), BATCH_SIZE):
            lote = jogos_massa[i:i + BATCH_SIZE]
            colecao.insert_many(lote)
        fim = time.perf_counter()
        tempo_insercao_massa = round(fim - inicio, 4)
        resultados.append(("Insercao_Massa", tempo_insercao_massa))
        print(f"✅ Inserção em massa concluída em {tempo_insercao_massa}s")

        # 3. Consulta Simples - Buscar por empresa
        print("\n=== 3. Consulta Simples ===")
        inicio = time.perf_counter()
        jogos_rockstar = list(colecao.find({"publisher": "Rockstar Games"}))
        fim = time.perf_counter()
        tempo_consulta_simples = round(fim - inicio, 4)
        resultados.append(("Consulta_Simples", tempo_consulta_simples))
        print(f"✅ Encontrados {len(jogos_rockstar)} jogos da Rockstar em {tempo_consulta_simples}s")

        # 4. Consulta Complexa - Jogos com preço < $30 e gênero Action
        print("\n=== 4. Consulta Complexa ===")
        inicio = time.perf_counter()
        jogos_baratos_bons = list(colecao.find({
            "price": {"$lt": 30},
            "genres": {"$in": ["Action"]}
        }))
        fim = time.perf_counter()
        tempo_consulta_complexa = round(fim - inicio, 4)
        resultados.append(("Consulta_Complexa", tempo_consulta_complexa))
        print(f"✅ Encontrados {len(jogos_baratos_bons)} jogos de ação baratos em {tempo_consulta_complexa}s")

        # 5. Atualização Simples
        print("\n=== 5. Atualização Simples ===")
        inicio = time.perf_counter()
        resultado_update_simples = colecao.update_one(
            {"_id": resultado_insercao_simples.inserted_id},
            {"$set": {"price_category": "budget"}}
        )
        fim = time.perf_counter()
        tempo_atualizacao_simples = round(fim - inicio, 4)
        resultados.append(("Atualizacao_Simples", tempo_atualizacao_simples))
        print(f"✅ 1 documento atualizado em {tempo_atualizacao_simples}s")

        # 6. Atualização em Massa
        print("\n=== 6. Atualização em Massa ===")
        inicio = time.perf_counter()
        resultado_update = colecao.update_many(
            {"price": {"$lt": 10}},
            {"$set": {"price_category": "budget"}}
        )
        fim = time.perf_counter()
        tempo_atualizacao = round(fim - inicio, 4)
        resultados.append(("Atualizacao_Massa", tempo_atualizacao))
        print(f"✅ {resultado_update.modified_count} documentos atualizados em {tempo_atualizacao}s")

        # 7. Deleção Simples
        print("\n=== 7. Deleção Simples ===")
        inicio = time.perf_counter()
        resultado_delete_simples = colecao.delete_one({"_id": resultado_insercao_simples.inserted_id})
        fim = time.perf_counter()
        tempo_delecao_simples = round(fim - inicio, 4)
        resultados.append(("Delecao_Simples", tempo_delecao_simples))
        print(f"✅ 1 documento deletado em {tempo_delecao_simples}s")

        # 8. Deleção em Massa
        print("\n=== 8. Deleção em Massa ===")
        inicio = time.perf_counter()
        resultado_delete = colecao.delete_many({"price": {"$gt": 100}})  # Exemplo: deleta jogos muito caros
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