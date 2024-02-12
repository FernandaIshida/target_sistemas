'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
 ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''


def verifica_fibonacci(entrada):
    penultimo = 0
    ultimo = 1
    encontrado = False

    if entrada == 0 or entrada == 1:
        print(f'O valor {entrada} pertence a sequencia de Fibonacci.')
    else:
        while ultimo < entrada:
            soma = ultimo + penultimo
            penultimo = ultimo
            ultimo = soma

            if entrada == ultimo:
                print(f'O valor {entrada} pertence a sequencia de Fibonacci.')
                encontrado = True

        if not encontrado:
            print(f'O valor {entrada} não pertence a sequencia de Fibonacci.')


verifica_fibonacci(0)
verifica_fibonacci(1)
verifica_fibonacci(21)
verifica_fibonacci(22)


