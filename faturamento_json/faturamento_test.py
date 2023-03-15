import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

    valor_min = round(min(item['valor'] for item in dados if item['valor']), 2)
    valor_max = round(max(item['valor'] for item in dados), 2)

    dias_validos = len([item['valor'] for item in dados if item['valor']])
    faturamento_total = round(sum(item['valor'] for item in dados if item['valor']), 2)
    media_faturamento = round((faturamento_total / dias_validos), 2)

    dias_faturamento_superior = len([item['valor'] for item in dados if item['valor'] > media_faturamento])

    print("Faturamento minimo: ", valor_min)
    print("Faturamento maximo: ", valor_max)
    print("Dias com faturamento superior a media: ", dias_faturamento_superior)