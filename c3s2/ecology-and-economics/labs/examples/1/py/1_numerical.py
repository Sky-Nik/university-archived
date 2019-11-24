#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# проміжок на якому розглядається задачу, 12 місяців = 1 рік
t = np.linspace(0, 12, 1000)

# початкові умови
P10, P20 = 50, 300


# задаємо похідну dP / dt як функцію двох змінних: P і t
def dPdt(P, t):
	return 0.004 * P * (150 - P)


# знаходимо чисельні розв'язки відповідних задач Коші
P1, P2 = odeint(dPdt, P10, t), odeint(dPdt, P20, t)

# побудова графіків
matplotlib.rcParams.update({'font.size': 20})
plt.plot(t, P1, 'r-', label='$P(0) = 50$, numerical')
plt.plot(t, P2, 'b-', label='$P(0) = 300$, numerical')
plt.plot(t, [150 for _ in t], 'g-', label='$P(0) = 150$')
plt.xlabel('$t$, місяців')
plt.ylabel('$P(t)$, особин кролів')
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
