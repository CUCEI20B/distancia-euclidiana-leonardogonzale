from math import sqrt 

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


x_1 = (3)
x_2 = (5)
y_1 = (5)
y_2 = (9)

print(distancia_euclidiana(x_1, y_1, x_2, y_2))
    