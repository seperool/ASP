import pandas as pd
import numpy as np
import cmath
import math
import Get_Y as gy

caminho_arquivo = r"C:\Users\Sergio\github\ASP\Projetos\Projeto_3–Solucao_do_Fluxo_de_Potencia\Dados\Matriz_Ybus.csv"
Y_bus_str = pd.read_csv(caminho_arquivo, header=0, dtype=str).to_numpy() # Lê a matriz Ybus do arquivo CSV como strings
print("Matriz Ybus carregada:")
print(Y_bus_str)

Y_bus = np.vectorize(complex)(Y_bus_str)                                 # Converte a matriz de strings para complexos
print("Matriz Ybus convertida para complex:")
print(Y_bus)
print(Y_bus.dtype)


# Calculo das potências ativa e reativa entre duas barras k e m
#def Potencia_ativa():
#    P = Vk * Vm * (Gkm * np.cos(theta_k - theta_m) + Bkm * np.sin(theta_k - theta_m))
#    return P

#def Potencia_reativa():
#    Q = Vk * Vm * (Gkm * np.sin(theta_k - theta_m) - Bkm * np.cos(theta_k - theta_m))
#    return Q

# mismatch de potência ativa
#def delta_P(P, P_spec):
#    P_calculada = Potencia_ativa()
#    delta_P = P_spec - P_calculada
#    return delta_P

# mismatch de potência reativa
#def delta_Q(Q, Q_spec):
#    Q_calculada = Potencia_reativa()
#    delta_Q = Q_spec - Q_calculada
#    return delta_Q

# Derivadas parciais da potência ativa em relação a theta e V
#def deriv_P_theta():
#    return dP_dtheta

#def deriv_P_V():
#    return dP_dV