import pandas as pd
import numpy as np
import cmath
import math

# Calculo das potências ativa e reativa entre duas barras k e m
def Potencia_ativa():
    P = Vk * Vm * (Gkm * np.cos(theta_k - theta_m) + Bkm * np.sin(theta_k - theta_m))
    return P

def Potencia_reativa():
    Q = Vk * Vm * (Gkm * np.sin(theta_k - theta_m) - Bkm * np.cos(theta_k - theta_m))
    return Q

# mismatch de potência ativa
def delta_P(P, P_spec):
    P_calculada = Potencia_ativa()
    delta_P = P_spec - P_calculada
    return delta_P

# mismatch de potência reativa
def delta_Q(Q, Q_spec):
    Q_calculada = Potencia_reativa()
    delta_Q = Q_spec - Q_calculada
    return delta_Q

# Derivadas parciais da potência ativa em relação a theta e V
def deriv_P_theta():
    return dP_dtheta

def deriv_P_V():
    return dP_dV