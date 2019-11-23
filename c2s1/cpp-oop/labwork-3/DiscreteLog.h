#pragma once

#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>

#include "Factorization.h"

using namespace std;

typedef long long ll;

ll primitiveAlgorithm(ll g, ll b, ll n);

ll shanksAlgorithm(ll g, ll b, ll n);

ll pollardRho(ll g, ll b, ll n, ll limit);

ll index(ll g, ll b, ll n);

vector<ll> modGauss(vector<vector<ll>> A, ll p);

ll pohligHellman(ll g, ll b, ll n);
