#!/usr/bin/env python3
"""
Script para testar conexão com MongoDB Atlas
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

def test_connection():
    """Testa a conexão com MongoDB Atlas"""
    print("🔍 Testando conexão com MongoDB Atlas...")
    
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Obter string de conexão
    mongodb_uri = os.getenv('MONGODB_URI')
    
    if not mongodb_uri:
        print("❌ MONGODB_URI não encontrada no arquivo .env")
        print("Execute primeiro: python setup_atlas.py")
        return False
    
    try:
        # Conectar ao MongoDB Atlas
        print(f"Conectando a: {mongodb_uri.split('@')[1] if '@' in mongodb_uri else 'URI inválida'}")
        
        cliente = MongoClient(mongodb_uri)
        
        # Testar conexão listando bancos
        dbs = cliente.list_database_names()
        
        print(f"✅ Conexão bem-sucedida!")
        print(f"📚 Bancos disponíveis: {len(dbs)}")
        
        if dbs:
            print(f"Bancos: {dbs[:5]}...")  # Mostrar primeiros 5
        
        # Testar operação básica
        db_name = os.getenv('DATABASE_NAME', 'steam_db')
        db = cliente[db_name]
        
        # Listar coleções
        collections = db.list_collection_names()
        print(f"📋 Coleções no banco '{db_name}': {len(collections)}")
        
        if collections:
            print(f"Coleções: {collections}")
        
        cliente.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        print("\n🔧 Possíveis soluções:")
        print("1. Verifique se o arquivo .env existe")
        print("2. Confirme a string de conexão")
        print("3. Verifique se o IP está liberado no Atlas")
        print("4. Teste as credenciais")
        return False

def show_connection_info():
    """Mostra informações da conexão"""
    load_dotenv()
    
    print("\n📋 Informações da Conexão:")
    print("=" * 30)
    
    mongodb_uri = os.getenv('MONGODB_URI', 'Não configurada')
    database_name = os.getenv('DATABASE_NAME', 'steam_db')
    collection_name = os.getenv('COLLECTION_NAME', 'games')
    
    # Mascarar senha na URI
    if '@' in mongodb_uri:
        parts = mongodb_uri.split('@')
        if ':' in parts[0]:
            user_pass = parts[0].split(':')
            masked_uri = f"{user_pass[0]}:****@{parts[1]}"
        else:
            masked_uri = mongodb_uri
    else:
        masked_uri = mongodb_uri
    
    print(f"URI: {masked_uri}")
    print(f"Database: {database_name}")
    print(f"Collection: {collection_name}")

if __name__ == "__main__":
    print("🔌 Teste de Conexão MongoDB Atlas")
    print("=" * 40)
    
    show_connection_info()
    
    if test_connection():
        print("\n🎉 Tudo funcionando! Você pode executar o benchmark.")
        print("Execute: python run_benchmark.py")
    else:
        print("\n❌ Problema na conexão. Verifique as configurações.") 