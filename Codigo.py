

import numpy as np

# Coeficientes de las ecuaciones (porcentajes de arena, grano fino y grano grueso)
A = np.array([[52, 20, 25],  # Arena
              [30, 50, 20],  # Grano fino
              [18, 30, 55]]) # Grano grueso

# Requerimientos del ingeniero (4800 de arena, 5810 de grano fino, 5690 de grano grueso)
b = np.array([4800, 5810, 5690])

# Resolver el sistema de ecuaciones Ax = b
x = np.linalg.solve(A, b)

# Mostrar los resultados en el formato requerido
print('Resultados:')
print(f'Cantera 1: {x[0]:.2f} metros^2')
print(f'Cantera 2: {x[1]:.2f} metros^2')
print(f'Cantera 3: {x[2]:.2f} metros^2')
