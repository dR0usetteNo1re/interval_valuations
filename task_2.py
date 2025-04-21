# ANSI - for console colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Сброс цвета

# Imports
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# Известные данные
n = 12 # Выборка
k = n - 1 # распределение Стьюдента (Степень свободы), так как у нас НЕ генеральная выборка (насколько я понял)
gamma = 0.95 # Надежность ŷ
x_i = [-0.5, -0.4, -0.4, -0.2, 0, 0.2, 0.6, 0.8, 1, 1.2, 1.2, 1.5]
n_i = [1, 2, 1, 1, 1, 1, 1, 1, 2, 1]

t_y = 2.20 #alpha = 1 - gamma (Значение по таблице Критические точки распределения Стьюдента)

# Расчет необходимых данных
print(f"{CYAN}T = (x̄ - a) / S / √n{RESET}")

x_mean = round(sum(x_i)/n, 3) # Выборочная средняя x̄

print(f"Выборочная средняя {RED}x̄ = {x_mean}{RESET}")


# В данной формуле мы вместо n подставляем k, так как x - Выборка из большой совокупности

S = sqrt(sum([(i - x_mean)**2 for i in x_i]) / k) # Исправленное Среднеквадратичное отклонение

print(f"Исправленное Среднеквадратичное отклонение {GREEN}S = {S}{RESET}")

lower = x_mean - (t_y * S) / sqrt(n)
upper = x_mean + (t_y * S) / sqrt(n)

print(f"Нижняя граница = {YELLOW}{lower}{RESET}\nВерхняя граница = {YELLOW}{upper}{RESET}")


# Строим интервал
x = np.linspace(lower, upper, 1000)
y = stats.norm.pdf(x, x_mean, S / sqrt(n))

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Нормальное распределение')
plt.fill_between(x, y, where=(x >= lower) & (x <= upper), color='lightgreen', alpha=0.5,
                 label='Доверительный интервал')
plt.axvline(x=lower, color='red', linestyle='--', label='Нижняя, Верхняя граница')
plt.axvline(x=upper, color='red', linestyle='--')
plt.title('Доверительный интервал для математического ожидания')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()
