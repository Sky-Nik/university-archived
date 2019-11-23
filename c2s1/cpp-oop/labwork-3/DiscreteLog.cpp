#pragma warning(disable:4244)
#pragma warning(disable:4334)
#pragma warning(disable:4715)

#include "DiscreteLog.h"

ll primitiveAlgorithm(ll g, ll b, ll n) {
	ll x = 1;

	for (ll i = 0; i < n; ++i) {
		if (x == b) return i;

		x = (x * g) % n;
	}
}

ll shanksAlgorithm(ll g, ll b, ll n) {
	ll a = ceil(sqrt(n));

	vector<pair<ll, ll>> L1, L2;

	ll t = modPow(g, a, n);

	ll c = 1;
	for (ll i = 0; i <= a; ++i) {
		L1.push_back({ c, i });
		c = c * t % n;
	}
	sort(L1.begin(), L1.end());

	c = b;
	for (ll i = 0; i < a; ++i) {
		L2.push_back({ c, i });
		c = c * g % n;
	}
	sort(L2.begin(), L2.end());

	ll i = 0, j = 0;
	while (true) {
		if (L1[i].first < L2[j].first) ++i;
		else if (L1[i].first > L2[j].first) ++j;
		else break;
	}

	ll k = L2[j].second, l = L1[i].second;

	return l * a - k;
}

ll pollardRho(ll g, ll b, ll n, ll limit) {
	vector<ll> U{ 0 }, V{ 0 }, Z{ 1 };

	for (ll i = 0; i < limit; ++i) {
		if (Z.back() < n / 3) {
			U.push_back((U.back() + 1) % (n - 1));
			V.push_back(V.back() % (n - 1));
			Z.push_back(g * Z.back() % n);
		}
		else if (Z.back() < 2 * n / 3) {
			U.push_back((2 * U.back()) % (n - 1));
			V.push_back((2 * V.back()) % (n - 1));
			Z.push_back(Z.back() * Z.back() % n);
		}
		else {
			U.push_back(U.back() % (n - 1));
			V.push_back((V.back() + 1) % (n - 1));
			Z.push_back(b * Z.back() % n);
		}
	}

	for (ll i = 0; i < limit / 2; ++i) {
		if (Z[i] == Z[2 * i]) {
			ll d = abs(gcd(U[i] - U[2 * i], n - 1));
			if (d == 1) {
				ll l = modInv(U[2 * i] - U[i], n - 1)[0];
				
				return (l * abs(V[i] - V[2 * i]) + n - 1) % (n - 1);
			}
			else if (d != n - 1) {
				ll mod = (n - 1) / d;
				ll x0 = (modInv((U[2 * i] - U[i]) / d, mod)[0] * abs(V[i] - V[2 * i]) / mod + mod) % mod;
				for (ll m = 0; m < d; ++m) {
					ll guess = modPow(g, x0 + m * mod, n);
					if (guess == b) {
						return (x0 + m * mod) % (n - 1);
					}
				}
			}
		}
	}

	return primitiveAlgorithm(g, b, n); // in case of fail
}

pair<bool, vector<pair<ll, ll>>> factorize(ll n, vector<ll> FB) {
	vector<pair<ll, ll>> factors;

	for (ll prime : FB) {
		factors.push_back({ prime, 0 });

		while (n % prime == 0) {
			n /= prime;
			++(factors.back().second);
		}
	}

	bool successful = (n == 1);

	return{ successful, factors };
}

ll index(ll g, ll b, ll n) {
	vector<ll> S = primes((ll)sqrt(n));
	vector<vector<ll>> Equations;

	while (Equations.size() < S.size() + 10) {
		ll k = rand() % (n - 1);

		ll t = modPow(g, k, n);
		auto f = factorize(t, S);

		if (f.first) {
			vector<ll> Equation;

			for (auto P : f.second)
				Equation.push_back(P.second);

			Equation.push_back(k);

			Equations.push_back(Equation);
		}
	}

	auto Solution = modGauss(Equations, n - 1);

	bool success = false;

	while (!success) {
		ll k = rand() % (n - 1);

		ll t = b * modPow(g, k, n) % n;

		auto f = factorize(t, S);

		if (f.first) {
			ll sum = 0;

			for (ll i = 0; i < S.size(); ++i)
				sum += Solution[i] * f.second[i].second;

			return (sum - k + (n - 1) * n) % (n - 1);
		}
	}
}

vector<ll> modGauss(vector<vector<ll>> A, ll p) {
	ll n = A.size();
	ll m = A[0].size();

	for (ll i = 0; i < m - 1; ++i) {
		// Search for invertible elem
		ll invEl = A[i][i];
		ll invRow = i;
		for (ll k = i + 1; k < n; k++) {
			if (gcd(A[k][i], p) == 1) {
				invEl = A[k][i];
				invRow = k;
				break;
			}
		}

		// Swap invertible row with current row(column by column)
		for (ll k = i; k < m; ++k) {
			ll tmp = A[invRow][k];
			A[invRow][k] = A[i][k];
			A[i][k] = tmp;
		}

		// Make all rows below this one 0 in current column
		for (ll k = i + 1; k < n; ++k) {
			ll c = (-A[k][i] * modInv(A[i][i], p)[0]) % p;

			A[k][i] = 0;
			for (ll j = i + 1; j < m; ++j)
				A[k][j] = (A[k][j] + c * A[i][j]) % p;
		}
	}

	// Solve equation Ax = b for an upper triangular matrix A
	vector<ll> x(m - 1, 0);
	for (ll i = m - 2; i >= 0; --i) {
		if (A[i][i] != 0) {
			x[i] = (A[i][m - 1] * modInv(A[i][i], p)[0]) % p;

			for (ll k = i - 1; k > -1; --k)
				A[k][m - 1] = (A[k][m - 1] - A[k][i] * x[i]) % p;
		}
	}

	return x;
}

ll pohligHellman(ll g, ll b, ll n) {
	ll m = n - 1, k = 0;
	while (m > 1) {
		m /= 2;
		++k;
	}

	vector<ll> Z(k);
	Z[0] = b;
	vector<ll> Q(k);
	Q[0] = modPow(Z[0], (n - 1) / 2, n) == 1 ? 0 : 1;

	for (ll i = 1; i < k; ++i) {
		Z[i] = (Z[i - 1] * modPow(modInv(g, n)[0], Q[i - 1] * (1 << (i - 1)), n)) % n;
		Q[i] = modPow(Z[i], (n - 1) / (1 << (i + 1)), n) == 1 ? 0 : 1;
	}

	ll x = 0;
	for (ll i = 0; i < k; ++i)
		x += Q[i] * (1 << i);

	return x % (n - 1);
}
