import matplotlib.pyplot as plt

horas_estudio = [1, 2, 3, 4, 5, 6]
rendimiento = [50, 55, 65, 70, 80, 90]

plt.figure(figsize=(8,5))
plt.scatter(horas_estudio, rendimiento, color='purple')
plt.xlabel('Horas de estudio')
plt.ylabel('Puntaje del examen')
plt.title('Relación entre horas de estudio y rendimiento')
plt.grid(True)
plt.show()
