/*
	Strassen.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/18/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lnum.h"

#define PI 3.1415926535897932384626433832795028841971693993751

// Fast Fourier Transform
void fft(vector<complex<double>> & a, bool invert)
{
	int n = (int)a.size();

	for (int i = 1, j = 0; i < n; ++i)
	{
		int bit = n >> 1;
		for (; j >= bit; bit >>= 1)
			j -= bit;
		j += bit;
		if (i < j)
			swap(a[i], a[j]);
	}

	for (int len = 2; len <= n; len <<= 1)
	{
		double ang = 2 * PI / len * (invert ? -1 : 1);
		complex<double> wlen(cos(ang), sin(ang));
		for (int i = 0; i < n; i += len)
		{
			complex<double> w(1);
			for (int j = 0; j < len / 2; ++j)
			{
				complex<double> u = a[i + j], v = a[i + j + len / 2] * w;
				a[i + j] = u + v;
				a[i + j + len / 2] = u - v;
				w *= wlen;
			}
		}
	}

	if (invert)
		for (int i = 0; i < n; ++i)
			a[i] /= n;
}

lnum lnum::Strassen(lnum N)
{
	vector<int> a = digits, b = N.digits;
	vector<complex<double>> fa(a.begin(), a.end()), fb(b.begin(), b.end());
	int n = 1, k = max((int)a.size(), (int)b.size());
	while (n < k)
		n <<= 1;
	n <<= 1;

	fa.resize(n), fb.resize(n);

	fft(fa, false), fft(fb, false);
	for (int i = 0; i < n; ++i)
		fa[i] *= fb[i];
	fft(fa, true);

	lnum A = 0;
	for (int i = 0; i < n; ++i)
	{
		int s = A.digits.back() + int(fa[i].real() + 0.5) + A.base;
		A.digits.back() = s % A.base;
		A.digits.push_back(s / A.base - 1);
	}

	A = strip(A);

	return A;
}