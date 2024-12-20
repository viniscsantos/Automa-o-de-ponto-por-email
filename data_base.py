import pandas as pd


entrada = []
inicio_almoco = []
fim_almoco = []
saida = []

entrada_series = pd.Series(entrada)
inicio_almoco_series = pd.Series(inicio_almoco)
fim_almoco_series = pd.Series(fim_almoco)
saida_series = pd.Series(saida)

espelho_ponto = pd.DataFrame({
        'entrada': entrada_series,
        'ida almoço': inicio_almoco_series,
        'volta almoço': fim_almoco_series,
        'saída': saida_series
    })

print(espelho_ponto)
