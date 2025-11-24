# Biblioteca de Dados IEEE 14 Barras
import Dados_ieee14 as dados
import pandas as pd
import numpy as np
import cmath

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
