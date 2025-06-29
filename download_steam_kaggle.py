import kagglehub
import pandas as pd
import os

# Baixar o dataset do Kaggle
print("Baixando dataset do Kaggle...")
path = kagglehub.dataset_download("fronkongames/steam-games-dataset")
print("Path to dataset files:", path)

# Encontrar o arquivo CSV baixado
csv_path = None
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.csv'):
            csv_path = os.path.join(root, file)
            break

if not csv_path:
    print("❌ Arquivo CSV não encontrado no dataset baixado!")
    exit(1)

print("Convertendo CSV para JSON...")
df = pd.read_csv(csv_path)
json_path = os.path.join(os.path.dirname(__file__), "novos_jogos.json")
df.to_json(json_path, orient='records', force_ascii=False)
print(f"✅ Conversão concluída! JSON salvo em: {json_path}") 