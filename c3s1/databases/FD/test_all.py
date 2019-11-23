#!usr/bin/env python
from os import system

if __name__ == '__main__':
	print(f'\nTesting closure:')
	system('python test_closure.py')

	print(f'\nTesting reduce:')
	system('python test_reduce.py')

	print(f'\nTesting equivalent:')
	system('python test_equivalent.py')
