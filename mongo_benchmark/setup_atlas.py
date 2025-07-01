import os
import getpass

def setup_mongodb_atlas():
    """Configura as credenciais do MongoDB Atlas"""
    print("=== CONFIGURAÇÃO DO MONGODB ATLAS ===")
    print("Para conectar ao MongoDB Atlas, você precisa:")
    print("1. Criar uma conta no MongoDB Atlas (https://cloud.mongodb.com)")
    print("2. Criar um cluster")
    print("3. Obter a string de conexão")
    print("4. Configurar as credenciais\n")
    
    # Solicitar informações do usuário
    print("Digite as informações do seu cluster MongoDB Atlas:")
    
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    cluster_name = input("Nome do cluster (ex: cluster0): ")
    database_name = input("Nome do banco de dados (padrão: steam_db): ") or "steam_db"
    collection_name = input("Nome da coleção (padrão: games): ") or "games"
    
    # Construir a string de conexão
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/"
    
    # Criar arquivo .env
    env_content = f"""# MongoDB Atlas Configuration
MONGODB_URI={connection_string}
DATABASE_NAME={database_name}
COLLECTION_NAME={collection_name}

# Dataset Configuration
STEAM_DATASET_PATH=steam_dataset.json
LARGE_DATASET_PATH=novos_jogos.json

# Benchmark Configuration
BATCH_SIZE=1000
MAX_DOCUMENTS=10000
"""
    
    # Salvar arquivo .env
    with open(".env", "w") as f:
        f.write(env_content)
    
    print(f"\n✅ Arquivo .env criado com sucesso!")
    print(f"📁 String de conexão: {connection_string}")
    print(f"📊 Banco: {database_name}")
    print(f"📋 Coleção: {collection_name}")
    
    # Testar conexão
    print(f"\n=== TESTANDO CONEXÃO ===")
    try:
        from pymongo import MongoClient
        cliente = MongoClient(connection_string)
        
        # Listar bancos de dados para testar
        dbs = cliente.list_database_names()
        print(f"✅ Conexão bem-sucedida!")
        print(f"📚 Bancos disponíveis: {len(dbs)}")
        
        cliente.close()
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        print("Verifique suas credenciais e tente novamente.")
        return False
    
    return True

def install_dependencies():
    """Instala as dependências necessárias"""
    print(f"\n=== INSTALANDO DEPENDÊNCIAS ===")
    
    try:
        import subprocess
        import sys
        
        # Instalar dependências
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        print("Execute manualmente: pip install -r requirements.txt")

if __name__ == "__main__":
    print("🚀 Setup do MongoDB Atlas para Benchmark Steam")
    print("=" * 50)
    
    # Instalar dependências
    install_dependencies()
    
    # Configurar Atlas
    if setup_mongodb_atlas():
        print(f"\n🎉 Setup concluído com sucesso!")
        print(f"Próximos passos:")
        print(f"1. Execute: python analyze_dataset.py")
        print(f"2. Execute: python insert_batch.py")
        print(f"3. Execute: python benchmark_atlas.py")
    else:
        print(f"\n❌ Setup falhou. Verifique as credenciais.") 