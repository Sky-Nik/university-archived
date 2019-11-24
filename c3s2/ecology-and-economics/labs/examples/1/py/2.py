#!/usr/bin/env python -W ignore
import numpy as np

# матриця Леслі
L = np.array([
	[  0,   6, 15],
	[0.5,   0,  0],
	[  0, 0.5,  0]
])

# початковий розподіл популяції
x0 = np.array([1, 1, 1])

# розподіл через t = 5 кроків обчислюємо як L^t * x0
t = 5
xt = np.dot(np.linalg.matrix_power(L, t), x0)
print(f'x({t}) = {xt}')  # x(5) = [239.625   55.125   16.6875]

# знаходимо власні значення і власні вектори
_lambda, x = np.linalg.eig(L)
# знаходимо найбільше додатне власне значення
lambda_L = np.max(_lambda)

print(f'lambda_L = {np.float_(lambda_L)}')  # lambda_L = 2.173738392044369

# знаходимо власний вектор що йому відповідає
x_L = x[:, _lambda == lambda_L].T[0] 
# нормуємо цей вектор в || ||_1 нормі
x_L /= np.linalg.norm(x_L, 1)

print(f'x_L = {np.abs(np.float_(x_L))}')  # x_L = [0.77946759 0.17929195 0.04124046]

# знаходимо min t: ||x(t)||_1 > 75
t = 0
while np.sum(x0) <= 75:
	x0 = np.dot(L, x0)
	t += 1

print(f't = {t}, X({t}) = {np.sum(x0)}')  # t = 3, X(3) = 77.25
