/*
	Toom-3.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/16/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lnum.h"

#define MIN_DIGITS 1

lnum lnum::Toom_Cook(lnum N, int r)
{
//	long long t1 = GetTickCount(); // "time" measurement
	*this = strip(*this);
	N = strip(N);

	int n = (int)max(exp(), N.exp());

	// base case
	if (n <= MIN_DIGITS)
		return *this * N;

	n += r - 1;
	n /= r;
	n *= r;

	// add zeros
	while (exp() != n)
		digits.push_back(0);
	while (N.exp() != n)
		N.digits.push_back(0);

	// divide into parts
	int t = n / r;
	vector<int> m(r + 1);
	for (int i = 0; i < r; ++i)
		m[i] = i * t;
	m[r] = n;
	
	vector<lnum> U(r);
	for (int i = 0; i < r; ++i)
		U[i] = lnum(vector<int>(digits.begin() + m[i], digits.begin() + m[i + 1]));
	vector<lnum> V(r);
	for (int i = 0; i < r; ++i)
		V[i] = lnum(vector<int>(N.digits.begin() + m[i], N.digits.begin() + m[i + 1]));

	// compute W(i), i = 0..2r-2
	vector<lnum> W(2 * r - 1);
	for (int i = 0; i < 2 * r - 1; ++i)
	{
		lnum P(0), Q(0);
		for (int j = 0; j < r; ++j)
		{
			P += U[j] * (long long)pow(i, j);
			Q += V[j] * (long long)pow(i, j);
		}
	
		// TODO: make recursive call
		// recursive (well, not really) call
		W[i] = P * Q;
	}

	// compute "coefficients" of W
	for (int i = 1; i < 2 * r - 1; ++i)
	{
		for (int j = 2 * r - 2; j >= i; --j)
		{
			W[j] -= W[j - 1];
			W[j] /= i;
		}
	}

	// compute ai
	for (int i = 2 * r - 3; i > 0; --i)
		for (int j = i; j < 2 * r - 2; ++j)
			W[j] -= W[j + 1] * i;

	// compute answer
	lnum A(0);
	for (int i = 0; i < 2 * r - 1; ++i)
		A += (W[i]) << (i * t);

//	long long t2 = GetTickCount();  // "time" measurement
//	cout << "Processor ticks used : " << (t2 - t1) << "\n";
	A = strip(A);

	return A;
}