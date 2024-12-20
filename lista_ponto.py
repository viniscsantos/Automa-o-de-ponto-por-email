import json
import pandas as pd
from datetime import datetime, date


# Criar as listas das colunas
def verifica_dia():
    data = date.today()
    data = data.strftime("%d/%m/%y")
    with open('dia.json', 'r') as arquivo:
        dia = json.load(arquivo)
    if dia[-1] != data:
        dia.append(data)
        with open('dia.json', 'w') as arquivo:
            json.dump(dia, arquivo)
            cond = True
    else:
        cond = False
    return cond


def adicionar_ponto(document, hora):
    with open(document, 'r') as arquivo:
        val = json.load(arquivo)
    val.append(hora)
    with open(document, 'w') as arquivo:
        json.dump(val, arquivo)


# Retornar os valores das listas
def pegar_valor(val_arquivo):
    with open(val_arquivo, 'r') as arquivo:
        valor = json.load(arquivo)
    return valor


def verifica_atraso():
    pega_entrada = pegar_valor('entrada.json')
    pega_saida_almoco = pegar_valor('saida_almoco.json')
    pega_volta_almoco = pegar_valor('volta_almoco.json')
    pega_saida = pegar_valor('saida.json')

    entrada = pega_entrada[-1]
    saida_almoco = pega_saida_almoco[-1]
    volta_almoco = pega_volta_almoco[-1]
    saida = pega_saida[-1]
    base_dia = "09:00"
    time_base = datetime.strptime(base_dia, "%H:%M")
    hora_almoco = datetime.strptime("01:00", "%H:%M")
    ti1 = datetime.strptime(entrada, "%H:%M")
    ti2 = datetime.strptime(saida_almoco, "%H:%M")
    ti3 = datetime.strptime(volta_almoco, "%H:%M")
    ti4 = datetime.strptime(saida, "%H:%M")

    total_trabalho = (ti2 - ti1) + (ti4 - ti3)
    hora_trabalho = time_base - hora_almoco

    if hora_trabalho > total_trabalho:
        atraso = hora_trabalho - total_trabalho
        return True


def calcula_debito():
    pega_entrada = pegar_valor('entrada.json')
    pega_saida_almoco = pegar_valor('saida_almoco.json')
    pega_volta_almoco = pegar_valor('volta_almoco.json')
    pega_saida = pegar_valor('saida.json')

    entrada = pega_entrada[-1]
    saida_almoco = pega_saida_almoco[-1]
    volta_almoco = pega_volta_almoco[-1]
    saida = pega_saida[-1]

    base_dia = "09:00"
    time_base = datetime.strptime(base_dia, "%H:%M")
    hora_almoco = datetime.strptime("01:00", "%H:%M")
    ti1 = datetime.strptime(entrada, "%H:%M")
    ti2 = datetime.strptime(saida_almoco, "%H:%M")
    ti3 = datetime.strptime(volta_almoco, "%H:%M")
    ti4 = datetime.strptime(saida, "%H:%M")

    total_trabalho = (ti2 - ti1) + (ti4 - ti3)
    hora_trabalho = time_base - hora_almoco

    if hora_trabalho > total_trabalho:
        atraso = hora_trabalho - total_trabalho
        return "0" + str(atraso)[:-3]
    else:
        hora_extra = total_trabalho - hora_trabalho
        return "0" + str(hora_extra)[:-3]


def adiciona_atraso(valor):
    # Abre o arquivo
    with open('atraso.json', 'r') as arquivo:
        atraso = json.load(arquivo)
    # Adiciona valor
    atraso.append(valor)
    # Salva a lista em um arquivo
    with open('atraso.json', 'w') as arquivo:
        json.dump(atraso, arquivo)


def adiciona_extra(valor):
    # Abre o arquivo
    with open('hora_extra.json', 'r') as arquivo:
        extra = json.load(arquivo)
    # Adiciona valor
    extra.append(valor)
    # Salva a lista em um arquivo
    with open('hora_extra.json', 'w') as arquivo:
        json.dump(extra, arquivo)


# Imprimir em uma tabela
def mostrar_tabela1():
    dia_series = pd.Series(pegar_valor('dia.json'))
    entrada_series = pd.Series(pegar_valor('entrada.json'))
    inicio_almoco_series = pd.Series(pegar_valor('saida_almoco.json'))
    fim_almoco_series = pd.Series(pegar_valor('volta_almoco.json'))
    saida_series = pd.Series(pegar_valor('saida.json'))
    atraso_series = pd.Series(pegar_valor('atraso.json'))
    extra_series = pd.Series(pegar_valor('hora_extra.json'))

    espelho_ponto = pd.DataFrame({
        'DIA': dia_series,
        '| ENTRADA': entrada_series,
        '| INICIO DO INTERVALO': inicio_almoco_series,
        '| FIM DO INTERVALO': fim_almoco_series,
        '| SAIDA': saida_series,
        '| ATRASO': atraso_series,
        '| HORA EXTRA': extra_series
    })
    espelho_ponto.to_csv('espelho_ponto.csv')
    return espelho_ponto




