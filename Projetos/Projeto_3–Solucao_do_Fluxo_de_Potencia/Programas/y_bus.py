import pandas as pd
import numpy as np
import cmath
import math

caminho_absoluto = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Dados_y.csv"
caminho_absoluto2 = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Dados_barras_pu.csv"

df_y = pd.read_csv(caminho_absoluto, sep=',')
print("Dados lidos para Y:")
print(df_y)

df_barras = pd.read_csv(caminho_absoluto2, sep=',')
df_barras.set_index('num', inplace=True) # <-- ESTE PASSO É CRUCIAL!
print("Dados das barras (com 'num' como índice):")
print(df_barras)

# Criação da matriz Ybus
# Inicialmente, uma matriz N x N de zeros, onde N é o número de barras
N = len(df_barras) # 14 barras
Y_bus = np.zeros((N, N), dtype=complex)
print("Matriz Ybus inicial:")
print(Y_bus)

# Preenchimento da matriz Ybus
for index, row in df_y.iterrows():
    # 1. Obter índices (ajustados para base zero: 1 -> 0)
    k = int(row['De']) - 1
    m = int(row['Para']) - 1

    # 2. Admitância em Série
    R = row['R_pu']
    X = row['X_pu']
    Z = R + 1j * X
    y_km = 1 / Z # Admitância em p.u. (Y_pu)

    # 3. Tap Inverso (a' = 1/a)
    a_prime = row['Tap']

    # 4. Admitância Shunt de Meia Linha (Bsh/2)
    Bsh_meio = row['Bsh/2_pu']

    # --- ATUALIZAÇÃO FORA DA DIAGONAL (Y_km e Y_mk) ---
    # FÓRMULA: Y_km = -y_km * a' (onde a' = 1/a)
    Y_bus[k, m] -= y_km * a_prime
    Y_bus[m, k] -= y_km * a_prime

    # --- ATUALIZAÇÃO NA DIAGONAL (Y_kk e Y_mm) ---

    # Para Y_kk (Barra 'De', que possui o Tap a')
    # FÓRMULA (Trafo): Y_kk += y_km * (a')^2
    # FÓRMULA (Linha): Y_kk += y_km
    Y_bus[k, k] += y_km * (a_prime ** 2)

    # Para Y_mm (Barra 'Para', sem Tap)
    # FÓRMULA: Y_mm += y_km
    Y_bus[m, m] += y_km

    # --- ADMITÂNCIA SHUNT DE MEIA LINHA (Adicionada nas Diagonais) ---
    # Adicionar o termo shunt em ambos os lados
    y_shunt = 1j * Bsh_meio
    Y_bus[k, k] += y_shunt
    Y_bus[m, m] += y_shunt

# --- PASSO 3: Adicionar Shunt de Barra (Bc) ---
# Fonte: df_barras_pu
for i in range(N):
    Bc = df_barras.loc[i + 1, 'Bc_pu'] # Usando loc com índice baseado em 1
    Y_bus[i, i] += 1j * Bc

print("Matriz Ybus final:")
print(Y_bus)

# Salvando a matriz Ybus em um arquivo CSV
Y_bus_df = pd.DataFrame(Y_bus)

Y_bus_df.to_csv('Matriz_Ybus.csv', index=False)