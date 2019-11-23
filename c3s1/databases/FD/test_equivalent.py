#!usr/bin/env python
import unittest
from reduce import _reduce
from equivalent import _equivalent


class TestEquivalent(unittest.TestCase):
	def test01(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'DF -> B', 
						'A -> BC', 
						'BCF -> D', 
						'A -> D', 
						'D -> F',
					]
				),
				l2=[
					'D -> B', 
					'A -> C', 
					'BCF -> D', 
					'A -> D', 
					'D -> F',
				]
			)
		)


	def test02(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AC -> D', 
						'AD -> EF', 
						'E -> ACD', 
						'AF -> DB',
					]
				),
				l2=[
					'AC -> D', 
					'AD -> EF', 
					'E -> ACD', 
					'AF -> DB',
				]
			)
		)


	def test03(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'TZ -> Y', 
						'Y -> TU',
						'YU -> T',
					]
				),
				l2=[
					'X -> TZ', 
					'TZ -> Y', 
					'Y -> TU',
				]
			)
		)


	def test04(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'K -> L', 
						'LM -> KN', 
						'LN -> MP', 
						'P -> KL', 
						'N -> P',
					]
				),
				l2=[
					'K -> L', 
					'LM -> KN', 
					'N -> M', 
					'P -> KL', 
					'N -> P',
				]
			)
		)


	def test05(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'Z -> YU', 
						'ST -> YZ', 
						'Y -> US', 
						'S -> ZU',
					]
				),
				l2=[
					'X -> TZ', 
					'Z -> YU', 
					'Y -> US', 
					'S -> ZU',
				]
			)
		)


	def test06(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AFE -> BC', 
						'A -> D', 
						'D -> BE', 
						'BD -> AF',
					]
				),
				l2=[
					'A -> C', 
					'A -> D', 
					'D -> BE', 
					'D -> AF',
				]
			)
		)


	def test07(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> CD', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[
					'A -> CD', 
					'D -> C', 
					'A -> B', 
					'C -> AD',
				]
			)
		)


	def test08(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'C -> BF', 
						'BF -> D', 
						'D -> E', 
						'DE -> F', 
						'C -> EF',
					]
				),
				l2=[
					'C -> B', 
					'BF -> D', 
					'D -> E', 
					'D -> F', 
					'C -> EF',
				]
			)
		)


	def test09(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AD -> C', 
						'C -> DF', 
						'BE -> A', 
						'D -> BF', 
						'FD -> AC',
					]
				),
				l2=[
					'C -> DF', 
					'BE -> A', 
					'D -> B', 
					'D -> AC',
				]
			)
		)


	def test10(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AB -> F', 
						'E -> CD', 
						'ABC -> DE', 
						'AD -> CF', 
						'F -> E',
					]
				),
				l2=[
					'AB -> F', 
					'E -> CD', 
					'AD -> CF', 
					'F -> E',
				]
			)
		)


	def test11(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZYU', 
						'Z -> XS', 
						'UY -> ZT', 
						'XY -> S',
					]
				),
				l2=[
					'X -> ZYU', 
					'Z -> XS', 
					'UY -> ZT',
				]
			)
		)


	def test12(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'ST -> YZ', 
						'Z -> UX', 
						'XT -> S', 
						'X -> TZS',
					]
				),
				l2=[
					'ST -> YZ', 
					'Z -> UX', 
					'X -> TZS',
				]
			)
		)


	def test13(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'DF -> B', 
						'A -> BC', 
						'BCF -> D', 
						'A -> D', 
						'D -> F',
					]
				),
				l2=[
					'A -> C', 
					'BCF -> D', 
					'A -> D', 
					'D -> F',
				]
			)
		)


	def test14(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AC -> D', 
						'AD -> EF', 
						'E -> ACD', 
						'AF -> DB',
					]
				),
				l2=[
					'AD -> EF', 
					'E -> ACD', 
					'AF -> DB',
				]
			)
		)


	def test15(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'TZ -> Y', 
						'Y -> TU', 
						'YU -> T',
					]
				),
				l2=[
					'TZ -> Y', 
					'Y -> TU',
				]
			)
		)


	def test16(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'K -> L', 
						'LM -> KN', 
						'LN -> MP', 
						'P -> KL', 
						'N -> P',
					]
				),
				l2=[
					'LM -> KN', 
					'N -> M', 
					'P -> KL', 
					'N -> P',
				]
			)
		)


	def test17(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'Z -> YU', 
						'ST -> YZ', 
						'Y -> US', 
						'S -> ZU',
					]
				),
				l2=[
					'Z -> YU', 
					'Y -> US', 
					'S -> ZU',
				]
			)
		)


	def test18(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AFE -> BC', 
						'A -> D', 
						'D -> BE', 
						'BD -> AF',
					]
				),
				l2=[
					'A -> D', 
					'D -> BE', 
					'D -> AF',
				]
			)
		)


	def test19(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> CD', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[
					'D -> C', 
					'A -> B', 
					'C -> AD',
				]
			)
		)


	def test20(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'C -> BF', 
						'BF -> D', 
						'D -> E', 
						'DE -> F', 
						'C -> EF',
					]
				),
				l2=[
					'BF -> D', 
					'D -> E', 
					'D -> F', 
					'C -> EF',
				]
			)
		)


	def test21(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AD -> C', 
						'C -> DF', 
						'BE -> A', 
						'D -> BF', 
						'FD -> AC',
					]
				),
				l2=[
					'BE -> A', 
					'D -> B', 
					'D -> AC',
				]
			)
		)


	def test22(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AB -> F', 
						'E -> CD', 
						'ABC -> DE', 
						'AD -> CF', 
						'F -> E',
					]
				),
				l2=[
					'E -> CD', 
					'AD -> CF', 
					'F -> E',
				]
			)
		)


	def test23(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZYU', 
						'Z -> XS', 
						'UY -> ZT', 
						'XY -> S',
					]
				),
				l2=[
					'Z -> XS', 
					'UY -> ZT',
				]
			)
		)


	def test24(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'ST -> YZ', 
						'Z -> UX', 
						'XT -> S', 
						'X -> TZS',
					]
				),
				l2=[
					'Z -> UX', 
					'X -> TZS',
				]
			)
		)


	def test25(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'DF -> B', 
						'A -> BC', 
						'BCF -> D', 
						'A -> D', 
						'D -> F',
					]
				),
				l2=[
					'D -> B', 
					'A -> C', 
					'CF -> D', 
					'A -> D', 
					'D -> F',
				]
			)
		)


	def test26(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AC -> D', 
						'AD -> EF', 
						'E -> ACD', 
						'AF -> DB',
					]
				),
				l2=[
					'C -> D', 
					'AD -> EF', 
					'E -> ACD', 
					'AF -> DB',
				]
			)
		)


	def test27(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'TZ -> Y', 
						'Y -> TU', 
						'YU -> T',
					]
				),
				l2=[
					'X -> Z', 
					'TZ -> Y', 
					'Y -> TU',
				]
			)
		)


	def test28(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'K -> L', 
						'LM -> KN', 
						'LN -> MP', 
						'P -> KL', 
						'N -> P',
					]
				),
				l2=[
					'K -> L', 
					'M -> KN', 
					'N -> M', 
					'P -> KL', 
					'N -> P',
				]
			)
		)


	def test29(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'Z -> YU', 
						'ST -> YZ', 
						'Y -> US', 
						'S -> ZU',
					]
				),
				l2=[
					'X -> Z', 
					'Z -> YU', 
					'Y -> US', 
					'S -> ZU',
				]
			)
		)


	def test30(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AFE -> BC', 
						'A -> D', 
						'D -> BE', 
						'BD -> AF',
					]
				),
				l2=[
					'A -> C', 
					'A -> D', 
					'D -> E', 
					'D -> AF',
				]
			)
		)


	def test31(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> CD', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[
					'A -> D', 
					'D -> C', 
					'A -> B', 
					'C -> AD',
				]
			)
		)


	def test32(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'C -> BF', 
						'BF -> D', 
						'D -> E', 
						'DE -> F', 
						'C -> EF',
					]
				),
				l2=[
					'C -> B', 
					'F -> D', 
					'D -> E', 
					'D -> F', 
					'C -> EF',
				]
			)
		)


	def test33(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AD -> C', 
						'C -> DF', 
						'BE -> A', 
						'D -> BF', 
						'FD -> AC',
					]
				),
				l2=[
					'C -> F', 
					'BE -> A', 
					'D -> B', 
					'D -> AC',
				]
			)
		)


	def test34(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'AB -> F', 
						'E -> CD', 
						'ABC -> DE', 
						'AD -> CF', 
						'F -> E',
					]
				),
				l2=[
					'B -> F', 
					'E -> CD', 
					'AD -> CF', 
					'F -> E',
				]
			)
		)


	def test35(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZYU', 
						'Z -> XS', 
						'UY -> ZT', 
						'XY -> S',
					]
				),
				l2=[
					'X -> U', 
					'Z -> XS', 
					'UY -> ZT',
				]
			)
		)


	def test36(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'ST -> YZ', 
						'Z -> UX', 
						'XT -> S', 
						'X -> TZS',
					]
				),
				l2=[
					'T -> YZ', 
					'Z -> UX', 
					'X -> TZS',
				]
			)
		)


	def test37(self):
		self.assertFalse(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> CD', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[
					'A -> CD', 
					'D -> C', 
					'A -> B', 
					'C -> D',
				]
			)
		)


	def test38(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'DF -> B', 
						'A -> BC', 
						'BCF -> D', 
						'A -> D', 
						'D -> F',
					]
				),
				l2=[
					'A -> C', 
					'D -> B', 
					'BCF -> D', 
					'A -> D', 
					'D -> F',
				]
			)
		)


	def test39(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AC -> D', 
						'AD -> EF', 
						'E -> ACD', 
						'AF -> DB',
					]
				),
				l2=[
					'AD -> EF',
					'AC -> D',  
					'E -> ACD', 
					'AF -> DB',
				]
			)
		)


	def test40(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'TZ -> Y', 
						'Y -> TU',
						'YU -> T',
					]
				),
				l2=[
					'TZ -> Y', 
					'X -> TZ', 
					'Y -> TU',
				]
			)
		)


	def test41(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'K -> L', 
						'LM -> KN', 
						'LN -> MP', 
						'P -> KL', 
						'N -> P',
					]
				),
				l2=[
					'LM -> KN',
					'K -> L',  
					'N -> M', 
					'P -> KL', 
					'N -> P',
				]
			)
		)


	def test42(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> TZ', 
						'Z -> YU', 
						'ST -> YZ', 
						'Y -> US', 
						'S -> ZU',
					]
				),
				l2=[
					'Z -> YU', 
					'X -> TZ', 
					'Y -> US', 
					'S -> ZU',
				]
			)
		)


	def test43(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AFE -> BC', 
						'A -> D', 
						'D -> BE', 
						'BD -> AF',
					]
				),
				l2=[
					'A -> D', 
					'A -> C', 
					'D -> BE', 
					'D -> AF',
				]
			)
		)


	def test44(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> CD', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[ 
					'D -> C', 
					'A -> CD',
					'A -> B', 
					'C -> AD',
				]
			)
		)


	def test45(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'C -> BF', 
						'BF -> D', 
						'D -> E', 
						'DE -> F', 
						'C -> EF',
					]
				),
				l2=[
					'BF -> D', 
					'C -> B', 
					'D -> E', 
					'D -> F', 
					'C -> EF',
				]
			)
		)


	def test46(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AD -> C', 
						'C -> DF', 
						'BE -> A', 
						'D -> BF', 
						'FD -> AC',
					]
				),
				l2=[
					'BE -> A', 
					'C -> DF', 
					'D -> B', 
					'D -> AC',
				]
			)
		)


	def test47(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'AB -> F', 
						'E -> CD', 
						'ABC -> DE', 
						'AD -> CF', 
						'F -> E',
					]
				),
				l2=[
					'E -> CD', 
					'AB -> F', 
					'AD -> CF', 
					'F -> E',
				]
			)
		)


	def test48(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZYU', 
						'Z -> XS', 
						'UY -> ZT', 
						'XY -> S',
					]
				),
				l2=[
					'Z -> XS', 
					'X -> ZYU', 
					'UY -> ZT',
				]
			)
		)


	def test49(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'ST -> YZ', 
						'Z -> UX', 
						'XT -> S', 
						'X -> TZS',
					]
				),
				l2=[ 
					'Z -> UX', 
					'ST -> YZ',
					'X -> TZS',
				]
			)
		)


	def test50(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'FD -> B', 
						'A -> BC', 
						'BCF -> D', 
						'A -> D', 
						'D -> F',
					]
				),
				l2=[
					'D -> B', 
					'A -> C', 
					'BCF -> D', 
					'A -> D', 
					'D -> F',
				]
			)
		)


	def test51(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'CA -> D', 
						'AD -> EF', 
						'E -> ACD', 
						'AF -> DB',
					]
				),
				l2=[
					'AC -> D', 
					'AD -> EF', 
					'E -> ACD', 
					'AF -> DB',
				]
			)
		)


	def test52(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZT', 
						'TZ -> Y', 
						'Y -> TU',
						'YU -> T',
					]
				),
				l2=[
					'X -> TZ', 
					'TZ -> Y', 
					'Y -> TU',
				]
			)
		)


	def test53(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'K -> L', 
						'ML -> KN', 
						'LN -> MP', 
						'P -> KL', 
						'N -> P',
					]
				),
				l2=[
					'K -> L', 
					'LM -> KN', 
					'N -> M', 
					'P -> KL', 
					'N -> P',
				]
			)
		)


	def test54(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> ZT', 
						'Z -> YU', 
						'ST -> YZ', 
						'Y -> US', 
						'S -> ZU',
					]
				),
				l2=[
					'X -> TZ', 
					'Z -> YU', 
					'Y -> US', 
					'S -> ZU',
				]
			)
		)


	def test55(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'EFA -> BC', 
						'A -> D', 
						'D -> BE', 
						'BD -> AF',
					]
				),
				l2=[
					'A -> C', 
					'A -> D', 
					'D -> BE', 
					'D -> AF',
				]
			)
		)


	def test56(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'A -> DC', 
						'D -> C', 
						'BC -> AD', 
						'AC -> B', 
						'C -> AD',
					]
				),
				l2=[
					'A -> CD', 
					'D -> C', 
					'A -> B', 
					'C -> AD',
				]
			)
		)


	def test57(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'C -> FB', 
						'BF -> D', 
						'D -> E', 
						'DE -> F', 
						'C -> EF',
					]
				),
				l2=[
					'C -> B', 
					'BF -> D', 
					'D -> E', 
					'D -> F', 
					'C -> EF',
				]
			)
		)


	def test58(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'DA -> C', 
						'C -> DF', 
						'BE -> A', 
						'D -> BF', 
						'FD -> AC',
					]
				),
				l2=[
					'C -> DF', 
					'BE -> A', 
					'D -> B', 
					'D -> AC',
				]
			)
		)


	def test59(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'BA -> F', 
						'E -> CD', 
						'ABC -> DE', 
						'AD -> CF', 
						'F -> E',
					]
				),
				l2=[
					'AB -> F', 
					'E -> CD', 
					'AD -> CF', 
					'F -> E',
				]
			)
		)


	def test60(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'X -> UYZ', 
						'Z -> XS', 
						'UY -> ZT', 
						'XY -> S',
					]
				),
				l2=[
					'X -> ZYU', 
					'Z -> XS', 
					'UY -> ZT',
				]
			)
		)


	def test61(self):
		self.assertTrue(
			_equivalent(
				l1=_reduce(
					l=[
						'TS -> YZ', 
						'Z -> UX', 
						'XT -> S', 
						'X -> TZS',
					]
				),
				l2=[
					'ST -> YZ', 
					'Z -> UX', 
					'X -> TZS',
				]
			)
		)


if __name__ == '__main__':
	unittest.main()
