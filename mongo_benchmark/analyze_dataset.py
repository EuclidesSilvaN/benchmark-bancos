import json
from collections import Counter

def analyze_steam_dataset(file_path):
    """Analisa a estrutura do dataset da Steam"""
    try:
        print(f"Analisando dataset: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        print(f"Total de documentos: {len(dados)}")
        
        if len(dados) == 0:
            print("❌ Dataset vazio!")
            return
        
        # Analisar primeiro documento
        primeiro_doc = dados[0]
        print(f"\n=== ESTRUTURA DO PRIMEIRO DOCUMENTO ===")
        for chave, valor in primeiro_doc.items():
            tipo = type(valor).__name__
            if isinstance(valor, list):
                print(f"{chave} (list): {len(valor)} itens - {valor[:3] if valor else '[]'}")
            elif isinstance(valor, dict):
                print(f"{chave} (dict): {len(valor)} chaves - {list(valor.keys())[:3]}")
            else:
                print(f"{chave} ({tipo}): {valor}")
        
        # Analisar campos mais importantes
        print(f"\n=== ANÁLISE DOS CAMPOS ===")
        
        # Verificar campos de texto
        campos_texto = ['name', 'title', 'app_name', 'game_name']
        for campo in campos_texto:
            if campo in primeiro_doc:
                print(f"Campo de nome encontrado: '{campo}'")
                break
        
        # Verificar campos de preço
        campos_preco = ['price', 'cost', 'app_price']
        for campo in campos_preco:
            if campo in primeiro_doc:
                print(f"Campo de preço encontrado: '{campo}'")
                break
        
        # Verificar campos de gênero
        campos_genero = ['genres', 'genre', 'categories', 'tags']
        for campo in campos_genero:
            if campo in primeiro_doc:
                print(f"Campo de gênero encontrado: '{campo}'")
                break
        
        # Verificar campos de avaliação
        campos_avaliacao = ['positive_ratio', 'rating', 'score', 'reviews']
        for campo in campos_avaliacao:
            if campo in primeiro_doc:
                print(f"Campo de avaliação encontrado: '{campo}'")
                break
        
        # Verificar campos de publisher/empresa
        campos_empresa = ['publisher', 'developer', 'company', 'studio']
        for campo in campos_empresa:
            if campo in primeiro_doc:
                print(f"Campo de empresa encontrado: '{campo}'")
                break
        
        # Estatísticas básicas
        print(f"\n=== ESTATÍSTICAS BÁSICAS ===")
        
        # Contar documentos com preço
        docs_com_preco = [doc for doc in dados if any(campo in doc for campo in campos_preco)]
        print(f"Documentos com preço: {len(docs_com_preco)}")
        
        # Contar documentos com avaliação
        docs_com_avaliacao = [doc for doc in dados if any(campo in doc for campo in campos_avaliacao)]
        print(f"Documentos com avaliação: {len(docs_com_avaliacao)}")
        
        # Mostrar alguns exemplos de valores
        print(f"\n=== EXEMPLOS DE VALORES ===")
        
        # Exemplos de nomes
        nomes = []
        for campo in campos_texto:
            if campo in primeiro_doc:
                nomes = [doc.get(campo, 'N/A') for doc in dados[:5]]
                break
        if nomes:
            print(f"Exemplos de nomes: {nomes}")
        
        # Exemplos de preços
        precos = []
        for campo in campos_preco:
            if campo in primeiro_doc:
                precos = [doc.get(campo, 'N/A') for doc in dados[:5]]
                break
        if precos:
            print(f"Exemplos de preços: {precos}")
        
        return primeiro_doc
        
    except Exception as e:
        print(f"❌ Erro ao analisar dataset: {e}")
        return None

if __name__ == "__main__":
    # Analisar dataset grande
    print("=== ANÁLISE DO DATASET STEAM ===")
    estrutura = analyze_steam_dataset("novos_jogos.json")
    
    if estrutura:
        print(f"\n✅ Análise concluída! Use essas informações para adaptar as consultas.") 