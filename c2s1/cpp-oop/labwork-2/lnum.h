/*
	lreal.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/14/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#pragma once

#include <algorithm>
#include <iostream>
#include <complex>
#include <vector>

#define DEFAULT_BASE 2 // change to 2^n

using namespace std;

long long gcdExtended(long long, long long, long long *, long long *);

long long modInverse(long long, long long);

/*
Class modeling long signed integer N.

Fields:
	digits - list of digits of N, N = sum_(i = 0)^(exp) digits[i] * pow(base, i);
	base   - base of the system in which N is represented, 2 by default;
	exp    - amount of digits in N, smallest n such that (1 << (n + 1)) > N, 0 for N = 0;
	sign   - signum function, +1 for positive, 0 for 0, -1 for negative, 0 ;

Members:
	Constructors:
		default, construct zero
		from long long
		from vector of digigts

	Supported operators: 
		+ (addition)
		- (substraction)
		- (unary)
		* (multiplication)
		/ (division) (by int and by lnum)
		+= (addition and assignment)
		-= (substraction and assignment)
		*= (multiplication and assignment)
		/= (division and assignment) (by int and by lnum)

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

	Strip - drops out leading zeros

	Abs   - returns abs of lnum

	Destructor
*/
class lnum
{
protected:
	vector<int> digits;
	int base;
	int sign;

public:
	lnum() { digits = vector<int>(1,0); base = DEFAULT_BASE; sign = 0; };
	lnum(long long);
	lnum(vector<int>);
	lnum(vector<int>, int);

	int exp() { return (int)digits.size(); };

	friend class lreal;

protected:
	friend lnum abs(lnum);
	friend lnum strip(lnum);

public:
	friend ostream& operator << (ostream&, lnum);

	lnum operator + (lnum);
	lnum operator - (lnum);
	lnum operator * (lnum); // Karatsuba multiplication
	lnum operator / (lnum);
	lnum operator / (long long);
	lnum operator % (lnum);
	lnum operator % (long long);

	lnum operator += (lnum);
	lnum operator -= (lnum);
	lnum operator *= (lnum);
	lnum operator /= (lnum);
	lnum operator /= (long long);
	lnum operator %= (lnum);
	lnum operator %= (long long);

	lnum operator - (); // unary

	lnum operator << (int); // a.k.a. * 2
	lnum operator <<= (int);
	lnum operator >> (int); // a.k.a. / 2
	lnum operator >>= (int);

	bool operator < (lnum);
	bool operator <= (lnum);
	bool operator > (lnum);
	bool operator >= (lnum);
	bool operator == (lnum);
	bool operator != (lnum);

	//operator bool(); // false iff 0

	virtual operator string();

	lnum Toom_Cook(lnum, int);

	lnum Strassen(lnum);

	lnum Schonhage(lnum);

	~lnum() = default;
};