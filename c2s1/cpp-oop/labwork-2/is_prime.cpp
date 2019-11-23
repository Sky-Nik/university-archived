/*
	is_prime.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/23/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "is_prime.h"

// it's kinda long but appears to be faster than recurvise version
ll gcd(ll x, ll y)
{
	ll g;
	if (x < 0)
		x = -x;
	if (y < 0)
		y = -y;
	assert(x + y != 0);

	g = y;
	while (x > 0)
	{
		g = x;
		x = y % x;
		y = g;
	}
	return g;
}

// Jacobi's symbol
ll J(ll a, ll b)
{
	assert(b % 2 == 1);
	
	if (a >= b)
		a %= b;
	if (a == 0)
		return 0;
	if (a == 1)
		return 1;
	
	if (a < 0)
		if ((b - 1) / 2 % 2 == 0)
			return J(-a, b);
		else
			return -J(-a, b);

	if (a % 2 == 0)
		if (((b * b - 1) / 8) % 2 == 0) 
			return J(a / 2, b);
		else
			return -J(a / 2, b);

	ll g = gcd(a, b);

	if (g == a)
		return 0;
	if (g != 1)
		return J(g, b) * J(a / g, b);
	if (((a - 1) * (b - 1) / 4) % 2 == 0)
		return J(b, a);
	else
		return -J(b, a);
}

bool Soloway_Strassen(ll p, int Jehovah_witnesses)
{
	srand((unsigned int) time(nullptr));

	for (int i = 0; i < Jehovah_witnesses; ++i)
	{
		ll a = rand() % (p - 1) + 1;
		if (gcd(a, p) > 1)
			return false;

		ll j = mod_pow(a, (p - 1) / 2, p);
	
		ll _j = J(a, p);
	
		if ((j + p) % p != (_j + p) % p)
			return false;
	}

	return true;
}

// (x ** y) % N
ll mod_pow(ll x, ll y, ll N)
{
	ll temp;
	if (y == 1) return (x % N);
	if (y % 2 == 0)
	{
		temp = mod_pow(x, y / 2, N);
		return (temp * temp) % N;
	}
	else
	{
		temp = mod_pow(x, (y - 1) / 2, N);
		temp = (temp * temp) % N;
		temp = (temp * x) % N;
		return temp;
	}
}

bool Lehmann(ll p, int Jehovah_witnesses)
{
	srand((unsigned int)time(nullptr));

	for (int i = 0; i < Jehovah_witnesses; ++i)
	{
		ll a = rand() % (p - 1) + 1;
		
		ll b = mod_pow(a, (p - 1) / 2, p);

		if ((p + b) % p != 1 && (p + b) % p != p - 1)
			return false;
	}

	return true;
}

// TODO: fix
bool Rabin_Miller(ll p, int Jehovah_witnesses)
{
	srand((unsigned int)time(nullptr));

	ll P = p - 1, b = 0;
	while (P % 2 == 0)
	{
		++b;
		P >>= 1;
	}

	ll m = (p - 1) >> b;

	for (int i = 0; i < Jehovah_witnesses; ++i)
	{
		ll a = rand() % (p - 3) + 2;
	
		ll j = 0, z = (mod_pow(a, m, p) + p) % p;

		if (z == 1 || z == p - 1)
			continue;

		for (; j < b; ++j)
		{
			z = (z * z) % p;
			if (z == 1)
				return false;
			if (z == p - 1)
				break;
		}

		if (j == b && z != p - 1)
			return false;
	}

	return true;
}

// TODO
ll o(ll a, ll r)
{
	return 0;
}

// TODO
ll phi(ll r)
{
	return 0;
}

// TODO
bool AKS(ll n)
{
	; // if n = a^b, return false

	ll r = 2;
	while (o(n, r) <= log2(n) * log2(n))
		++r;
	
	for (ll a = 1; a < r; ++a)
		if (gcd(a, n) > 1)
			return false;

	if (n <= r)
		return true;

	for (ll a = 1; a < int(sqrt(phi(r)) * log(n)); ++a)
	{
		// compute polynomials (X+a)^n and X^n+a modulo X^r - 1, n (X^r = 1, n = 0);
		;
	}

	return true;
}