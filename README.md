# 🎮 Benchmark MongoDB Atlas - Dataset Steam

Este projeto realiza benchmarks de performance no MongoDB Atlas usando um dataset real da Steam, agora lido diretamente do arquivo CSV.

## 📋 Pré-requisitos

- Conta no [MongoDB Atlas](https://cloud.mongodb.com)
- Python 3.8+
- Dataset `steam_games.csv` na pasta do projeto

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/mongo-benchmark.git
cd mongo-benchmark
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure a string de conexão do Atlas
- Use o arquivo `.env` para definir sua string de conexão, nome do banco e coleção.
- Exemplo de `.env`:
```
MONGODB_URI=mongodb+srv://usuario:senha@cluster0.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=gamessteam
COLLECTION_NAME=novos_jogos
```

### 4. Prepare o dataset
- Baixe o arquivo `steam_games.csv` do Kaggle e coloque na pasta do projeto.
- O benchmark já lê direto do CSV, não é necessário converter para JSON.
- Exemplo de linha do CSV:
```
name,publisher,original_price,genre
"Counter-Strike","Valve",9.99,"Action, Shooter"
```

### 5. Execute o benchmark completo
```bash
python benchmark_atlas.py
```
- O script irá conectar ao MongoDB Atlas, executar as operações e salvar os resultados em `results_atlas.csv`.

### 6. Gerar gráfico de performance
```bash
python plot_results.py
```
- O gráfico será salvo como `benchmark_mongodb.png`.

## 📊 Resultados
- Resultados dos benchmarks são salvos em `results_atlas.csv`.
- O gráfico de performance é salvo como `benchmark_mongodb.png`.

## 🛠️ Scripts principais
- `benchmark_atlas.py` — Benchmark completo com dataset real
- `plot_results.py` — Gera gráfico de performance
- Scripts auxiliares: inserção, consulta, atualização, deleção (opcional)

## 📝 Dicas
- Se mudar usuário/senha do Atlas, atualize a string de conexão no `.env`.
- Se der erro de autenticação, revise permissões e IP liberado no Atlas.
- Para rodar benchmarks com muitos dados, ajuste o parâmetro `MAX_DOCUMENTS` no `.env` ou `config.py`.

## 📁 Estrutura esperada do CSV
| name            | publisher | original_price | genre           |
|-----------------|-----------|---------------|-----------------|
| Counter-Strike  | Valve     | 9.99          | Action, Shooter |

## 🔒 Segurança
- **NUNCA** commite arquivos `.env` com credenciais
- Use variáveis de ambiente para configurações sensíveis
- O arquivo `.gitignore` já está configurado para proteger dados sensíveis

---

**Qualquer dúvida, envie uma issue ou entre em contato!** 