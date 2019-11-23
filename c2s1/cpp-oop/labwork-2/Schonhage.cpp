/*
	Schonhage.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/20/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lnum.h"

#define R 6

vector<long long> Q = { 1 };
vector<long long> P = {};

// fills P and Q
void init()
{
	for (int i = 0; i < 10; ++i)
		Q.push_back(Q.back() * 3 - 1);
	for (int i = 0; i < Q.size(); ++i)
		P.push_back(Q[i] * 18 + 8);
}

long long modInverse(long long a, long long m)
{
	long long x, y;
	long long g = gcdExtended(a, m, &x, &y);
	long long res = (x % m + m) % m;
	return res;
}

long long gcdExtended(long long a, long long b, long long *x, long long *y)
{
	if (a == 0)
	{
		*x = 0, *y = 1;
		return b;
	}

	long long x1, y1;
	long long gcd = gcdExtended(b % a, a, &x1, &y1);

	*x = y1 - (b / a) * x1;
	*y = x1;

	return gcd;
}

lnum lnum::Schonhage(lnum N)
{
	init();

	int i = 0, n = (int)max(exp(), N.exp());

	// find best length
	while (n > P[i])
		++i;

	// add zeros
	while (exp() < P[i])
		digits.push_back(0);
	while (N.exp() < P[i])
		N.digits.push_back(0);
	n = (int)max(exp(), N.exp());

	vector<long long> M(R);
	M[0] = (1 << (R * Q[i] - 1)) - 1;
	M[1] = (1 << (R * Q[i] + 1)) - 1;
	M[2] = (1 << (R * Q[i] + 2)) - 1;
	M[3] = (1 << (R * Q[i] + 3)) - 1;
	M[4] = (1 << (R * Q[i] + 5)) - 1;
	M[5] = (1 << (R * Q[i] + 7)) - 1;

	vector<lnum> U(R);
	for (int i = 0; i < R; ++i)
		U[i] = *this % M[i];

	vector<lnum> V(R);
	for (int i = 0; i < R; ++i)
		V[i] = (N) % M[i];

	vector<lnum> _w(R);
	for (int i = 0; i < R; ++i)
		_w[i] = (U[i] * V[i]) % M[i]; // make this multiplication recursive

	vector<vector<long long>> C(R, vector<long long>(R, 0));
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < i; ++j)
			C[i][j] = modInverse(M[i], M[j]);
		for (int j = i + 1; j < R; ++j)
			C[i][j] = modInverse(M[i], M[j]);
	}

	// TODO: add FAST computation of Cs

	vector<lnum> w(R, 0);
	w[0] = _w[0];
	for (int j = 0; j < R; ++j)
	{
		w[j] = _w[j];
		for (int i = 0; i < j; ++i)
		{
			w[j] = w[j] - w[i];
			w[j] = w[j] * lnum(C[i][j]);
			w[j] = w[j] % M[j];
			w[j] = w[j] + lnum(M[j]);
			w[j] = w[j] % M[j];
		}
	}

	lnum W = w[R - 1];
	for (int i = 0; i < R; ++i)
	{
		W = W * lnum(M[R - i - 1]);
		W = W + w[R - i - 1];
	}

	return W;
}