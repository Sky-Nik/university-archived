/*
	lreal.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/26/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lreal.h"

lreal::lreal(lnum N)
{
	base = N.base;
	digits = N.digits;
	sign = N.sign;
	decimal_point = 0;
}

lreal::lreal(vector<int> digits, int decimal_point)
{
	this->digits = digits;
	this->decimal_point = decimal_point;
	sign = 1;
	base = 2;
}

lreal lreal::operator + (lreal R)
{
	int n = max(R.decimal_point, decimal_point);
	lreal A = lreal(lnum((*this << n).digits) + lnum((R << n).digits)) >> n;
	A.decimal_point = n;
	return A;
}

lreal lreal::operator - (lreal R)
{
	int n = max(R.decimal_point, decimal_point);
	lreal A = lreal(lnum((*this << n).digits) - lnum((R << n).digits)) >> n;
	A.decimal_point = n;
	return A;
}

lreal lreal::operator * (lreal R)
{
	int n = max(R.decimal_point, decimal_point);
	lreal A = lreal(lnum((*this << n).digits) * lnum((R << n).digits)) >> (2 * n);
	A.decimal_point = 2 * n;
	return A;
}

lreal lreal::operator / (lreal R)
{
	int n = R.exp() - R.decimal_point;
	lreal A = *this >> n;
	lreal B = R >> n;
	return A * B.inverse(A.decimal_point + B.decimal_point);
}

lreal lreal::operator << (int n)
{
	lnum New = *this;
	int p = decimal_point;
	
	for (int i = 0; i < n; ++i)
		--p;
	
	while (p < 0)
	{
		New.digits.insert(New.digits.begin(), 0);
		++p;
	}
	
	return New;
}

lreal lreal::operator >> (int n)
{
	lreal New = *this;
	
	for (int i = 0; i < n; ++i)
		++New.decimal_point;

	while (New.exp() < New.decimal_point)
		New.digits.push_back(0);

	return New;
}


lreal lreal::inverse(int p)
{
	lreal New = *this;

	while (New.decimal_point < 3)
	{
		New.digits.insert(New.digits.begin(), 0);
		++New.decimal_point;
	}

	// initial approximation
	lreal Z(8 / (4 * New.digits[New.decimal_point - 1] + 2 * New.digits[New.decimal_point - 2] + New.digits[New.decimal_point - 3]));
	// wiki recommends 48/17 - 32/17 * *this
	
	int k = 1;

	while (k < p)
	{
		lreal temp = Z * Z;

		while (New.exp() < 2 * k + 3)
			New.digits.push_back(0);

		vector<int> v_k;
		for (int i = 0; i < 2 * k + 3; ++i)
			v_k.push_back(New.digits[i]);

		lreal V_k(v_k, New.decimal_point);
		// cout << "V_k = " << V_k << '\n';

		Z = lreal(2) * Z - V_k * temp;
		while (Z.decimal_point > k + 1 && Z.digits[0] == 1)
		{
			Z = Z + lreal({ 1 }, decimal_point);
			Z.digits.erase(Z.digits.begin());
			--Z.decimal_point;
		}
		k <<= 1;
	}

	return Z;
}

lreal::operator string()
{
	lreal New = strip(*this);

	while (New.exp() <= New.decimal_point)
		New.digits.push_back(0);

	string s = "";
	
	for (int i = 0; i < New.exp(); ++i)
	{
		if (i == New.decimal_point)
			s = '.' + s;

		s = (char)(New.digits[i] + 48) + s;
	}
	
	if (sign == -1)
		s = '-' + s;

	return s;
}

lreal strip(lreal R)
{
	lreal New = R;
	while (New.exp() > 1 && New.digits.back() == 0)
		New.digits.pop_back();
	while (New.digits[0] == 0)
	{
		New.digits.erase(New.digits.begin());
		--New.decimal_point;
	}

	return New;
}

ostream& operator << (ostream& out, lreal R)
{ 
	out << (string)R;
	return out;
}