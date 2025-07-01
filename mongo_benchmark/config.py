import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do MongoDB Atlas
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'steam_db')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'games')

# Configuração do dataset
STEAM_DATASET_PATH = os.getenv('STEAM_DATASET_PATH', 'steam_dataset.json')
LARGE_DATASET_PATH = os.getenv('LARGE_DATASET_PATH', 'novos_jogos.json')

# Configurações de benchmark
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '1000'))
MAX_DOCUMENTS = int(os.getenv('MAX_DOCUMENTS', '10000')) 