
""""
def mostrar_dia():
    with open('dia.json', 'r') as arquivo:
        dia = json.load(arquivo)
    return dia


def mostrar_entrada():
    with open('entrada.json', 'r') as arquivo:
        entrada = json.load(arquivo)
    return entrada


def mostrar_saida_almoco():
    with open('saida_almoco.json', 'r') as arquivo:
        saida_almoco = json.load(arquivo)
    return saida_almoco


def mostrar_volta_almoco():
    with open('volta_almoco.json', 'r') as arquivo:
        volta_almoco = json.load(arquivo)
    return volta_almoco


def mostrar_saida():
    with open('saida.json', 'r') as arquivo:
        saida = json.load(arquivo)
    return saida


def mostrar_debito():
    with open('debito.json', 'r') as arquivo:
        debito = json.load(arquivo)
    return debito 
    def adiciona_entrada(a):
    # Abre o arquivo
    with open('entrada.json', 'r') as arquivo:
        entrada = json.load(arquivo)
    # Adiciona valor
    entrada.append(a)

    # Salva a lista em um arquivo
    with open('entrada.json', 'w') as arquivo:
        json.dump(entrada, arquivo)


def adiciona_saida_almoco(b):
    # Abre o arquivo
    with open('saida_almoco.json', 'r') as arquivo:
        saida_almoco = json.load(arquivo)
    # Adiciona valor
    saida_almoco.append(b)

    # Salva a lista em um arquivo
    with open('saida_almoco.json', 'w') as arquivo:
        json.dump(saida_almoco, arquivo)


def adiciona_volta_almoco(c):
    # Abre o arquivo
    with open('volta_almoco.json', 'r') as arquivo:
        volta_almoco = json.load(arquivo)
    # Adiciona valor
    volta_almoco.append(c)

    # Salva a lista em um arquivo
    with open('volta_almoco.json', 'w') as arquivo:
        json.dump(volta_almoco, arquivo)


def adiciona_saida(d):
    # Abre o arquivo
    with open('saida.json', 'r') as arquivo:
        saida = json.load(arquivo)
    # Adiciona valor
    saida.append(d)

    # Salva a lista em um arquivo
    with open('saida.json', 'w') as arquivo:
        json.dump(saida, arquivo)
"""""

from lista_ponto import calcula_debito

print(calcula_debito())


