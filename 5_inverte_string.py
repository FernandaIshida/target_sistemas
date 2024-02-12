'''Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''


def inverte_string(entrada: str):
    saida = ''
    for i in range(len(entrada) - 1, -1, -1):
        saida += entrada[i]

    return saida


print(inverte_string('target'))
