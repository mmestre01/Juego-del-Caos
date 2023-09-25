import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button

# Función para obtener el punto medio
def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Vértices del triángulo equilátero
vertices = [(0, 0), (0.5, (3**0.5)/2), (1, 0)]
xs, ys = [], []

# Función para actualizar el punto en el Juego del caos
def update_point(event):
    global point
    if event.key == ' ':
        iterations = 1
    elif event.key == 'd':
        iterations = 10
    else:
        return
    
    for _ in range(iterations):
        chosen_vertex = random.choice(vertices)
        point = get_midpoint(point, chosen_vertex)
        xs.append(point[0])
        ys.append(point[1])
    ax.clear()
    ax.plot([vertices[0][0], vertices[1][0], vertices[2][0], vertices[0][0]],
            [vertices[0][1], vertices[1][1], vertices[2][1], vertices[0][1]], 'g-')  # Dibuja el triángulo
    ax.scatter(xs, ys, s=1, color='blue')
    ax.axis('equal')
    plt.draw()

fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', update_point)
# Dibujar el triángulo equilátero
ax.plot([vertices[0][0], vertices[1][0], vertices[2][0], vertices[0][0]],
        [vertices[0][1], vertices[1][1], vertices[2][1], vertices[0][1]], 'g-')
# Punto inicial elegido por el usuario
print("Por favor, haz clic en un punto dentro del triángulo para elegir el punto inicial.")
point = plt.ginput(1)[0]
xs.append(point[0])
ys.append(point[1])



ax.scatter(xs, ys, s=1, color='blue')
ax.axis('equal')
plt.show()
