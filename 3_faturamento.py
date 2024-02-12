'''Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json


def processa_faturamento_mensal(filename):
    with open(filename, 'r') as file:
        file_data = json.load(file)

        menor_faturamento = file_data[0]['valor']
        maior_faturamento = file_data[0]['valor']
        total_faturamento = 0
        dias_com_faturamento = 0
        dias_faturamento_acima = 0

        for i in file_data:
            if i['valor'] > maior_faturamento:
                maior_faturamento = i['valor']

            if menor_faturamento > i['valor'] > 0:
                menor_faturamento = i['valor']

            if i['valor'] != 0:
                dias_com_faturamento += 1

            total_faturamento += i['valor']

        media_faturamento = total_faturamento / dias_com_faturamento
        for i in file_data:
            if i['valor'] > media_faturamento:
                dias_faturamento_acima += 1

        print(f'O menor valor de faturamento diário é de R$ {menor_faturamento}')
        print(f'O maior valor de faturamento diário é de R$ {maior_faturamento}')
        print(f'Houveram {dias_faturamento_acima} dias de faturamento no mês com valor acima da média mensal.')


processa_faturamento_mensal('dados.json')




