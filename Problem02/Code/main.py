# Author: Cleiton Brito

import string

def elementos(qtd):
    if qtd < 27:
        letras = list(string.ascii_lowercase)
        aux_elementos = []
        for i in range(0, qtd):
            aux_elementos.append(letras[i])

        elementos = []

        # Último elemento na primeira posição
        elementos[0:] = aux_elementos[-1]
        
        #  Os demais elementos a partir da posição 1
        elementos[1:] = aux_elementos[0:-1]

        return elementos
    else:
        return print("Não é possível ser maior que 26")
    


def main():
    el_qtd = int(input("Quantos elementos? "))
    el = elementos(el_qtd)

    pos = int(input("Qual posição você deseja encontar? "))

    print("Elemento: "+el[pos % el_qtd] )

main()

