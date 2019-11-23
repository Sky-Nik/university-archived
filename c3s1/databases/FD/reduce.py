#!usr/bin/env python
from typing import List
from closure import _closure


def _reduce(l: List[str]) -> List[str]:
	for i in range(len(l)):
		fi, ti = l[i].split(' -> ')

		ti = set(ti)

		mi = l[:i] + l[i + 1:]

		ci = _closure(fi, mi)

		if ci >= ti:
			return _reduce(mi)
		
		if ci & ti:
			tin = sorted(list(ti - ci))
			return _reduce(l[:i] + [fi + ' -> ' + ''.join(tin), ] + l[i + 1:])

	for i in range(len(l)):
		fi, ti = l[i].split(' -> ')
		
		for j in range(len(fi)):
			fij = fi[j]
		
			mi = l[:i] + l[i + 1:]
		
			cij = _closure(set(fi) - {fij}, mi)
		
			if fij in cij:
				fin = sorted(list(set(fi) - {fij}))
				return _reduce(l[:i] + [''.join(fin) + ' -> ' + ti, ] + l[i + 1:])

	for i in range(len(l)):
		fi, ti = l[i].split(' -> ')

		for j in range(len(ti)):
			tij = ti[j]

			mi = l[:i] + l[i + 1:]

			cij = _closure(set(fi) | set(ti) - {tij}, mi)

			if tij in cij:
				tin = sorted(list(set(ti) - {tij}))
				return _reduce(l[:i] + [fi + ' -> ' + ''.join(tin), ] + l[i + 1:])

	return l
