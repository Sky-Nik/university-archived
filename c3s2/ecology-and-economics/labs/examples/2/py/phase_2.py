#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = 10, 25, 20, 30, 10


def dxdt(x: float, y: float) -> float:
	return x * (a - b * y - e * x)


def dydt(x: float, y: float) -> float:
	return y * (d * x - c)


delta = .1

s = 50

x_s, y_s = c / d, (a - c * e / d) / b

for x_l, x_r, y_l, y_r in [(0.01, 1, 0.01, 1), 
	(x_s - delta, x_s + delta, y_s - delta, y_s + delta)]:
	x_space, y_space = np.meshgrid(np.arange(x_l, x_r, (x_r - x_l) / s), 
		np.arange(y_l, y_r, (y_r - y_l) / s))

	u = np.array([[dxdt(x_space[i, j], y_space[i, j]) \
		for j in range(x_space.shape[1])] for i in range(x_space.shape[0])])

	v = np.array([[dydt(x_space[i, j], y_space[i, j]) \
		for j in range(x_space.shape[1])] for i in range(x_space.shape[0])])

	plt.figure(figsize=(20,20))

	plt.title(f'Phase portrait on $[{x_l:.2f}, {x_r:.2f}] '
		f'\\times [{y_l:.2f}, {y_r:.2f}]$', fontsize=20)
	
	plt.xlabel('$x$', fontsize=16)
	plt.ylabel('$y$', fontsize=16)

	plt.quiver(x_space, y_space, u, v, np.hypot(u, v))

	plt.scatter(x_s, y_s, s=100, c='k', label=f'Stationary point:\n'
		f'$x = {x_s:.2f}, y = {y_s:.2f}$.')

	plt.legend()

	plt.savefig(f'../tex/phase_{x_l:.2f}_{x_r:.2f}_{y_l:.2f}_{y_r:.2f}_{s}_2.png')
