import matplotlib.pyplot as plt

asignaturas = ['Sitio A', 'Sitio B','Sitio C','Sitio D','Sitio E']
calificaciones = [1.2, 2.5, 0.9, 3.0, 1.8]

plt.figure(figsize=(8,5))
plt.bar(asignaturas, calificaciones, color='skyblue')
plt.xlabel('SITIOS WEB')
plt.ylabel('TIEMPO PROMEDIO')
plt.title('Comparacion dedl tiempo de carga de diferentes paginas web')
plt.ylim(0, 3.5)
plt.show()
