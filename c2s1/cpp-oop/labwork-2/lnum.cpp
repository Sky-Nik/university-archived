/*
	lnum.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/14/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lnum.h"
#include "lreal.h"

lnum::lnum(long long n)
{
	base = DEFAULT_BASE;

	// check for negatives
	if (n < 0)
	{
		sign = -1;
		n *= -1;
	}
	
	if (n > 0)
		sign = 1;
	
	if (n == 0)
	{
		sign = 0;
		digits = vector<int>(1,0);
	}

	while (n > 0)
	{
		digits.push_back(n % base);
		n /= base;
	}
}

lnum::lnum(vector<int> N)
{
	for (int i = 0; i < N.size(); ++i)
		digits.push_back(N[i]);
	base = DEFAULT_BASE;
	sign = 1;
}

lnum::lnum(vector<int> digits, int decimal_point)
{
	this->digits = vector<int>(digits.begin() + decimal_point, digits.end());
	base = DEFAULT_BASE;
	sign = 1;
}

lnum lnum::operator + (lnum N)
{
	lnum New;
	// strip
	*this = strip(*this);
	N = strip(N);

	if (-N > *this && N.sign < 0)
	{
		New = (-N) + (-(*this));
		New = -New;
		return New;
	}
		
	if (-(*this) > N && sign < 0)
	{
		New = (-*this) + (-N);
		New = -New;
		return New;
	}

	// add zeros
	int n = (int)max(exp(), N.exp());
	while (exp() != n)
		digits.push_back(0);
	while (N.exp() != n)
		N.digits.push_back(0);
			
	New.digits = vector<int>(1,0);

	for (size_t i = 0; i < n; ++i)
	{
		int s = New.digits.back() + digits[i] * sign + N.digits[i] * N.sign;
		New.digits.back() = (s + 2 * base) % base;
		New.digits.push_back((s + 2 * base) / base - 2);
	}
	
	New.base = DEFAULT_BASE;
	New.sign = 1;

	New = strip(New);

	return New;
}

lnum lnum::operator += (lnum N)
{
	lnum New = *this + N;
	*this = New;
	return *this;
}

lnum lnum::operator - ()
{
	lnum New = *this;
	New.sign *= -1;
	return New;
}

lnum lnum::operator - (lnum N)
{
	return *this + (-N);
}

lnum lnum::operator -= (lnum N)
{
	lnum New = *this - N;
	*this = New;
	return *this;
}

// Karatsuba
lnum lnum::operator * (lnum N)
{
	// strip
	*this = strip(*this);
	N = strip(N);
	
	int n = (int)max(exp(), N.exp());

	// add zeros
	while (exp() != n)
		digits.push_back(0);
	while (N.exp() != n)
		N.digits.push_back(0);

	// base case
	if (n == 0)
	{
		lnum A(0);
		return A;
	}
	if (n == 1)
	{
		lnum A(digits[0] * N.digits[0]);
		A.sign = sign * N.sign;
		return A;
	}

	// recursive calls
	int m = n / 2;
	vector<int> u0, u1, v0, v1;
	for (int i = 0; i < m; ++i)
	{
		u0.push_back(digits[i]); 
		v0.push_back(N.digits[i]);
	}
	for (int i = m; i < n; ++i)
	{
		u1.push_back(digits[i]);
		v1.push_back(N.digits[i]);
	}

	lnum U0(u0), U1(u1), V0(v0), V1(v1);
	U0.sign = sign; U1.sign = sign; V0.sign = N.sign; V1.sign = N.sign;

	lnum M1 = U1 - U0, M2 = V0 - V1;
	
	lnum N1 = U1 * V1, N2 = M1 * M2, N3 = U0 * V0;

	lnum A = (N1 << (2 * m)) + (N1 << m) + (N2 << m) + (N3 << m) + N3;

	A.sign = sign * N.sign;
	A = strip(A);

	return A;
}

lnum lnum::operator *= (lnum N)
{
	lnum New = *this * N;
	*this = New;
	return *this;
}

lnum lnum::operator / (long long n)
{
	lnum New = *this;
	for (int i = (int)New.exp() - 1; i > 0; --i)
	{
		int s = New.digits[i];
		New.digits[i] /= n;
		New.digits[i - 1] += base * (s - n * New.digits[i]);
	}
	New.digits[0] /= n;

	return New;
}

lnum lnum::operator /= (long long n)
{
	*this = *this / n;
	return *this;
}

lnum lnum::operator / (lnum N)
{
	int n = N.exp();
	lreal T = lreal(*this) >> n;
	lreal R = lreal(N) >> n;
	lreal A = T / R;
	A = strip(A);
	return lnum(A.digits, A.decimal_point);
}

lnum lnum::operator /= (lnum N)
{
	lnum New = *this / N;
	*this = New;
	return *this;
}

lnum lnum::operator % (lnum N)
{
	return (*this - (*this / N) * N);
}

lnum lnum::operator %= (lnum N)
{
	*this -= (*this / N) * N;
	return *this;
}

lnum lnum::operator % (long long n)
{
	return (*this - (*this / n) * n);
}

lnum lnum::operator %= (long long n)
{
	*this -= (*this / n) * lnum(n);
	return *this;
}

lnum lnum::operator << (int n)
{
	lnum New = *this;
	for (int i = 0; i < n; ++i)
		New.digits.insert(New.digits.begin(), 0);
	return New;
}

lnum lnum::operator <<= (int n)
{
	*this = *this << n;
	return *this;
}

lnum lnum::operator >> (int n)
{
	lnum New = *this;
	for (int i = 0; i < n; ++i)
		New.digits.erase(New.digits.begin());
	return New;
}

lnum lnum::operator >>= (int n)
{
	*this = *this >> n;
	return *this;
}

bool lnum::operator < (lnum N)
{
	return (*this <= N) && (*this != N);
}

bool lnum::operator <= (lnum N)
{
	return *this == N || ! (N >= *this);
}

bool lnum::operator > (lnum N)
{
	return (*this >= N) && (*this != N);
}

bool lnum::operator >= (lnum N)
{
	// strip
	*this = strip(*this);
	N = strip(N);

	// basic checks
	if (sign > N.sign)
		return true;
	if (sign < N.sign)
		return false;
	if (exp() > N.exp())
		return true;
	if (exp() < N.exp())
		return false;

	// per digit comparison
	for (int i = (int)exp() - 1; i >= 0; --i)
	{
		if (digits[i] > N.digits[i])
			return true;
		if (digits[i] < N.digits[i])
			return false;
	}

	// equality case
	return true;
}

bool lnum::operator == (lnum N)
{
	*this = strip(*this);
	N = strip(N);

	// basic checks
	if (sign != N.sign)
		return false;
	if (exp() != N.exp())
		return false;

	// per digit comparison
	for (int i = 1; i <= exp(); ++i)
		if (digits[exp() - i] != N.digits[exp() - i])
			return false;

	// equality case
	return true;
}

bool lnum::operator != (lnum N)
{
	return !(*this == N);
}

/*lnum::operator bool()
{
	return *this != lnum();
}*/

lnum::operator string()
{
	lnum New = strip(*this);

	string s = "";
	for (int i = 0; i < New.exp(); ++i)
		s = (char)(New.digits[i] + 48) + s;
	if (New.sign == -1)
		s = '-' + s;

	return s;
}

lnum abs(lnum N)
{
	lnum New = N;
	New.sign = 1;
	return New;
}

lnum strip(lnum N)
{
	lnum New = N;
	while (New.exp() > 1 && New.digits.back() == 0)
		New.digits.pop_back();
	return New;
}


ostream& operator << (ostream& out, lnum N)
{
	out << (string)N;
	return out;
}