'''Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''


def calcula_perc_estado(faturamento_por_estado: dict):
    total = 0

    for estado in faturamento_por_estado:
        total += faturamento_por_estado[estado]

    for estado in faturamento_por_estado:
        representacao = (faturamento_por_estado[estado] / total) * 100
        print(f'O percentual de representação do estado {estado} é de {representacao:,.2f}%.')


faturamento_estadual = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53
}

calcula_perc_estado(faturamento_estadual)
