#pragma once

#include <vector>

#include "Factorization.h"

using namespace std;

typedef long long ll;

vector<ll> primes(ll n);

vector<ll> modInv(ll a, ll b);

ll gcd(ll a, ll b);

ll legender(ll a, ll p);

ll modPow(ll a, ll p, ll m);

ll fermat(ll n);

ll pollardRho(ll n, ll limit);

ll generator(ll n, vector<ll> P);