#pragma once

#include <Windows.h>
#include <algorithm>
#include <typeinfo>  
#include <iostream>
#include <complex>
#include <vector>

#define DEFAULT_BASE 2 // change to 2^n

using namespace std;

/*
Class modeling long signed integer N.

Fields:
	digits - list of digits of N, N = sum_(i = 0)^(exp) digits[i] * pow(base, i);
	base   - base of the system in which N is represented, 2 by default;
	sign   - signum function, +1 for positive, 0 for 0, -1 for negative, 0 ;

Members:
	Constructors:
		default, construct zero

		template from inherit numeric types such as short, int, long long, etc.

		from vector of digigts

	Supported operators: (all operators are template to work with both inherit numeric and lnum types;
		- (unary)
		
		+ (addition)
		- (substraction)
		* (multiplication) 
		/ (division)
		% (remainder modulo)

		+= (addition and assignment)
		-= (substraction and assignment)
		*= (multiplication and assignment)
		/= (division and assignment) 
		%= (remained modulo and assignment)s

		<< (left binary shift)
		>> (right binary shift)
		<<= (left binary shift with assignment)
		>>= (right binary shift with assignment)

		> (greater than)
		< (less than)
		>= (greater or equal)
		<= (less or equal)

		
		== (equal)
		!= (not equal)

	Cast:
		to bool
		to string

	Fucntions:
		strip() - drops out leading zeros
		abs()   - returns absoluta value of lnum
		exp ()  - number of digits in N

	Destructor
*/
class lnum
{
	vector<int> digits;
	int base;
	int sign;

public:
	lnum() { digits = { 0 }; base = DEFAULT_BASE; sign = 0; };
	
	// can't write as template
	lnum(long long);

	lnum(vector<int>);

	size_t exp() { return digits.size(); };

	friend lnum abs(lnum);

	friend lnum strip(lnum);

	friend ostream& operator << (ostream&, lnum);

	template<typename T>
	lnum operator + (T);
	template<typename T>
	lnum operator - (T);
	template<typename T>
	lnum operator * (T); // Karatsuba multiplication
	template<typename T>
	lnum operator / (T);
	template<typename T>
	lnum operator % (T);

	template<typename T>
	lnum operator += (T);
	template<typename T>
	lnum operator -= (T);
	template<typename T>
	lnum operator *= (T);
	template<typename T>
	lnum operator /= (T);
	template<typename T>
	lnum operator %= (T);

	lnum operator - (); // unary

	lnum inverse(int); // Computes 1 / *this with precision given by int

	lnum operator << (int); // a.k.a. * 2
	lnum operator >> (int); // a.k.a. / 2

	lnum operator <<= (int);
	lnum operator >>= (int);

	template<typename T>
	bool operator < (T);
	template<typename T>
	bool operator <= (T);
	template<typename T>
	bool operator > (T);
	template<typename T>
	bool operator >= (T);
	template<typename T>
	bool operator == (T);
	template<typename T>
	bool operator != (T);

	operator bool(); // false iff 0

	operator string(); // lnum, base

	lnum Toom_Cook(lnum, int); // appears to be correct, but relies on division opertor

	lnum Strassen(lnum);

	lnum Schonhage(lnum);

	~lnum() = default;
};

#include "lnum_temp.tpp"