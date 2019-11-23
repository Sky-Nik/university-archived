#!usr/bin/env python
from itertools import combinations
from typing import List
from closure import _closure


def _equivalent(l1: List[str], l2: List[str]) -> bool:
	a = set(''.join(l1 + l2)) - set(' -> ')

	for k in range(1, len(a) + 1):
		for f in combinations(a, k):
			f = set(f)

			if _closure(f.copy(), l1.copy()) != _closure(f.copy(), l2.copy()):
				return False

	return True
