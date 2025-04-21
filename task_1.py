# ANSI - for console colors  
RED = "\033[91m"  
GREEN = "\033[92m"  
YELLOW = "\033[93m"  
BLUE = "\033[94m"  
MAGENTA = "\033[95m"  
CYAN = "\033[96m"  
RESET = "\033[0m"  # Сброс цвета  
  
# Imports  
import scipy.stats as stats  
from math import sqrt  
import matplotlib.pyplot as plt  
import numpy as np  
  
# Известные данные  
# X - Нормальное распределение  
sigma = 3 # Среднеквадратичное отклонение σ  
x_bar = 5 # Выборочная средняя x̄  
n = 36 # Объем выборки  
gamma = 0.95 # Надежность оценки γ  
t = 1.96  
# t = stats.norm.ppf(1 - alpha / 2) # Вариант вычисления t без таблицы Лапласа  
  
print(f"{BLUE}P(|X - a| < δ) = 2F(δ/σ){RESET} - Начальная формула")  
print(f"{BLUE}P(|X - a| < δ) = 2F(δ√n/σ) = 2F(t){RESET} - Заменили X на x̄ σ и σ(x̄) = σ/√n")  
print(f"t = δ√n/σ, тогда δ = tσ/√n, ==> {YELLOW}P(|x̄ - a| < δ = tσ/√n) = 2F(t){RESET}")  
  
  
# Вычислить доверительный интервал  
lower_bound = x_bar - t * sigma / sqrt(n)  
upper_bound = x_bar + t * sigma / sqrt(n)  
  
  
print(f"Критическое значение t: {t} (По таблице Функции Лапласа)")  
print(f"Доверительный интервал: Нижняя граница = {GREEN}{lower_bound}{RESET}, Верхняя граница = {GREEN}{upper_bound}{RESET}")  
  
# 2. Построить график доверительного интервала  
x = np.linspace(lower_bound, upper_bound, 1000)  
y = stats.norm.pdf(x, x_bar, sigma / sqrt(n))  
  
plt.figure(figsize=(10, 6))  
plt.plot(x, y, label='Нормальное распределение')  
plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), color='lightblue', alpha=0.5, label='Доверительный интервал')  
plt.axvline(x=lower_bound, color='red', linestyle='--', label='Нижняя, Верхняя граница')  
plt.axvline(x=upper_bound, color='red', linestyle='--')  
plt.title('Доверительный интервал для математического ожидания')  
plt.xlabel('Значение')  
plt.ylabel('Плотность вероятности')  
plt.legend()  
plt.grid(True)  
plt.show()  
  
print(f"Таким образом, с надежностью {CYAN}{gamma}{RESET} можно утверждать,\nчто доверительный интервал {GREEN}{lower_bound}{RESET} < a < {GREEN}{upper_bound}{RESET} покрывает неизвестный параметр a;\nточность оценки δ = tσ/√n ({YELLOW}{t*sigma/sqrt(n)}{RESET})")  
  
  
