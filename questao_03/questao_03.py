import json

# Leitura do arquivo JSON com os dados de faturamento diário
with open("dados.json", "r") as file:
    faturamento_diario = json.load(file)

# Atribuindo um valor da lista para inicializar as variáveis de comparação
menor_faturamento = faturamento_diario[0]["valor"]
maior_faturamento = faturamento_diario[0]["valor"]

# Verificando menor e maior faturamento
for faturamento in faturamento_diario:
    if faturamento["valor"] > 0:
        if faturamento["valor"] < menor_faturamento:
            menor_faturamento = faturamento["valor"]
        if faturamento["valor"] > maior_faturamento:
            maior_faturamento = faturamento["valor"]

# Cálculo da média mensal de faturamento
dias_com_faturamento = []
for faturamento in faturamento_diario:
    if faturamento["valor"] > 0:
        dias_com_faturamento.append(faturamento["valor"])

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Dias no mês em que o valor de faturamento diário foi superior à média mensal
faturamento_acima_media = []

for faturamento in faturamento_diario:
    if faturamento["valor"] > media_mensal:
        faturamento_acima_media.append(faturamento["dia"])

num_faturamentos_acima_media = len(faturamento_acima_media)

# Resultados
print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor_faturamento}\n")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior_faturamento}\n")
print(
    f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:{num_faturamentos_acima_media}\n"
)
