#!usr/bin/env python
import unittest
from closure import _closure


class TestClosure(unittest.TestCase):
	def test01(self):
		self.assertEqual(
			_closure(
				s='DF',
				l=[
					'A -> BC',
					'BCD -> D',
					'A -> D',
					'D -> F',
				],
				return_set=False
			),
			'DF'
		)


	def test02(self):
		self.assertEqual(
			_closure(
				s='A',
				l=[
					'DF -> B',
					'BCD -> D',
					'A -> D',
					'D -> F',
				],
				return_set=False
			),
			'ABDF'
		)
	

	def test03(self):
		self.assertEqual(
			_closure(
				s='BCD',
				l=[
					'DF -> B',
					'A -> BC',
					'A -> D',
					'D -> F',
				],
				return_set=False
			),
			'BCDF'
		)
	

	def test04(self):
		self.assertEqual(
			_closure(
				s='A',
				l=[
					'DF -> B',
					'A -> BC',
					'BCD -> D',
					'D -> F',
				],
				return_set=False
			),
			'ABC'
		)
	

	def test05(self):
		self.assertEqual(
			_closure(
				s='D',
				l=[
					'DF -> B',
					'A -> BC',
					'BCD -> D',
					'A -> D',
				],
				return_set=False
			),
			'D'
		)

	
	def test06(self):
		self.assertEqual(
			_closure(
				s='AC',
				l=[
					'AD -> EF',
					'E -> ACD',
					'AF -> DB',
				],
				return_set=False
			),
			'AC'
		)
	

	def test07(self):
		self.assertEqual(
			_closure(
				s='AD',
				l=[
					'AC -> D',
					'E -> ACD',
					'AF -> DB',
				],
				return_set=False
			),
			'AD'
		)
	

	def test08(self):
		self.assertEqual(
			_closure(
				s='E',
				l=[
					'AC -> D',
					'AD -> EF',
					'AF -> DB',
				],
				return_set=False
			),
			'E'
		)
	

	def test09(self):
		self.assertEqual(
			_closure(
				s='AF',
				l=[
					'AC -> D',
					'AD -> EF',
					'E -> ACD',
				],
				return_set=False
			),
			'AF'
		)
	

	def test10(self):
		self.assertEqual(
			_closure(
				s='X',
				l=[
					'TZ -> Y',
					'Y -> TU',
					'YU -> T',
				],
				return_set=False
			),
			'X'
		)
	

	def test11(self):
		self.assertEqual(
			_closure(
				s='TZ',
				l=[
					'X -> TZ',
					'Y -> TU',
					'YU -> T',
				],
				return_set=False
			),
			'TZ'
		)
	

	def test12(self):
		self.assertEqual(
			_closure(
				s='Y',
				l=[
					'X -> TZ',
					'TZ -> Y',
					'YU -> T',
				],
				return_set=False
			),
			'Y'
		)
	

	def test13(self):
		self.assertEqual(
			_closure(
				s='YU',
				l=[
					'X -> TZ',
					'TZ -> Y',
					'Y -> TU',
				],
				return_set=False
			),
			'TUY'
		)
	

	def test14(self):
		self.assertEqual(
			_closure(
				s='K',
				l=[
					'LM -> KN',
					'LN -> MP',
					'P -> KL',
					'N -> P',
				],
				return_set=False
			),
			'K'
		)
	

	def test15(self):
		self.assertEqual(
			_closure(
				s='LM',
				l=[
					'K -> L',
					'LN -> MP',
					'P -> KL',
					'N -> P',
				],
				return_set=False
			),
			'LM'
		)
	

	def test16(self):
		self.assertEqual(
			_closure(
				s='LN',
				l=[
					'K -> L',
					'LM -> KN',
					'P -> KL',
					'N -> P',
				],
				return_set=False
			),
			'KLNP'
		)
	

	def test17(self):
		self.assertEqual(
			_closure(
				s='P',
				l=[
					'K -> L',
					'LM -> KN',
					'LN -> MP',
					'N -> P',
				],
				return_set=False
			),
			'P'
		)
	

	def test18(self):
		self.assertEqual(
			_closure(
				s='N',
				l=[
					'K -> L',
					'LM -> KN',
					'LN -> MP',
					'P -> KL',
				],
				return_set=False
			),
			'N'
		)

	
	def test19(self):
		self.assertEqual(
			_closure(
				s='X',
				l=[
					'Z -> YU',
					'ST -> YZ',
					'Y -> US',
					'S -> ZU',
				],
				return_set=False
			),
			'X'
		)
	

	def test20(self):
		self.assertEqual(
			_closure(
				s='Z',
				l=[
					'X -> TZ',
					'ST -> YZ',
					'Y -> US',
					'S -> ZU',
				],
				return_set=False
			),
			'Z'
		)
	

	def test21(self):
		self.assertEqual(
			_closure(
				s='ST',
				l=[
					'X -> TZ',
					'Z -> YU',
					'Y -> US',
					'S -> ZU',
				],
				return_set=False
			),
			'STUYZ'
		)
	

	def test22(self):
		self.assertEqual(
			_closure(
				s='Y',
				l=[
					'X -> TZ',
					'Z -> YU',
					'ST -> YZ',
					'S -> ZU',
				],
				return_set=False
			),
			'Y'
		)
	

	def test23(self):
		self.assertEqual(
			_closure(
				s='S',
				l=[
					'X -> TZ',
					'Z -> YU',
					'ST -> YZ',
					'Y -> US',
				],
				return_set=False
			),
			'S'
		)
	

	def test24(self):
		self.assertEqual(
			_closure(
				s='AFE',
				l=[
					'A -> D',
					'D -> BE',
					'BD -> AF',
				],
				return_set=False
			),
			'ABDEF'
		)

	
	def test25(self):
		self.assertEqual(
			_closure(
				s='A',
				l=[
					'AFE -> BC',
					'D -> BE',
					'BD -> AF',
				],
				return_set=False
			),
			'A'
		)
	

	def test26(self):
		self.assertEqual(
			_closure(
				s='D',
				l=[
					'AFE -> BC',
					'A -> D',
					'BD -> AF',
				],
				return_set=False
			),
			'D'
		)
	

	def test27(self):
		self.assertEqual(
			_closure(
				s='BD',
				l=[
					'AFE -> BC',
					'A -> D',
					'D -> BE',
				],
				return_set=False
			),
			'BDE'
		)
	

	def test28(self):
		self.assertEqual(
			_closure(
				s='A',
				l=[
					'D -> C',
					'BC -> AD',
					'AC -> B',
					'C -> AD',
				],
				return_set=False
			),
			'A'
		)
	

	def test29(self):
		self.assertEqual(
			_closure(
				s='D',
				l=[
					'A -> CD',
					'BC -> AD',
					'AC -> B',
					'C -> AD',
				],
				return_set=False
			),
			'D'
		)
	

	def test30(self):
		self.assertEqual(
			_closure(
				s='BC',
				l=[
					'A -> CD',
					'D -> C',
					'AC -> B',
					'C -> AD',
				],
				return_set=False
			),
			'ABCD'
		)
	

	def test31(self):
		self.assertEqual(
			_closure(
				s='AC',
				l=[
					'A -> CD',
					'D -> C',
					'BC -> AD',
					'C -> AD',
				],
				return_set=False
			),
			'ACD'
		)
	

	def test32(self):
		self.assertEqual(
			_closure(
				s='C',
				l=[
					'A -> CD',
					'D -> C',
					'BC -> AD',
					'AC -> B',
				],
				return_set=False
			),
			'C'
		)
	

	def test33(self):
		self.assertEqual(
			_closure(
				s='C',
				l=[
					'BF -> D',
					'D -> E',
					'DE -> F',
					'C -> EF',
				],
				return_set=False
			),
			'CEF'
		)
	

	def test34(self):
		self.assertEqual(
			_closure(
				s='BF', 
				l=[
					'C -> BF', 
					'D -> E', 
					'DE -> F', 
					'C -> EF',
				],
				return_set=False
			), 
			'BF'
		)
	

	def test35(self):
		self.assertEqual(
			_closure(
				s='D', 
				l=[
					'C -> BF', 
					'BF -> D', 
					'DE -> F', 
					'C -> EF',
				],
				return_set=False
			), 
			'D'
		)
	

	def test36(self):
		self.assertEqual(
			_closure(
				s='DE', 
				l=[
					'C -> BF', 
					'BF -> D', 
					'D -> E', 
					'C -> EF',
				],
				return_set=False
			), 
			'DE'
		)
	

	def test37(self):
		self.assertEqual(
			_closure(
				s='C', 
				l=[
					'C -> BF', 
					'BF -> D', 
					'D -> E', 
					'DE -> F',
				],
				return_set=False
			), 
			'BCDEF'
		)
	

	def test38(self):
		self.assertEqual(
			_closure(
				s='AD', 
				l=[
					'C -> DF', 
					'BE -> A', 
					'D -> BF', 
					'FD -> AC',
				],
				return_set=False
			), 
			'ABCDF'
		)
	

	def test39(self):
		self.assertEqual(
			_closure(
				s='C', 
				l=[
					'AD -> C', 
					'BE -> A', 
					'D -> BF', 
					'FD -> AC',
				],
				return_set=False
			), 
			'C'
		)
	

	def test40(self):
		self.assertEqual(
			_closure(
				s='BE', 
				l=[
					'AD -> C', 
					'C -> DF', 
					'D -> BF', 
					'FD -> AC',
				],
				return_set=False
			), 
			'BE'
		)
	

	def test41(self):
		self.assertEqual(
			_closure(
				s='D', 
				l=[
					'AD -> C', 
					'C -> DF', 
					'BE -> A', 
					'FD -> AC',
				],
				return_set=False
			), 
			'D'
		)
	

	def test42(self):
		self.assertEqual(
			_closure(
				s='FD', 
				l=[
					'AD -> C', 
					'C -> DF', 
					'BE -> A', 
					'D -> BF',
				],
				return_set=False
			), 
			'BDF'
		)
	

	def test43(self):
		self.assertEqual(
			_closure(
				s='AB', 
				l=[
					'E -> CD', 
					'ABC -> DE', 
					'AD -> CF', 
					'F -> E',
				],
				return_set=False
			), 
			'AB'
		)
	

	def test44(self):
		self.assertEqual(
			_closure(
				s='E', 
				l=[
					'AB -> F', 
					'ABC -> DE', 
					'AD -> CF', 
					'F -> E',
				],
				return_set=False
			), 
			'E'
		)
	

	def test45(self):
		self.assertEqual(
			_closure(
				s='ABC', 
				l=[
					'AB -> F', 
					'E -> CD', 
					'AD -> CF', 
					'F -> E',
				],
				return_set=False
			), 
			'ABCDEF'
		)
	

	def test46(self):
		self.assertEqual(
			_closure(
				s='AD', 
				l=[
					'AB -> F', 
					'E -> CD', 
					'ABC -> DE', 
					'F -> E',
				],
				return_set=False
			), 
			'AD'
		)
	

	def test47(self):
		self.assertEqual(
			_closure(
				s='F', 
				l=[
					'AB -> F', 
					'E -> CD', 
					'ABC -> DE', 
					'AD -> CF',
				],
				return_set=False
			), 
			'F'
		)
	

	def test48(self):
		self.assertEqual(
			_closure(
				s='X', 
				l=[
					'Z -> XS', 
					'UY -> ZT', 
					'XY -> S',
				],
				return_set=False
			), 
			'X'
		)
	

	def test49(self):
		self.assertEqual(
			_closure(
				s='Z', 
				l=[
					'X -> ZYU', 
					'UY -> ZT', 
					'XY -> S',
				],
				return_set=False
			), 
			'Z'
		)
	

	def test50(self):
		self.assertEqual(
			_closure(
				s='UY', 
				l=[
					'X -> ZYU', 
					'Z -> XS', 
					'XY -> S',
				],
				return_set=False
			), 
			'UY'
		)
	

	def test51(self):
		self.assertEqual(
			_closure(
				s='XY', 
				l=[
					'X -> ZYU', 
					'Z -> XS', 
					'UY -> ZT',
				],
				return_set=False
			), 
			'STUXYZ'
		)
	

	def test52(self):
		self.assertEqual(
			_closure(
				s='ST', 
				l=[
					'Z -> UX', 
					'XT -> S', 
					'X -> TZS',
				],
				return_set=False
			),
			'ST'
		)
	

	def test53(self):
		self.assertEqual(
			_closure(
				s='Z', 
				l=[
					'ST -> YZ', 
					'XT -> S', 
					'X -> TZS',
				],
				return_set=False
			), 
			'Z'
		)
	

	def test54(self):
		self.assertEqual(
			_closure(
				s='XT', 
				l=[
					'ST -> YZ', 
					'Z -> UX', 
					'X -> TZS',
				],
				return_set=False
			), 
			'STUXYZ'
		)
	

	def test55(self):
		self.assertEqual(
			_closure(
				s='X', 
				l=[
					'ST -> YZ', 
					'Z -> UX', 
					'XT -> S',
				],
				return_set=False
			), 
			'X'
		)


if __name__ == '__main__':
	unittest.main()
