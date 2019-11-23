#!usr/bin/env python
from typing import List, Set


def _closure(s: Set[str] or str, l: List[str], return_set: bool=True) -> Set[str] or str:
	if isinstance(s, str):
		s = set(s)

	ps = set()

	l = list(map(lambda _: tuple(map(set, _.split(' -> '))), l))

	while s != ps:
		ps, nl = s.copy(), []

		for f, t in l:
			if f <= s:
				s |= t
			else:
				nl.append((f, t))

		l = nl.copy()

	return s if return_set else ''.join(sorted(list(s)))
