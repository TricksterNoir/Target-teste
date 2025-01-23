"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)
    
faturamento = [dia for dia in dados if dia > 0]

if faturamento:
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media = sum(faturamento) / len(faturamento)
    
    dias_acima_media = sum(1 for dia in dados if dia > media and dia > 0)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias acima da média: {dias_acima_media}")
else:
    print("Não há dados de faturamento.")