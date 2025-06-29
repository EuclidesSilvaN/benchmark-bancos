#!/usr/bin/env python3
"""
Teste simples de conexão com MongoDB Atlas
"""

from pymongo import MongoClient

def test_simple_connection():
    """Testa conexão com string simplificada"""
    
    # String de conexão simplificada
    uri = "mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    print("🔍 Testando conexão simples...")
    print(f"URI: {uri.split('@')[1] if '@' in uri else 'URI inválida'}")
    
    try:
        # Conectar
        cliente = MongoClient(uri)
        
        # Testar conexão
        dbs = cliente.list_database_names()
        
        print(f"✅ Conexão bem-sucedida!")
        print(f"📚 Bancos disponíveis: {len(dbs)}")
        
        if dbs:
            print(f"Bancos: {dbs[:5]}")
        
        # Testar operação básica
        db = cliente["steam_db"]
        collections = db.list_collection_names()
        print(f"📋 Coleções no banco 'steam_db': {len(collections)}")
        
        cliente.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🔌 Teste Simples de Conexão")
    print("=" * 30)
    
    if test_simple_connection():
        print("\n🎉 Conexão funcionando!")
    else:
        print("\n❌ Problema na conexão.")
        print("\n🔧 Verifique:")
        print("1. Se o usuário 'euclidespu21' foi criado no Atlas")
        print("2. Se a senha está correta")
        print("3. Se o IP está liberado (Allow Access from Anywhere)")

    # Testar conexão com o código fornecido
    uri = "mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    try:
        client = MongoClient(uri)
        print(client.list_database_names())
        print("✅ Conexão bem-sucedida!")
    except Exception as e:
        print("❌ Erro:", e) 