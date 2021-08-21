import os
import time
from typing import List

def clear():
    os.system('cls')

def lista(ListaNumeros):
    clear()

    print("Introduz o numero. E depois a frequencia absoluta.")
    print("Quando terminares escreve *s*")
    print("Para apagar um numero escreve *n*")
    print("")
    print("Lista:")

    temp = ''

    for x in ListaNumeros:
        temp = temp + str(x) + '  '
    print(temp)
    print("")
    ListaTemporario = input()
    if ListaTemporario == "s":
        return ListaNumeros
    if ListaTemporario == "n":
        try:
            ListaNumeros.pop()
            lista(ListaNumeros)
        except:
            lista(ListaNumeros)
    try:
        try:
            ListaTemporario = int(ListaTemporario)
            ListaNumeros.append(int(ListaTemporario))
            lista(ListaNumeros)
        except:
            ListaTemporario = float(ListaTemporario)
            ListaNumeros.append(float(ListaTemporario))
            lista(ListaNumeros)
    except:
        if ListaTemporario != "s" and ListaTemporario != "n":
            print("Nao percebi esse ultimo.")
            time.sleep(0.8)
            lista(ListaNumeros)

def cota(listaValores, valorDistribuir, bias):
    divisorPadrao = 0
    listaCotas = {}

    for x in listaValores:
        divisorPadrao += x
    
    divisorPadrao = divisorPadrao / valorDistribuir
    divisorPadrao += bias
    divisorPadrao = round(divisorPadrao, 3)

    for x in listaValores:
        cotaPadrao = x / divisorPadrao
        listaCotas[str(x)] = round(cotaPadrao, 0)   
     
    return divisorPadrao, listaCotas

def total(listaCotas):
    valorTotal = 0
    for x in listaCotas:
        valorTotal += listaCotas[x]
    return valorTotal

def resolucao(listaValores):
    done = False
    valorDistribuir = 110
    bias = 0

    while not done:
        bias = round(bias, 3)
        # Calculacao das cotas
        divisorPadrao, listaCotas = cota(listaValores, valorDistribuir, bias)

        #check if it is correct
        valorTotal = total(listaCotas)
        if valorTotal == valorDistribuir:
            done = True
        elif valorTotal < valorDistribuir:
            bias -= 0.001
        elif valorTotal > valorDistribuir:
            bias += 0.001
    
    print(divisorPadrao)
    print(listaCotas)



def main():
    # Declaracao de variveis
    listaValores = []

    # Aquisicao de valores
    lista(listaValores)
    clear()

    # Resolucao
    resolucao(listaValores)


if __name__ == "__main__":
    main()