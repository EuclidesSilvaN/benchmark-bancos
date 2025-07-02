# 🎮 Benchmark MongoDB Atlas - Dataset Steam

Este projeto realiza benchmarks de performance no MongoDB Atlas usando um dataset real da Steam.

## 📋 Pré-requisitos

1. **Conta MongoDB Atlas**
   - Crie uma conta em [cloud.mongodb.com](https://cloud.mongodb.com)
   - Crie um cluster (gratuito disponível)
   - Obtenha a string de conexão

2. **Python 3.8+**
   - Instale Python em [python.org](https://python.org)

3. **Dataset Steam**
   - O arquivo `novos_jogos.json` deve estar na pasta

## 🚀 Configuração Rápida

### 1. Setup Automático
```bash
cd mongo_benchmark
python setup_atlas.py
```

O script irá:
- Instalar dependências automaticamente
- Solicitar suas credenciais do Atlas
- Criar arquivo `.env` com configurações
- Testar a conexão

### 2. Setup Manual

#### Instalar dependências:
```bash
pip install -r requirements.txt
```

#### Criar arquivo `.env`:
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=steam_db
COLLECTION_NAME=games
BATCH_SIZE=1000
MAX_DOCUMENTS=10000
```

## 📊 Scripts Disponíveis

### 1. Análise do Dataset
```bash
python analyze_dataset.py
```
- Analisa a estrutura do dataset Steam
- Identifica campos disponíveis
- Mostra estatísticas básicas

### 2. Inserção em Lotes
```bash
python insert_batch.py
```
- Insere o dataset completo em lotes
- Otimizado para datasets grandes
- Mostra progresso e métricas

### 3. Benchmark Completo
```bash
python benchmark_atlas.py
```
- Executa todas as operações CRUD
- Mede performance de consultas
- Gera relatório CSV

## 🔧 Operações Testadas

1. **Inserção em Massa**
   - Carregamento do dataset Steam
   - Inserção em lotes otimizada

2. **Consulta Simples**
   - Busca por publisher/empresa
   - Filtros básicos

3. **Consulta Complexa**
   - Múltiplos critérios
   - Filtros de preço e avaliação

4. **Agregação**
   - Top gêneros mais populares
   - Estatísticas por categoria

5. **Atualização em Massa**
   - Modificação de múltiplos documentos
   - Adição de campos calculados

6. **Deleção em Massa**
   - Remoção por critérios
   - Limpeza de dados

## 📈 Resultados

Os resultados são salvos em:
- `results_atlas.csv` - Métricas de performance
- `benchmark_mongodb.png` - Gráficos (se disponível)

## 🛠️ Configurações Avançadas

### Ajustar Tamanho do Lote
```env
BATCH_SIZE=500  # Menor = mais lento, mas usa menos memória
```

### Limitar Documentos
```env
MAX_DOCUMENTS=5000  # Para testes rápidos
```

### Usar Dataset Diferente
```env
LARGE_DATASET_PATH=meu_dataset.json
```

## 🔍 Troubleshooting

### Erro de Conexão
- Verifique a string de conexão no `.env`
- Confirme se o IP está liberado no Atlas
- Teste as credenciais

### Dataset Muito Grande
- Reduza `MAX_DOCUMENTS` no `.env`
- Aumente `BATCH_SIZE` para melhor performance

### Erro de Memória
- Reduza `BATCH_SIZE`
- Processe o dataset em partes menores

## 📚 Estrutura do Projeto

```
mongo_benchmark/
├── config.py              # Configurações centralizadas
├── setup_atlas.py         # Setup automático
├── analyze_dataset.py     # Análise do dataset
├── insert_batch.py        # Inserção otimizada
├── benchmark_atlas.py     # Benchmark completo
├── requirements.txt       # Dependências
├── .env                   # Credenciais (criado pelo setup)
└── novos_jogos.json      # Dataset Steam
```

## 🎯 Próximos Passos

1. Execute o setup: `python setup_atlas.py`
2. Analise o dataset: `python analyze_dataset.py`
3. Insira os dados: `python insert_batch.py`
4. Execute o benchmark: `python benchmark_atlas.py`
5. Analise os resultados em `results_atlas.csv`

## 📞 Suporte

Se encontrar problemas:
1. Verifique se o MongoDB Atlas está ativo
2. Confirme as credenciais no arquivo `.env`
3. Teste a conexão com `python setup_atlas.py`
4. Verifique se o dataset está no formato correto 

dataset da Steam "https://www.kaggle.com/datasets/trolukovich/steam-games-complete-dataset"