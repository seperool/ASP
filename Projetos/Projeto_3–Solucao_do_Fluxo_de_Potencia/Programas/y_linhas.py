# Bibliotecas necessárias
import pandas as pd
import numpy as np
import cmath
import math

# Leitura dos dados das barras e linhas a partir dos arquivos CSV
caminho_absoluto = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Dados_barras_pu.csv"
caminho_absoluto2 = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Dados_circuitos_pu.csv"

dt_barras = pd.read_csv(caminho_absoluto, sep=',')
print(dt_barras)

dt_linhas = pd.read_csv(caminho_absoluto2, sep=',')
print(dt_linhas)

# Cálculo da admitância das linhas
dt_linhas['Z_pu'] = dt_linhas['R_pu'] + 1j * dt_linhas['X_pu']
dt_linhas['Y_pu'] = 1 / dt_linhas['Z_pu']

print(dt_linhas)

# criar um DataFrame apenas com os dados necessários para Ybus
#juntando as DataFrames de barras e linhas

dt_linhas.to_csv('Dados_y.csv', index=False)