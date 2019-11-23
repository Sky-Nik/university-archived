#!usr/bin/env python
import unittest
from reduce import _reduce


class TestReduce(unittest.TestCase):
	def test01(self):
		self.assertEqual(
			_reduce(
				l=[
					'DF -> B',
					'A -> BC',
					'BCF -> D',
					'A -> D',
					'D -> F',
				]
			),
			[
				'D -> B',
				'A -> C',
				'BCF -> D',
				'A -> D',
				'D -> F',
			]
		)


	def test02(self):
		self.assertEqual(
			_reduce(
				l=[
					'AC -> D',
					'AD -> EF',
					'E -> ACD',
					'AF -> DB',
				]
			),
			[
				'AC -> D',
				'AD -> EF',
				'E -> AC',
				'AF -> DB',
			]
		)


	def test03(self):
		self.assertEqual(
			_reduce(
				l=[
					'X -> TZ',
					'TZ -> Y',
					'Y -> TU',
					'YU -> T',
				]
			),
			[
				'X -> TZ',
				'TZ -> Y',
				'Y -> TU',
			]
		)


	def test04(self):
		self.assertEqual(
			_reduce(
				l=[
					'K -> L',
					'LM -> KN',
					'LN -> MP',
					'P -> KL',
					'N -> P',
				]
			),
			[
				'K -> L',
				'LM -> N',
				'N -> M',
				'P -> K',
				'N -> P',
			]
		)


	def test05(self):
		self.assertEqual(
			_reduce(
				l=[
					'X -> TZ',
					'Z -> YU',
					'ST -> YZ',
					'Y -> US',
					'S -> ZU',
				]
			),
			[
				'X -> TZ',
				'Z -> Y',
				'Y -> S',
				'S -> ZU',
			]
		)


	def test06(self):
		self.assertEqual(
			_reduce(
				l=[
					'AFE -> BC',
					'A -> D',
					'D -> BE',
					'BD -> AF',
				]
			),
			[
				'A -> C',
				'A -> D',
				'D -> BE',
				'D -> AF',
			]
		)


	def test07(self):
		self.assertEqual(
			_reduce(
				l=[
					'A -> CD',
					'D -> C',
					'BC -> AD',
					'AC -> B',
					'C -> AD',
				]
			),
			[
				'A -> D',
				'D -> C',
				'C -> B',
				'C -> A',
			]
		)


	def test08(self):
		self.assertEqual(
			_reduce(
				l=[
					'C -> BF',
					'BF -> D',
					'D -> E',
					'DE -> F',
					'C -> EF',
				]
			),
			[
				'C -> B',
				'BF -> D',
				'D -> E',
				'D -> F',
				'C -> F',
			]
		)


	def test09(self):
		self.assertEqual(
			_reduce(
				l=[
					'AD -> C',
					'C -> DF',
					'BE -> A',
					'D -> BF',
					'FD -> AC',
				]
			),
			[
				'C -> DF',
				'BE -> A',
				'D -> B',
				'D -> AC',
			]
		)


	def test10(self):
		self.assertEqual(
			_reduce(
				l=[
					'AB -> F',
					'E -> CD',
					'ABC -> DE',
					'AD -> CF',
					'F -> E',
				]
			),
			[
				'AB -> F',
				'E -> CD',
				'AD -> F',
				'F -> E',
			]
		)


	def test11(self):
		self.assertEqual(
			_reduce(
				l=[
					'X -> ZYU',
					'Z -> XS',
					'UY -> ZT',
					'XY -> S',
				]
			),
			[
				'X -> UY',
				'Z -> XS',
				'UY -> ZT',
			]
		)


	def test12(self):
		self.assertEqual(
			_reduce(
				l=[
					'ST -> YZ',
					'Z -> UX',
					'XT -> S',
					'X -> TZS',
				]
			),
			[
				'ST -> YZ',
				'Z -> UX',
				'X -> ST',
			]
		)


if __name__ == '__main__':
	unittest.main()
