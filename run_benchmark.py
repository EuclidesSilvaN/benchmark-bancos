#!/usr/bin/env python3
"""
Script principal para executar benchmark completo no MongoDB Atlas
"""

import os
import sys
import time
from pathlib import Path

def check_requirements():
    """Verifica se todos os requisitos estão atendidos"""
    print("🔍 Verificando requisitos...")
    
    # Verificar se o arquivo .env existe
    if not os.path.exists(".env"):
        print("❌ Arquivo .env não encontrado!")
        print("Execute primeiro: python setup_atlas.py")
        return False
    
    # Verificar se o dataset existe
    if not os.path.exists("novos_jogos.json"):
        print("❌ Dataset 'novos_jogos.json' não encontrado!")
        print("Certifique-se de que o arquivo está na pasta atual.")
        return False
    
    # Verificar dependências
    try:
        import pymongo
        import dotenv
        print("✅ Dependências OK")
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("Execute: pip install -r requirements.txt")
        return False
    
    print("✅ Todos os requisitos atendidos!")
    return True

def run_analysis():
    """Executa análise do dataset"""
    print("\n📊 Analisando dataset...")
    try:
        from analyze_dataset import analyze_steam_dataset
        estrutura = analyze_steam_dataset("novos_jogos.json")
        if estrutura:
            print("✅ Análise concluída!")
            return True
        else:
            print("❌ Erro na análise!")
            return False
    except Exception as e:
        print(f"❌ Erro ao analisar dataset: {e}")
        return False

def run_insertion():
    """Executa inserção dos dados"""
    print("\n📥 Inserindo dados no MongoDB Atlas...")
    try:
        from insert_batch import insert_large_dataset
        docs_inseridos, tempo = insert_large_dataset("novos_jogos.json")
        if docs_inseridos > 0:
            print(f"✅ {docs_inseridos} documentos inseridos em {tempo:.2f}s")
            return True
        else:
            print("❌ Falha na inserção!")
            return False
    except Exception as e:
        print(f"❌ Erro na inserção: {e}")
        return False

def run_benchmark():
    """Executa benchmark completo"""
    print("\n⚡ Executando benchmark...")
    try:
        from benchmark_atlas import run_benchmark
        resultados = run_benchmark()
        if resultados:
            print("✅ Benchmark concluído!")
            return True
        else:
            print("❌ Falha no benchmark!")
            return False
    except Exception as e:
        print(f"❌ Erro no benchmark: {e}")
        return False

def show_results():
    """Mostra resultados do benchmark"""
    print("\n📈 Resultados do Benchmark:")
    print("=" * 40)
    
    if os.path.exists("results_atlas.csv"):
        try:
            import csv
            with open("results_atlas.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Pular cabeçalho
                for operacao, tempo in reader:
                    print(f"{operacao}: {tempo}s")
        except Exception as e:
            print(f"❌ Erro ao ler resultados: {e}")
    else:
        print("❌ Arquivo de resultados não encontrado!")

def main():
    """Função principal"""
    print("🎮 Benchmark MongoDB Atlas - Dataset Steam")
    print("=" * 50)
    
    # Verificar requisitos
    if not check_requirements():
        sys.exit(1)
    
    # Menu de opções
    print("\nEscolha uma opção:")
    print("1. Análise do dataset")
    print("2. Inserção de dados")
    print("3. Benchmark completo")
    print("4. Executar tudo (recomendado)")
    print("5. Mostrar resultados")
    print("0. Sair")
    
    while True:
        try:
            opcao = input("\nDigite sua opção (0-5): ").strip()
            
            if opcao == "0":
                print("👋 Até logo!")
                break
            elif opcao == "1":
                run_analysis()
            elif opcao == "2":
                run_insertion()
            elif opcao == "3":
                run_benchmark()
            elif opcao == "4":
                print("\n🚀 Executando fluxo completo...")
                if run_analysis() and run_insertion() and run_benchmark():
                    print("\n🎉 Fluxo completo executado com sucesso!")
                    show_results()
                else:
                    print("\n❌ Erro durante a execução!")
            elif opcao == "5":
                show_results()
            else:
                print("❌ Opção inválida!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main() 