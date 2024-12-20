import lista_ponto
from auto_mail import pegar_hora

print("BEM VINDO AO ESPELHO DE PONTO!")
print('-' * 60)

while True:
    resp = int(input("1-Registrar dia"'\n'
                     "2-Registrar folga"'\n'
                     "3-Mostrar Espelho de Ponto"'\n'
                     "4-Sair"'\n'))
    if resp == 1:
        if lista_ponto.verifica_dia():
            lista_ponto.adicionar_ponto('entrada.json', pegar_hora())
            lista_ponto.adicionar_ponto('saida_almoco.json', pegar_hora())
            lista_ponto.adicionar_ponto('volta_almoco.json', pegar_hora())
            lista_ponto.adicionar_ponto('saida.json', pegar_hora())
            if lista_ponto.verifica_atraso():
                lista_ponto.adiciona_atraso(lista_ponto.calcula_debito())
                lista_ponto.adiciona_extra('00:00')
            else:
                lista_ponto.adiciona_extra(lista_ponto.calcula_debito())
                lista_ponto.adiciona_atraso('00:00')
            print("Dia registrado com sucesso!")
        else:
            print('DIA PREENCHIDO, VOLTE AMANHÃ!')
    elif resp == 2:
        if lista_ponto.verifica_dia():
            lista_ponto.adicionar_ponto('entrada.json', 'FOLGA')
            lista_ponto.adicionar_ponto('saida_almoco.json', 'FOLGA')
            lista_ponto.adicionar_ponto('volta_almoco.json', 'FOLGA')
            lista_ponto.adicionar_ponto('saida.json', 'FOLGA')
            lista_ponto.adiciona_atraso('00:00')
            lista_ponto.adiciona_extra('00:00')
            print("Folga registrada .")
        else:
            print('DIA PREENCHIDO, VOLTE AMANHÃ!')
    elif resp == 3:
        print(lista_ponto.mostrar_tabela1())
        print('-' * 60)
    elif resp == 4:
        break
    else:
        print("Escolha uma das opções")
