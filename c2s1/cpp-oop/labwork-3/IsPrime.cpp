#include "IsPrime.h"

bool TryDivisors(ll n)
{
	for (int d = 2; d <= sqrt(n); ++d)
		if (n % d == 0)
			return false;

	return true;
}

//bool TryDivisors_optimised(ll n)
//{
//	if (n % 2 == 0 || n % 3 == 0)
//		return false;
//
//	for (int j = 1; 5 + 6 * j <= sqrt(n); ++j)
//		if (n % (1 + 6 * j) == 0 || n % (5 + 6 * j) == 0)
//			return false;
//
//	return true;
//}

vector<ll> EratosphenSieve(ll N)
{
	vector<bool> Table(N + 1, true);

	for (ll i = 2; i <= sqrt(N); ++i)
		for (ll j = 2; j <= N / i; ++j)
			Table[i * j] = false;

	vector<ll> Ans = {};

	for (ll i = 2; i <= N; ++i)
		if (Table[i])
			Ans.push_back(i);

	return Ans;
}

ll modpow(ll a, ll pow, ll mod)
{
	ll ans = 1;
	a = a % mod;

	while (pow > 0)
	{
		if (pow % 2 != 0)
		{
			ans = a * ans % mod;
			--pow;
		}

		pow >>= 1;
		a = a * a % mod;
	}

	return ans;
}

bool Fermat_is_prime(ll n, ll witnesses)
{
	for (ll i = 0; i < witnesses; ++i)
	{
		ll a = rand() % n;
		if (modpow(a, n, n) != (a % n))
			return false;
	}
	return true;
}

bool strictPseudoPrimality(ll n)
{
	ll m = n - 1;
	ll s = 0;

	while (m % 2 == 0)
	{
		m >>= 1;
		++s;
	}

	ll d = m;
	vector<ll> a = { 2, 3, 5, 7 };

	if (n == 2 || n == 3 || n == 5 || n == 7)
		return true;

	for (ll i = 0; i < 4; ++i)
	{
		if (gcd(a[i], n) != 1)
			return false;

		ll r = 0;

		for (; r <= s; ++r)
			if (modpow(a[i], d * (1 << r), n) == 1)
				break;

		if (r == s + 1)
			return false;
	}

	if (n == 3215031751)
		return false;

	return true;
}

bool is_Fermat_prime(ll k)
{
	if (k == 0)
		return true;

	ll n = (1 << (1 << k)) + 1;

	return (modpow(3, (n - 1) / 2, n) == n - 1);
}

bool is_Mersenne_prime(ll q) {
	if (q == 2)
		return true;
	
	ll n = (1 << q) - 1;

	vector<ll> L{ 4 };

	for (int j = 0; j + 1 < q - 1; ++j)
		L.push_back(((L[j] * L[j] - 2) % n + n) % n);

	return (L.back() == 0);
}

bool Fermat_Mersenne(ll p)
{
	ll M_p = (1 << p) - 1;
	ll F_p = (1 << (1 << p)) + 1;
	return (modpow(M_p, (F_p - 1) / 2, F_p) == F_p - 1);
}

bool N_minus_1(ll n, vector<ll> P)
{
	// fix
	for (ll i = 0; i < P.size(); ++i)
	{
		ll a_i = 2;
		
		for (; a_i < n; ++a_i)
			if (modpow(a_i, (n - 1) / P[i], n) != 1 &&
				modpow(a_i, n - 1, n) == 1)
				break;
	
		if (a_i == n)
			return false;
	}

	return true;
}

//======================================================

ll generator(ll n)
{
	ll b = 1;
	while (b == 1)
	{
		ll g = rand() % n;

	}
	return 0;
}

bool Konyagin_Pomerance(ll n)
{
	vector<ll> P = EratosphenSieve(log(n) * log(n) + 1);
	vector<ll> F = { 0 , 1 };
	for (ll a = 2; a <= log(n) * log(n) + 1; ++a)
	{
		if (find(P.begin(), P.end(), a) == P.end())
		{
			F.push_back(F.back());
			goto step6;
		}
		else
		{
			if (modpow(a, F.back(), n) == 1)
			{
				F.push_back(F.back());
				goto step6;
			}
			else
			{
				if (modpow(a, n - 1, n) != 1)
					return false;
			}
			// TODO
		}
	}
step6:
	return true;
}

/*bool Lenstra(ll n)
{
step1:
	// TODO: change for larger n (currently n <= 10^22)
	vector<ll> p = { 2, 3, 5, 7 };
	vector<ll> q = { 3, 7, 11, 31, 43, 71, 211 };

step2:
	for (size_t i = 0; i < p.size(); ++i)
		if (n == p[i])
			return true;

	for (size_t j = 0; j < q.size(); ++j)
		if (n == q[j])
			return true;

	ll prod = 1;

	for (size_t i = 0; i < p.size(); ++i)
		prod *= p[i];

	for (size_t j = 0; j < q.size(); ++j)
		prod *= q[j];

	if (gcd(prod, n) != 1)
		return false;

step3:
	for (size_t i = 0; i < p.size(); ++i)
	{
		for (size_t j = 0; j < q.size(); ++j)
		{
			if (q[j] % p[i] == 1)
			{
				ll c_q = generator(q[j]);

				complex<double> nu_xi_p_q = 0;

				complex<double> dzeta_p = exp(2 * PI * complex<double>(1, 0) / (double)p[i]);

				for (ll x = 2; x < q[j] - 1; ++x)
				{
					ll ind_q_x = 1;

					ll prod = c_q;

					while (prod != x)
					{
						prod = (prod * c_q) % q[j];
						++ind_q_x;
					}

					nu_xi_p_q += pow(dzeta_p, ind_q_x);
				}
			}
		}
	}

step4:
	return 0;
}*/