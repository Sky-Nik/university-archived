/*
	is_prime.h
	OOP lab 2

	Created by Nikita Skybytskyi on 9/23/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

/*
This file contains four functions for determing whether a given number is a prime or not.

Functions:
	Soloway-Strassen's method, probabilistic

	Lehmannn's method, probabilistic

	Rabin-Miller's method, probabilistic with best results about amount of false witnesses

	Agraval-Kayal-Saxena's methos, deterministic, polynomial in size of input (ln n)
*/

#pragma once

#include <iostream>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

typedef long long ll;

ll mod_pow(ll, ll, ll);

bool Soloway_Strassen(ll, int);

bool Lehmann(ll, int);

bool Rabin_Miller(ll, int);

bool AKS(ll);