# import (nomeDaBiblioteca)==> importa biblioteca inteira     from math import log10 ==> importando somente o log

# function : def nome_da_funcao (argumento):
#   o que a função faz

# criar uma função que receba uma lista de 20 valores aleatórios, retornar apenas o maior valor e printar em tela:

# from random import randrange

# lista = []
# i = 1

# while i<= 20:
#     lista.append(r.randrange(0, 1000))
#     i = i+1

# print(f'Essa foi a lista gerada aleatoriamente: {lista}')

# def maior_valor(lista):
#     return max(lista, key=int)

#     print(f'Maior valor é: {maior_valor(lista)}')


    
    
    # def function (x, *args) *args = coloca uma lista  **kwargs= mesmo que args, mas com atribuições. Ex: elemento = valor

# 2- crie lista com 10 números aleatorios. mostrar quais são pares e quais ímpares

import random as x
lista = []
pares = []
impares = []
i = 1

while i<=10:
    lista.append(r.randrange(0, 1000))
    i = i+1

    print(f'Lista gerada: {lista}')

    def numeros(lista):
        for i in lista:
            if r % 2 = 0:
                pares.append(r)
                print(f'Números pares:{pares}')
            else:
                impares.append(r)
                print(f'Números ímpares: {impares}')