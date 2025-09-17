# Programa para calcular Y_barra

# =========================================================
# Limpeza de Tela e Variaveis
# =========================================================
clc          # Limpa a tela do console
clear all    # Limpa todas as variaveis do workspace

# =========================================================
# Variaveis
# =========================================================
nbus = 4; # Número de barras
nlin = 9; # Número de linhas

# =========================================================
# Vetores
# =========================================================
k = [1,2,3,4,1,2,3,1,3]; # Barra de origem
m = [1,2,3,4,2,3,4,3,4]; # Barra de destino

# Cria o vetor de admitancias de forma mais eficiente
ykm = (1:nlin) * (0.1 + 1j); # Vetor com as admitancias das linhas
disp('Vetor de admitancias ykm:')
disp(ykm)

# =========================================================
# Calculo
# =========================================================

# Inicializa a matriz Y_barra com zeros
for i = 1:nbus
  for j = 1:nbus
    Y(i,j) = 0.0; # Inicializa cada elemento da matriz com zero
  end
end

# Calculando os valores de Y_barra
for i = 1:nlin
  p = k(i); # Barra de origem
  q = m(i); # Barra de destino
  r = ykm(i); # Admitancia da linha

  Y(p,p) = Y(p,p) + r; # Adiciona admitancia na diagonal (barra p)

  if (p ~= q)
    Y(q,q) = Y(q,q) + r; # Adiciona admitancia na diagonal (barra q)
    Y(p,q) = Y(p,q) - r; # Subtrai admitancia fora da diagonal
    Y(q,p) = Y(p,q); # Atribui o valor simetrico
  end
end

disp('Matriz Y-barra calculada:')
disp(Y)
