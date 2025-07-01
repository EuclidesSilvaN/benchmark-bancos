import matplotlib.pyplot as plt
import csv

operacoes = []
tempos = []

with open('results_atlas.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        operacoes.append(row['Operacao'])
        tempos.append(float(row['Tempo_MongoDB_Atlas']))

plt.figure(figsize=(10, 6))
plt.bar(operacoes, tempos, color='royalblue')
plt.xlabel('Operação')
plt.ylabel('Tempo (segundos)')
plt.title('Benchmark MongoDB Atlas - Tempo por Operação')
plt.tight_layout()
plt.savefig('benchmark_mongodb.png')
plt.show() 