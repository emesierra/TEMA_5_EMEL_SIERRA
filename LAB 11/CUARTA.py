import matplotlib.pyplot as plt

departamentos = ['Ventas', 'Marketing', 'Ingeniería']
salarios = [
    [4000, 4500, 5000, 5500, 6000],
    [3000, 3500, 4000, 4500, 5000],
    [5000, 6000, 7000, 8000, 9000]
]

plt.figure(figsize=(8,5))
plt.boxplot(salarios, labels=departamentos)
plt.ylabel('Salario')
plt.title('Distribución de salarios por departamento')
plt.grid(True)
plt.show()
