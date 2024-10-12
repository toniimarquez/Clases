import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
np.random.seed(42) 
data = np.random.rand(100)
d_statistic, p_value = stats.kstest(data, 'uniform')
print(f'Estadístico D: {d_statistic}')
print(f'Valor p: {p_value}')
alpha = 0.05 
if p_value < alpha:
    print("Se rechaza la hipótesis nula: los datos no son uniformes.")
else:
    print("No se rechaza la hipótesis nula: los datos pueden ser uniformes.")

