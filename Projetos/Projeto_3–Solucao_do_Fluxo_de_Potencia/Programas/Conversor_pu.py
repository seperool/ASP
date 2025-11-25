# Biblioteca de Dados IEEE 14 Barras
import Dados_ieee14 as dados
import pandas as pd
import numpy as np
import cmath
import math

# Carregar os dados do módulo Dados_ieee14
S_base = dados.S_base # Base de Potência (MVA)
df_barras = dados.df_barras # Dados de Barras (DF_BARRAS)
df_circuitos = dados.df_circuitos # Dados de Circuitos (DLIN) – Dados Brutos

# Exibir os dados carregados
print("S_base:")
print(S_base)
print("Dados de Barras:")
print(df_barras)
print("\nDados de Circuitos:")
print(df_circuitos)

# iniciar DataFrame para dados em pu das barras
df = {'num':[],'cod':[],'Tipo':[],'v_pu':[], 'A_rad':[], 'Pg_pu':[], 'Qg_pu':[], 'Qn_pu':[], 'Qm_pu':[], 'Pl_pu':[], 'Ql_pu':[], 'Bc_pu':[]}
# Criação do DataFrame
df_barras_pu = pd.DataFrame(df)

# Adiciona colunas de identificação
df_barras_pu['num'] = df_barras['num']
df_barras_pu['cod'] = df_barras['Cod']
df_barras_pu['Tipo'] = df_barras['Tipo']

# Função para converter valores para pu
df_barras_pu['v_pu']= df_barras['V'] / 1000  # Tensão em pu (base 1000 V)
df_barras_pu['A_rad']= df_barras['A'] * (math.pi / 180)  # Ângulo em radianos
df_barras_pu['Pg_pu'] = df_barras['Pg'] / S_base  # Potência ativa gerada em pu
df_barras_pu['Qg_pu'] = df_barras['Qg'] / S_base  # Potência reativa gerada em pu
df_barras_pu['Qn_pu'] = df_barras['Qn'] / S_base  # Potência reativa mínima em pu
df_barras_pu['Qm_pu'] = df_barras['Qm'] / S_base  # Potência reativa máxima em pu
df_barras_pu['Pl_pu'] = df_barras['Pl'] / S_base  # Potência ativa de carga em pu
df_barras_pu['Ql_pu'] = df_barras['Ql'] / S_base  # Potência reativa de carga em pu
df_barras_pu['Bc_pu'] = df_barras['Bc'] / S_base  # Susceptância de carga em pu

print("\nDados de Barras em pu:")
print(df_barras_pu)

# Salvando dados em pu em arquivo CSV
df_barras_pu.to_csv('Dados_barras_pu.csv', index=False)

# iniciar DataFrame para dados em pu dos circuitos
df2 = {'De':[], 'Para':[], 'R_pu':[], 'X_pu':[], 'Bsh/2_pu':[], 'Tap':[]}
# Criação do DataFrame
df_circuitos_pu = pd.DataFrame(df2)

# Adiciona colunas de identificação
df_circuitos_pu['De'] = df_circuitos['De']
df_circuitos_pu['Para'] = df_circuitos['Para']

# Função para converter valores para pu
df_circuitos_pu['R_pu'] = df_circuitos['R%'] / S_base  # Resistência em pu
df_circuitos_pu['X_pu'] = df_circuitos['X%'] / S_base  # Reatância em pu
df_circuitos_pu['Bsh/2_pu'] = (df_circuitos['Bsh_Mvar'] / (S_base*2))  # Susceptância de cada lado em pu
df_circuitos_pu['Tap'] = 1 / df_circuitos['Tap']  # Fator de transformação (inverso do valor dado)

# print("\nDados de Circuitos em pu:")
print(df_circuitos_pu)

# Salvando dados em pu em arquivo CSV
df_circuitos_pu.to_csv('Dados_circuitos_pu.csv', index=False)