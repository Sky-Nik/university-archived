#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit, root_scalar
import numpy as np
from typing import Callable


df = pd.DataFrame({
	'price': [1.2, 1.7, 2.5, 2.9, 3.5, 4.2, 4.8, 5.5],
	'demand': [122, 97, 77, 56, 43, 36, 27, 17],
	'supply': [20, 35, 59, 65, 78, 83, 95, 120],
})

p_l, p_r, q_l, q_r = 1, 6, 10, 130


class SupplyLin(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * t + b, 
			df['price'], df['supply'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * t + self.b

	def __repr__(self):
		return f'{self.a:.2f} * t + {self.b:.2f}'


class DemandExp(object):
	def __init__(self, df: pd.DataFrame):
		self.a, self.b = curve_fit(lambda t, a, b: a * np.exp(b * t), 
			df['price'], df['demand'])[0]
	
	def __call__(self, t: float) -> float:
		return self.a * np.exp(self.b * t)

	def __repr__(self):
		return f'{self.a:.2f} * exp({self.b:.2f} * t)'


f = {'supply_lin': SupplyLin(df), 'demand_exp': DemandExp(df)}

price_space = np.arange(1, 6, .01)

df_interp = pd.DataFrame({
	'price': price_space,
	'demand': f['demand_exp'](price_space),
	'supply': f['supply_lin'](price_space),
})

p = root_scalar(lambda t: f['demand_exp'](t) - f['supply_lin'](t), x0=p_l, x1=p_r).root
q = (f['demand_exp'](p) + f['supply_lin'](p)) / 2


plt.figure(figsize=(20,20))
plt.scatter(df['price'], df['demand'], s=100, 
	marker='x', c='r', label='$Q_d(P)$, true')
plt.scatter(df['price'], df['supply'], s=100, 
	marker='x', c='b', label='$Q_s(P)$, true')
plt.plot(df_interp['price'], df_interp['supply'], 
	'b-', label='$Q_s(P)$', zorder=1)
plt.plot(df_interp['price'], df_interp['demand'], 
	'r-', label='$Q_d(P)$', zorder=1)
plt.scatter(p, q, s=100, c='k', label=f'equilibrium, ({p:.2f}, {q:.2f})', zorder=2)
plt.axvline(p, 0, (q - q_l) / (q_r - q_l), c='k', linestyle='--')
plt.axhline(q, 0, (p - p_l) / (p_r - p_l), c='k', linestyle='--')
plt.title('Лінії тренду у вісях $(P, Q)$', fontsize=20)
plt.xlabel('$P$', fontsize=16)
plt.ylabel('$Q$', fontsize=16)
plt.xlim((p_l, p_r))
plt.ylim((q_l, q_r))
plt.legend(loc='right', fontsize=16)
plt.grid(True)
plt.savefig('../tex/p_q.png', bbox_inches='tight')


plt.figure(figsize=(20,20))
plt.scatter(df['demand'], df['price'], s=100, 
	marker='x', c='r', label='$Q_d(P)$, true')
plt.scatter(df['supply'], df['price'], s=100, 
	marker='x', c='b', label='$Q_s(P)$, true')
plt.plot(df_interp['supply'], df_interp['price'], 
	'b-', label='$Q_s(P)$', zorder=1)
plt.plot(df_interp['demand'], df_interp['price'], 
	'r-', label='$Q_d(P)$', zorder=1)
plt.scatter(q, p, s=100, c='k', label=f'equilibrium, ({q:.2f}, {p:.2f})', zorder=2)
plt.axvline(q, 0, (p - p_l) / (p_r - p_l), c='k', linestyle='--')
plt.axhline(p, 0, (q - q_l) / (q_r - q_l), c='k', linestyle='--')
plt.title('Лінії тренду у вісях $(Q, P)$', fontsize=20)
plt.xlabel('$Q$', fontsize=16)
plt.ylabel('$P$', fontsize=16)
plt.xlim((q_l, q_r))
plt.ylim((p_l, p_r))
plt.legend(loc='right', fontsize=16)
plt.grid(True)
plt.show()
# plt.savefig('../tex/q_p.png', bbox_inches='tight')


dotation = .5

df_dot = pd.DataFrame({
	'price': price_space,
	'demand': f['demand_exp'](price_space),
	'supply': f['supply_lin'](price_space + dotation),
})

p = root_scalar(lambda t: f['demand_exp'](t) - f['supply_lin'](t + dotation), 
	x0=p_l, x1=p_r).root
q = (f['demand_exp'](p) + f['supply_lin'](p + dotation)) / 2


plt.figure(figsize=(20,20))
plt.plot(df_dot['supply'], df_dot['price'], 
	'b-', label='$Q_s^{dot}(P)$', zorder=1)
plt.plot(df_dot['demand'], df_dot['price'], 
	'r-', label='$Q_d(P)$', zorder=1)
plt.plot(df_interp['supply'], df_interp['price'], 
	'b--', label='$Q_s(P)$', zorder=1)
plt.scatter(q, p, s=100, c='k', label=f'equilibrium, ({q:.2f}, {p:.2f})', zorder=2)
plt.axvline(q, 0, (p - p_l) / (p_r - p_l), c='k', linestyle='--')
plt.axhline(p, 0, (q - q_l) / (q_r - q_l), c='k', linestyle='--')
plt.title(f'Вплив дотації, $dot={dotation}$', fontsize=20)
plt.xlabel('$Q$', fontsize=16)
plt.ylabel('$P$', fontsize=16)
plt.xlim((q_l, q_r))
plt.ylim((p_l, p_r))
plt.legend(loc='right', fontsize=16)
plt.grid(True)
plt.show()
# plt.savefig('../tex/dotation.png', bbox_inches='tight')
