#pragma once

#include <iostream>
#include <vector>
#include <cmath>

#include "Factorization.h"

using namespace std;

typedef long long ll;

vector<ll> gauss(vector<vector<ll>> A);

ll quadraticSieve(ll number, ll limit);