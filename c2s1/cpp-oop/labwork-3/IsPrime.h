#pragma once

#include <iostream>
#include <complex>
#include <vector>
#include <cmath>
#include <set>

#define PI 3.1415926

#include "Factorization.h"

using namespace std;

typedef long long ll;

bool TryDivisors(ll);

//bool TryDivisors_optimised(ll);

vector<ll> EratosphenSieve(ll);

ll modpow(ll, ll, ll);

bool Fermat_is_prime(ll, ll);

bool strictPseudoPrimality(ll);

bool is_Fermat_prime(ll);

bool is_Mersenne_prime(ll);

bool Fermat_Mersenne(ll);

bool N_minus_1(ll, vector<ll>);

//==========================

bool Konyagin_Pomerance(ll);