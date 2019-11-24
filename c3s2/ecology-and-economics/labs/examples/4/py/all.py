#!/usr/bin/env python
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, minimize


df = pd.DataFrame({
	'capital': [2860, 2740, 2950, 2880, 2510, 2690, 2990, 2850, 3000, 3070],
	'labor': [10680, 10310, 10680, 10800, 10540, 10420, 10940, 10710, 9900, 9930],
	'production': [49920, 47750, 50550, 50570, 47820, 47900, 51900, 45970, 48030, 48100],
})

df[[0, 1]] = df[['capital', 'labor']]


class ProductionFunction(object):
	def __init__(self, df: pd.DataFrame):
		self.A, self.a = curve_fit(
			lambda cl, A, a: A * cl['capital']**a * cl['labor']**(1 - a), 
			df[['capital','labor']], df['production']
		)[0]
	
	def __call__(self, cl) -> float:
		# cl[0] = cl['capital'], cl[1] = cl['labor']
		return self.A * cl[0]**self.a * cl[1]**(1 - self.a)

	def __repr__(self):
		return f'{self.A:.2f} * K^{self.a:.2f} * L^{1 - self.a:.2f}'


production_function = ProductionFunction(df)

print(production_function)

p, w_1, w_2 = 5, 2, 3


def cost(cl) -> float:
	# cl[0] = cl['capital'], cl[1] = cl['labor']
	return w_1 * cl[0] + w_2 * cl[1]


def profit(cl) -> float:
	return p * production_function(cl) - cost(cl)


def minus_profit(cl) -> float:
	return -profit(cl)


def minus_production_function(cl) -> float:
	return -production_function(cl)


# region limited cost, maximal profit
TC = 100_000

cl_star_1 = minimize(
	minus_profit, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'ineq', 'fun': lambda cl: cost(cl)},
		{'type': 'ineq', 'fun': lambda cl: TC - cost(cl)},
	)
)['x']

print(
	'limited cost, maximal profit:\n'
	f'	        cl_star  = {cl_star_1}\n'
	f'	   cost(cl_star) = {cost(cl_star_1)}\n'
	f'	product(cl_star) = {production_function(cl_star_1)}\n'
	f'	 profit(cl_star) = {profit(cl_star_1)}\n'
)
# enregion

# region limited cost, maximal production
cl_star_2 = minimize(
	minus_production_function, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'ineq', 'fun': lambda cl: cost(cl)},
		{'type': 'ineq', 'fun': lambda cl: TC - cost(cl)},
	)
)['x']

print(
	'limited cost, maximal production:\n'
	f'	        cl_star  = {cl_star_2}\n'
	f'	   cost(cl_star) = {cost(cl_star_2)}\n'
	f'	product(cl_star) = {production_function(cl_star_2)}\n'
	f'	 profit(cl_star) = {profit(cl_star_2)}\n'
)
# enregion

# region fixed production, minimal cost
q_0 = 55_000

cl_star_3 = minimize(
	cost, 
	x0=(10_000, 10_000), 
	constraints=(
		{'type': 'eq', 'fun': lambda cl: production_function(cl) - q_0},
	)
)['x']

print(
	'fixed production, minimal cost:\n'
	f'	        cl_star  = {cl_star_3}\n'
	f'	   cost(cl_star) = {cost(cl_star_3)}\n'
	f'	product(cl_star) = {production_function(cl_star_3)}\n'
	f'	 profit(cl_star) = {profit(cl_star_3)}\n'
)
# enregion