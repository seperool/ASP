"""
Módulo para carregar a matriz de admitância Y_bus de um arquivo CSV
e fornecer funções para extrair os componentes de condutância (G) e
susceptância (B) entre barras específicas.
"""

# Importações de bibliotecas
import pandas as pd
import numpy as np
import cmath
import math

# Carregamento da matriz Y_bus a partir do arquivo CSV
caminho_arquivo = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Matriz_Ybus.csv"
Y_bus_str = pd.read_csv(caminho_arquivo, header=0, dtype=str).to_numpy() # Lê a matriz Ybus do arquivo CSV como strings
print("Matriz Ybus carregada:")
print(Y_bus_str)

Y_bus = np.vectorize(complex)(Y_bus_str)                                 # Converte a matriz de strings para complexos
print("Matriz Ybus convertida para complex:")
print(Y_bus)
print(Y_bus.dtype)

# Funções para extrair G e B da matriz de admitância Y_bus
# Extrai o condutância Gkm da matriz Y_bus
def get_G(Y_bus, k, m):
    Y_km = Y_bus[k, m]
    Gkm = Y_km.real
    return Gkm

# Extrai a susceptância Bkm da matriz Y_bus
def get_B(Y_bus, k, m):
    Y_km = Y_bus[k, m]
    Bkm = Y_km.imag
    return Bkm

# Exemplo de uso das funções get_G e get_B
#G11 = get_G(Y_bus, 0, 0)  
#print(f"G11: {G11}")
#B11 = get_B(Y_bus, 0, 0)
#print(f"B11: {B11}")