#!/usr/bin/env python
import numpy as np
import unittest
from typing import Callable, Tuple


def von_neumann(x_0: np.array, z_0: np.array, proj_c: Callable[[np.array], np.array], 
        proj_d: Callable[[np.array], np.array], eps: float=1e-5) -> Tuple[np.array, int]:
    """
    Classical von Neumann alternating projections method.
    
    Consists of iterations of the form:

        x^{k + 1} := proj_c(z^k)
        z^{k + 1} := proj_d(x^{k + 1})
    
    :param x_0: starting point (in C)
    :param z_0: starting point (in D)
    :param proj_c: function able to project points onto C
    :param proj_d: function able to project points onto D
    :param eps desired precision
    :return: a point y = (z^k + x^k) / 2 with k sufficiently large 
        for both d(y, C) < eps / 2 and d(y, D) < eps / 2 to hold simultaneously,
        and the value of k, i.e. the number of iterations
    """
    assert x_0.shape == z_0.shape, "x_0 and z_0 should be of the same shape"

    k, x_k, z_k = 0, np.copy(x_0), np.copy(z_0)
    z_k += np.repeat(eps, x_0.shape)

    while np.linalg.norm(x_k - z_k, 2) >= eps:
        x_k = proj_c(z_k)
        z_k = proj_d(x_k)
        k += 1

    return (x_k + z_k) / 2, k


def dijkstra(x_0: np.array, z_0: np.array, proj_c: Callable[[np.array], np.array], 
        proj_d: Callable[[np.array], np.array], eps: float=1e-5) -> Tuple[np.array, int]:
    """
    ADMM + von Neumann = Dijkstra alternating projections method.
    
    Consists of iterations of the form:

        x^{k + 1} := proj_c(z^k - u^k)
        z^{k + 1} := proj_d(x^{k + 1} + u^k)
        u^{k + 1} := u^k + x^{K + 1} - z^{k + 1}
    
    :param x_0: starting point (in C)
    :param z_0: starting point (in D)
    :param proj_c: function able to project points onto C
    :param proj_d: function able to project points onto D
    :param eps desired precision
    :return: a point y = (z^k + x^k) / 2 with k sufficiently large 
        for both d(y, C) < eps / 2 and d(y, D) < eps / 2 to hold simultaneously,
        and the value of k, i.e. the number of iterations
    """
    assert x_0.shape == z_0.shape, "x_0 and z_0 should be of the same shape"

    k, x_k, z_k = 0, np.copy(x_0), np.copy(z_0)
    z_k += np.repeat(eps, x_0.shape)
    u_k = np.repeat(eps, x_0.shape)

    while np.linalg.norm(x_k - z_k, 2) >= eps:
        x_k = proj_c(z_k - u_k)
        z_k = proj_d(x_k + u_k)
        u_k += x_k - z_k
        k += 1

    return (x_k + z_k) / 2, k


class Test(unittest.TestCase):
    def test(self):
        for dimensionality in range(2, 9):
            print(f'\nDimensionality = {dimensionality}:')
            with self.subTest(i=dimensionality):
                x_0 = np.zeros(dimensionality)
                z_0 = np.zeros(dimensionality)      

                # C is <x, c> = 1.
                c = np.random.random(dimensionality)
                c /= np.linalg.norm(c, 2)
                
                # D is <x, d> = 1.
                d = np.random.random(dimensionality)
                d /= np.linalg.norm(d, 2)

                def proj_c(x: np.array) -> np.array:
                    return x - (np.dot(c, x) - 1.) * c

                def proj_d(x: np.array) -> np.array:
                    return x - (np.dot(d, x) - 1.) * d

                eps = 1e-5

                y, k = von_neumann(x_0, z_0, proj_c, proj_d, eps)

                print(f'von Neumann: y_{k} = {y}')

                x_k, z_k = proj_c(y), proj_d(y)
                d_c, d_d = np.linalg.norm(x_k - y, 2), np.linalg.norm(z_k - y, 2)

                self.assertLess(d_c, eps / 2)
                self.assertLess(d_d, eps / 2)

                y, k = dijkstra(x_0, z_0, proj_c, proj_d, eps)

                print(f'DiJkstra   : y_{k} = {y}')

                x_k, z_k = proj_c(y), proj_d(y)
                d_c, d_d = np.linalg.norm(x_k - y, 2), np.linalg.norm(z_k - y, 2)

                self.assertLess(d_c, eps / 2)
                self.assertLess(d_d, eps / 2)


if __name__ == "__main__":
    np.set_printoptions(linewidth=120)
    np.random.seed(65537)
    unittest.main()
