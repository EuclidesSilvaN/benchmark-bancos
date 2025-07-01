# 🎮 Benchmark MongoDB Atlas - Dataset Steam

Este projeto realiza benchmarks de performance no MongoDB Atlas usando um dataset real da Steam.

## 📋 Pré-requisitos

- Conta no [MongoDB Atlas](https://cloud.mongodb.com)
- Python 3.8+
- Dataset `novos_jogos.json` na pasta `mongo_benchmark`

## 🚀 Como rodar o projeto

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Configure a string de conexão do Atlas
No código dos scripts, já está configurado para:
```
mongodb+srv://euclidespu21:9zYS8ofWt8vvVER@cluster0.s2qxmqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```
Se mudar usuário/senha, altere nos scripts.

### 3. Execute os scripts principais

- Inserir um jogo:
  ```bash
  python insert_game.py
  ```
- Consulta simples:
  ```bash
  python query_simple.py
  ```
- Consulta complexa:
  ```bash
  python query_complex.py
  ```
- Atualizar jogo:
  ```bash
  python update_game.py
  ```
- Deletar jogo:
  ```bash
  python delete_game.py
  ```
- Benchmark completo:
  ```bash
  python benchmark_runner.py
  ```
- Benchmark com dataset real e operações avançadas:
  ```bash
  python benchmark_atlas.py
  ```

### 4. Gerar gráfico de performance
```bash
python plot_results.py
```
O gráfico será salvo como `benchmark_mongodb.png`.

## 📈 Resultados
- Resultados dos benchmarks são salvos em `results.csv` e `results_atlas.csv`.
- O gráfico de performance é salvo como `benchmark_mongodb.png`.

## 🤝 Colaboração em grupo
- Suba o projeto para o GitHub:
  ```bash
  git init
  git add .
  git commit -m "Benchmark MongoDB Atlas funcionando"
  git branch -M main
  git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
  git push -u origin main
  ```
- Compartilhe o link do repositório com o grupo.
- Todos podem clonar, instalar dependências e rodar os scripts normalmente.

## 🛠️ Dicas
- Se mudar usuário/senha do Atlas, atualize a string de conexão nos scripts.
- Se der erro de autenticação, redefina a senha no Atlas e aguarde 1-2 minutos.
- Para rodar benchmarks com muitos dados, ajuste o arquivo `novos_jogos.json`.

## 📂 Estrutura dos scripts principais
- `insert_game.py` — Insere um jogo
- `query_simple.py` — Consulta simples
- `query_complex.py` — Consulta complexa
- `update_game.py` — Atualiza um jogo
- `delete_game.py` — Deleta um jogo
- `benchmark_runner.py` — Benchmark básico
- `benchmark_atlas.py` — Benchmark avançado com dataset real
- `plot_results.py` — Gera gráfico de performance

---

**Qualquer dúvida, envie uma issue ou entre em contato!** 