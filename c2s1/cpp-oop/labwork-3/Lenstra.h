#pragma once

#include <vector>

#include "Factorization.h"

using namespace std;

typedef long long ll;

vector<ll> ellipticAdd(vector<ll> Point, vector<ll> AnotherPoint, ll a, ll b, ll modulo);

vector<ll> ellipticMul(ll k, vector<ll> Point, ll a, ll b, ll modulo);

ll lenstra(ll number, ll limit);