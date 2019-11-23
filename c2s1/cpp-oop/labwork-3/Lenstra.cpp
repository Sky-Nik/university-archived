#include "Lenstra.h"

/* Addition in Elliptic curve modulo m p, q in Cartesian coordinates */
vector<ll> ellipticAdd(vector<ll> p, vector<ll> q, ll a, ll b, ll m) {
	// if one point is infinity, return the other one
	if (p[2] == 0) return q;

	if (q[2] == 0) return p;

	ll nom, denom;

	if (p[0] == q[0]) {
		if ((p[1] + q[1]) % m == 0) return{ 0, 1, 0 }; // infinity

		nom = (3 * p[0] * p[0] + a) % m;
		denom = (2 * p[1]) % m;
	}
	else {
		nom = (q[1] - p[1]) % m;
		denom = (q[0] - p[0]) % m;
	}

	vector<ll> A = modInv(denom, m);

	ll inv = A[0], g = A[2];

	// unable to find an inverse, arithmetic breaks
	if (g > 1) return{ 0, 0, denom };

	ll slope = nom * inv;

	ll z = (slope*slope - p[0] - q[0]) % m;

	return{ z, (slope * (z - p[0]) + p[1]) % m, 1 };
}

/* Fast multiplication of a point by a constant */
vector<ll> ellipticMul(ll k, vector<ll> p, ll a, ll b, ll m) {
	vector<ll> r{ 0, 1, 0 };  // infinity

	while (k > 0) {
		// p is not a valid point on  curve, return it
		if (p[2] > 1) return p;

		if (k % 2 == 1) r = ellipticAdd(p, r, a, b, m);

		k = k / 2;

		p = ellipticAdd(p, p, a, b, m);
	}

	return r;
}

/* Lenstra elliptic-curve method */
ll lenstra(ll n, ll limit) {
	ll g = n;

	ll a, b;

	vector<ll> q(3);

	while (g == n) {
		// randomizes x and y
		q = { rand() % n, rand() % n, 1 };

		// randomizes curve coefficient a, computes b
		a = rand() % n;
		b = (q[1] * q[1] - q[0] * q[0] * q[0] - a * q[0]) % n;

		g = gcd(4 * a * a * a + 27 * b * b, n);  // singularity check
	}

	// if we got lucky, return lucky factor
	if (g > 1) return g;

	// computes limit!* p one factor at a time
	for (ll p : primes(limit)) {
		ll pp = p;

		while (pp < limit) {
			q = ellipticMul(p, q, a, b, n);

			// point at infinity
			if (q[2] != 1) return gcd(q[2], n);

			pp = p * pp;
		}
	}

	return -1;
}