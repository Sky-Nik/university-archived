#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 12, 1000)


def P(t, c):
    return 150 * np.exp(0.6 * t) / (np.exp(0.6 * t) + c)


def P1(t):
    return P(t, 2)


def P2(t):
    return P(t, -.5)


matplotlib.rcParams.update({'font.size': 20})
plt.plot(t, P1(t), 'r-', label='$P(0) = 50$, analytical')
plt.plot(t, P2(t), 'b-', label='$P(0) = 300$, analytical')
plt.plot(t, [150 for _ in t], 'g-', label='$P(0) = 150$')
plt.xlabel('$t$, місяців')
plt.ylabel('$P(t)$, особин кролів')
plt.legend()
plt.grid(True)
plt.get_current_fig_manager().full_screen_toggle() 
plt.show()
