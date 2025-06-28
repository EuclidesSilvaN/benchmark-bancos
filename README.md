
## Como rodar o benchmark

1. **Instale as dependências:**
   ```bash
   pip install pymongo
   ```

2. **Certifique-se de que o MongoDB está rodando localmente**  
   (por padrão, o script conecta em `mongodb://localhost:27017/`).

3. **Execute o script de benchmark:**
   ```bash
   cd mongo_benchmark
   python benchmark_runner.py
   ```

4. **Veja os resultados:**  
   O tempo de cada operação será salvo no arquivo `results.csv`.

## Sobre o Dataset

O dataset utilizado é um arquivo JSON com informações de jogos da Steam, incluindo nome, gênero, preço, avaliações, empresa e data de lançamento.

## Scripts Individuais

Além do benchmark principal, há scripts separados para cada operação CRUD e consultas, facilitando testes e análises isoladas.

## Resultados

Os resultados do benchmark são salvos em `results.csv` e podem ser utilizados para gerar gráficos comparativos.

## Autor

Euclides Silva N.

---

**Dica:**  
Para gerar gráficos a partir do CSV, você pode usar Python com matplotlib ou seaborn. Se quiser um exemplo de script para isso, peça aqui!
