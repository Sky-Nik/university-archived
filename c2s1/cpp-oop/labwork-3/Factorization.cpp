#include "Factorization.h"

/* Sieve of Erathosphenes. Returns a vector of primes not excceeding n */
vector<ll> primes(ll n) {
	vector<bool> b(n + 1, true);

	vector<ll> ps;

	for (ll p = 2; p < n + 1; ++p) {
		if (b[p]) {
			ps.push_back(p);

			for (ll i = p; i < n + 1; i += p) b[i] = false;
		}
	}

	return ps;
}

/* Finds an inverse of a modulo b. Returns inverse, unused helper and gcd */
vector<ll> modInv(ll a, ll b) {
	if (b == 0) return{ 1, 0, a };

	ll q = a / b, r = a % b;

	vector<ll> I = modInv(b, r);

	ll x = I[0], y = I[1], g = I[2];

	return{ y, x - q * y, g };
}

/* Finds greatest common divisor of two numbers */
ll gcd(ll a, ll b) {
	if (b == 0) return a;

	return gcd(b, a % b);
}

/* Legender symbol of a modulo p */
ll legender(ll a, ll p) {
	return modPow(a, (p - 1) / 2, p);
}

/* Computes a^p % m */
ll modPow(ll a, ll p, ll m) {
	if (p == 0)	return 1;

	if (p % 2 == 0) return modPow(a * a % m, p / 2, m);

	return a * modPow(a * a % m, (p - 1) / 2, m) % m;
}

/* Fermat method of factoring */
ll fermat(ll n) {
	ll x = sqrt(n), y = 0;

	ll r = x * x - y * y - n;

	while (r != 0) {
		(r > 0) ? ++y : ++x;
		r = x * x - y * y - n;
	}

	return x - y;
}

/* Pollard_rho probabilistic method of factoring */
ll pollardRho(ll n, ll limit) {
	vector<ll> x = { rand() % n };

	for (ll i = 0; i < limit; ++i) x.push_back((x.back() * x.back() + 1) % n);

	for (ll k = 0; k < limit / 2; ++k)
		if (1 < gcd(x[2 * k] - x[k], n) && gcd(x[2 * k] - x[k], n) < n)
			return gcd(x[2 * k] - x[k], n);
}

/* Finds a generator of RRS of Z/nZ given a list P of prime factor of n - 1 */
ll generator(ll n, vector<ll> P) {
	while (true) {
	start:
		ll g = rand() % n;
	
		for (ll p : P) {
			ll b = modPow(g, (n - 1) / p, n);
		
			if (b == 1)
				goto start;
		}

		return g;
	}
}