#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Tuple

a, b, c, d, e = 10, 25, 20, 30, 10


def dxdt(x: float, y: float) -> float:
	return x * (a - b * y - e * x)


def dydt(x: float, y: float) -> float:
	return y * (d * x - c)


def f(x: float, y: float) -> Tuple[float, float]:
	return dxdt(x, y), dydt(x, y)


x_s, y_s = c / d, (a - c * e / d) / b

h = 0.01

t = np.arange(0, 2 + h, h)


def k1(x: float, y: float) -> Tuple[float, float]:
	return f(x, y)


def k2(x: float, y: float) -> Tuple[float, float]:
	k1x, k1y = k1(x, y)
	return f(x + (h / 2) * k1x, y + (h / 2) * k1y)


def k3(x: float, y: float) -> Tuple[float, float]:
	k2x, k2y = k2(x, y)
	return f(x + (h / 2) * k2x, y + (h / 2) * k2y)


def k4(x: float, y: float) -> Tuple[float, float]:
	k3x, k3y = k3(x, y)
	return f(x + h * k3x, y + h * k3y)


def rk(x: float, y: float) -> Tuple[float, float]:
	k1x, k1y = k1(x, y)
	k2x, k2y = k2(x, y)
	k3x, k3y = k3(x, y)
	k4x, k4y = k4(x, y)
	return x + (h / 6) * (k1x + 2 * k2x + 2 * k3x + k4x), \
		y + (h / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)


def plot_2d(x0: float, y0: float) -> None:
	x, y = [x0], [y0]

	for _ in range(len(t) - 1):
		_x, _y = rk(x[-1], y[-1])
		x.append(_x)
		y.append(_y)

	plt.figure(figsize=(20,10))

	plt.plot(t, x, 'b-', label=f'$x(t), x(0) = {x0:.2f}$')
	plt.plot(t, y, 'r-', label=f'$y(t), y(0) = {y0:.2f}$')

	plt.plot(t, [x_s for _ in t], 'b--', label=f'$x(t), x(0) = {x_s:.2f}$')
	plt.plot(t, [y_s for _ in t], 'r--', label=f'$y(t), y(0) = {y_s:.2f}$')

	plt.title(f'Solution plots with Runge-Kutta on $[{t[0]}, {t[-1]}]$\n'
		f'$x(0) = {x0:.2f}, y(0) = {y0:.2f}$', fontsize=20)
	
	plt.xlabel('$t$', fontsize=16)
	plt.ylabel('$x, y$', fontsize=16)

	plt.ylim(0, 1.25)

	plt.legend()

	plt.savefig(f'../tex/plot_2d_{x0:.2f}_{y0:.2f}_2.png')


def plot_3d(x0: float, y0: float) -> None:
	x, y = [x0], [y0]

	for _ in range(len(t) - 1):
		_x, _y = rk(x[-1], y[-1])
		x.append(_x)
		y.append(_y)

	fig = plt.figure(figsize=(10,10))

	ax = fig.gca(projection='3d')

	ax.plot(x, y, t, 'g-', label=f'$x(0) = {x0:.2f}, y(0) = {y0:.2f}$')

	ax.plot([x_s for _ in t], [y_s for _ in t], t, 'k--',
		label=f'$x(0) = {x_s:.2f}, y(0) = {y_s:.2f}$')
	
	ax.set_xlim3d(0, 1.25)
	ax.set_ylim3d(0, 1.25)

	plt.title(f'Solution plot with Runge-Kutta on $[{t[0]}, {t[-1]}]$\n'
		f'$x(0) = {x0:.2f}, y(0) = {y0:.2f}$', fontsize=20)

	ax.set_xlabel('$x(t)$', fontsize=16)
	ax.set_ylabel('$y(t)$', fontsize=16)
	ax.set_zlabel('$t$', fontsize=16)

	plt.savefig(f'../tex/plot_3d_{x0:.2f}_{y0:.2f}_2.png')


for x0, y0 in [(.9, .1), (.5, .5), (.1, .9)]:
	plot_2d(x0, y0)
	plot_3d(x0, y0)
