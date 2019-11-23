#include "QS.h"

/* Solves system A of linear equations */
vector<ll> gauss(vector<vector<ll>> A) {
	ll n = A.size();

	for (ll i = 0; i < n; ++i) {
		// Search for maximum in this column
		ll maxEl = abs(A[i][i]);
		ll maxRow = i;
		for (ll k = i + 1; k < n; ++k) {
			if (abs(A[k][i]) > maxEl) {
				maxEl = abs(A[k][i]);
				maxRow = k;
			}
		}

		if (maxEl != 0) {
			// Swap maximum row with current row(column by column)
			for (ll k = i; k < n + 1; ++k) {
				ll tmp = A[maxRow][k];
				A[maxRow][k] = A[i][k];
				A[i][k] = tmp;
			}

			// Make all rows below this one 0 in current column
			for (ll k = i + 1; k < n; ++k) {
				ll c = (-A[k][i] / A[i][i]) % 2;
				for (ll j = i; j < n + 1; ++j) {
					if (i == j)
						A[k][j] = 0;
					else
						A[k][j] = (A[k][j] + c * A[i][j]) % 2;
				}
			}
		}
	}

	// Solve equation Ax = b for an upper triangular matrix A
	vector<ll> x(n, 0);
	for (ll i = n - 1; i > -1; --i) {
		if (A[i][i] != 0) {
			x[i] = (A[i][n] / A[i][i]) % 2;

			for (ll k = i - 1; k > -1; --k)
				A[k][n] = (A[k][n] - A[k][i] * x[i]) % 2;
		}
	}

	return x;
}

/* Computes square root of a modulo prime number p using Tonelli - Shanks_algorithm */
ll primeModSqrt(ll a, ll p) {
	a %= p;

	// Simple case
	if (a == 0) return 0;

	if (p == 2)	return a;

	// Check solution existence on odd prime
	if (legender(a, p) != 1) return -1;

	// Simple case
	if (p % 4 == 3) {
		ll x = modPow(a, (p + 1) / 4, p);
		return x;
	}

	// Factor p - 1 on the form q * 2 ^ s(with Q odd)
	ll q = p - 1, s = 0;

	while (q % 2 == 0) {
		++s;
		q /= 2;
	}

	// Select a z which is a quadratic non resudue modulo p
	ll z = 1;

	while (legender(z, p) != -1)
		++z;

	ll c = modPow(z, q, p);

	// Search for a solution
	ll x = modPow(a, (q + 1) / 2, p), t = modPow(a, q, p), m = s;

	while (t != 1) {
		// Find the lowest i such that t ^ (2 ^ i) = 1
		ll i = 0, e = 2;

		for (ll i = 1; i < m; ++i) {
			if (modPow(t, e, p) == 1)
				break;

			e <<= 1;
		}

		// Update next value to iterate
		ll b = modPow(c, 2 << (m - i - 1), p);
		x = (x * b) % p;
		t = (t * b * b) % p;
		c = (b * b) % p;
		m = i;
	}

	return x;
}

/* Quadratic Sieve */
ll quadraticSieve(ll n, ll limit) {
	ll u = sqrt(n);

	vector<ll> f(2 * u + 1, 0);
	for (ll i = -u; i < u + 1; ++i)
		f[i + u] = i * i - n;

	cout << "\n\tF computed.\n\n\t";

	vector<ll> PP = primes(limit), P{ -1 };
	for (ll p : PP) {
		if (legender(n, p) == 1) {
			P.push_back(p);
			cout << p << ' ';
		}
	}

	cout << '\n';

	for (ll p : P) {
		ll r_i = primeModSqrt(n, p);
		for (ll k = ceil(-u - r_i / p); k < floor(u - r_i) / p; ++k) {
			while (f[u + k] % p == 0)
				f[u + k] /= p;
			cout << f[u + k] << ' ';
		}

		r_i = p - r_i;
		for (ll k = ceil(-u - r_i / p); k < floor(u - r_i) / p; ++k) {
			while (f[u + k] % p == 0)
				f[u + k] /= p;
			cout << f[u + k] << ' ';
		}

		cout << '\n';
	}

	cout << '\n';
	for (ll val : f)
		cout << val << ' ';
	cout << '\n';

	cout << "\n\tDivided.\n";

	vector<ll> R;

	for (ll r : f)
		if (r == 1)
			R.push_back(r);

	cout << "\n\t|R| = " << R.size() << '\n';

	// define V and E for convenience:
	vector<vector<ll>> E, V;

	for (ll i = 0; i < R.size(); ++i) {
		E.push_back({});
		V.push_back({});

		for (ll p : primes(limit)) {
			ll power = 0;

			while (R[i] % p == 0) {
				R[i] /= p;
				power += 1;
			}

			E.back().push_back(power);
			V.back().push_back(power % 2);
		}
	}

	cout << "\n\tSystem of equations created.\n";

	// find U :
	for (ll i = 0; i < V.size(); ++i)
		V[i].push_back(0);

	vector<ll> vec = gauss(V);
	vector<ll> U;

	for (ll i = 0; i < R.size(); ++i)
		if (vec[i] == 1)
			U.push_back(R[i]);

	cout << "\n\tSystem of equations solved.\n";

	// compute x and y:
	ll x = 1, y = 1;
	for (ll i = 0; i < R.size(); ++i) {
		if (find(U.begin(), U.end(), R[i]) != U.end()) {
			x *= R[i];
			x %= n;

			ll j = 0;
			for (ll p : primes(limit)) {
				y *= p * E[i][j++];
				y %= n;
			}
		}
	}

	if ((gcd(x + y, n) == 1 || gcd(x + y, n) == n) &&
		(gcd(x - y, n) == 1 || gcd(x - y, n) == n))
		return -1;

	if (gcd(x + y, n) == 1 || gcd(x + y, n) == n)
		return gcd(x - y, n);

	return gcd(x + y, n);
}