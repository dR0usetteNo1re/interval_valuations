# Известные данные
n = 19
k = 19 - 1 # Кол-во степеней свободы
S = 25 # Человек, Исправленное Среднеквадратичное отклонение.
gamma = 0.90 # Надежность

x_2_lower = 28.9
x_2_upper = 9.39 # По таблице Фишера = 1 - gamma / 2 = 0.95; т.к. степень свободны = 18

lower_int = sqrt(((n - 1) * S**2) / x_2_lower)
upper_int = sqrt(((n - 1) * S**2) / x_2_upper)

print(lower_int, upper_int)

# Строим интервал
x = np.linspace(lower_int, upper_int, 1000)
y = stats.norm.pdf(x, S, S / sqrt(n))

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Нормальное распределение')
plt.fill_between(x, y, where=(x >= lower_int) & (x <= upper_int), color='lightgreen', alpha=0.5,
                 label='Доверительный интервал')
plt.axvline(x=lower_int, color='red', linestyle='--', label='Нижняя, Верхняя граница')
plt.axvline(x=upper_int, color='red', linestyle='--')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()

print(f"Таким образом, с надежностью {CYAN}{gamma}{RESET} можно утверждать,\nчто доверительный интервал {YELLOW}{lower_int}{RESET} < a < {YELLOW}{upper_int}{RESET} покрывает неизвестный параметр a.")
