#include "lnum_temp.h"

lnum::lnum(long long n)
{
	base = DEFAULT_BASE;

	// check for negatives
	if (n < 0)
	{
		sign = -1;
		n *= -1;
	}

	if (n > 0)
		sign = 1;

	if (n == 0)
	{
		sign = 0;
		digits = { 0 };
	}

	while (n > 0)
	{
		digits.push_back(n % base);
		n /= base;
	}
}

lnum::lnum(vector<int> N)
{
	for (size_t i = 0; i < N.size(); ++i)
		digits.push_back(N[i]);
	base = DEFAULT_BASE;
	sign = 1;
}

template<typename T>
lnum lnum::operator + (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New;
	// strip
	*this = strip(*this);
	N = strip(N);

	if (-N > *this && N.sign < 0)
	{
		New = (-N) + (-(*this));
		New = -New;
		return New;
	}

	if (-(*this) > N && sign < 0)
	{
		New = (-*this) + (-N);
		New = -New;
		return New;
	}

	// add zeros
	size_t n = max(exp(), N.exp());
	while (exp() != n)
		digits.push_back(0);
	while (N.exp() != n)
		N.digits.push_back(0);

	New.digits = { 0 };

	for (size_t i = 0; i < n; ++i)
	{
		size_t s = New.digits.back() + digits[i] * sign + N.digits[i] * N.sign;
		New.digits.back() = (s + 2 * base) % base;
		New.digits.push_back((s + 2 * base) / base - 2);
	}

	New.base = DEFAULT_BASE;
	New.sign = 1;

	New = strip(New);

	return New;
}

template<typename T>
lnum lnum::operator += (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New = *this + N;
	*this = New;
	return *this;
}

template<typename T>
lnum lnum::operator - (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return *this + (-N);
}

template<typename T>
lnum lnum::operator -= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New = *this - N;
	*this = New;
	return *this;
}

// Karatsuba
template<typename T>
lnum lnum::operator * (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	// strip
	*this = strip(*this);
	N = strip(N);

	size_t n = max(exp(), N.exp());

	// add zeros
	while (exp() != n)
		digits.push_back(0);
	while (N.exp() != n)
		N.digits.push_back(0);

	// base case
	if (n == 0)
	{
		lnum A(0);
		return A;
	}
	if (n == 1)
	{
		lnum A(digits[0] * N.digits[0]);
		A.sign = sign * N.sign;
		return A;
	}

	// recursive calls
	size_t m = n / 2;
	vector<size_t> u0 = {}, u1 = {}, v0 = {}, v1 = {};
	for (size_t i = 0; i < m; ++i)
	{
		u0.push_back(digits[i]);
		v0.push_back(N.digits[i]);
	}
	for (size_t i = m; i < n; ++i)
	{
		u1.push_back(digits[i]);
		v1.push_back(N.digits[i]);
	}

	lnum U0(u0), U1(u1), V0(v0), V1(v1);
	U0.sign = sign; U1.sign = sign; V0.sign = N.sign; V1.sign = N.sign;

	lnum M1 = U1 - U0, M2 = V0 - V1;

	lnum N1 = U1 * V1, N2 = M1 * M2, N3 = U0 * V0;

	lnum A = (N1 << (2 * m)) + (N1 << m) + (N2 << m) + (N3 << m) + N3;

	A.sign = sign * N.sign;
	A = strip(A);

	return A;
}

template<typename T>
lnum lnum::operator *= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New = *this * N;
	*this = New;
	return *this;
}

template<typename T>
lnum lnum::operator / (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New = *this;
	for (size_t i = exp() - 1; i > 0; --i)
	{
		size_t s = New.digits[i];
		New.digits[i] /= N;
		New.digits[i - 1] += base * (s - N * New.digits[i]);
	}
	New.digits[0] /= N;

	return New;
}

template<typename T>
lnum lnum::operator /= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	lnum New = *this / N;
	*this = New;
	return *this;
}

template<typename T>
bool lnum::operator < (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return (*this <= N) && (*this != N);
}

template<typename T>
bool lnum::operator <= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return *this == N || !(N >= *this);
}

template<typename T>
bool lnum::operator > (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return (*this >= N) && (*this != N);
}

template<typename T>
bool lnum::operator >= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	// strip
	*this = strip(*this);
	N = strip(N);

	// basic checks
	if (sign > N.sign)
		return true;
	if (sign < N.sign)
		return false;
	if (exp() > N.exp())
		return true;
	if (exp() < N.exp())
		return false;

	// per digit comparison
	for (size_t i = exp() - 1; i >= 0; --i)
	{
		if (digits[i] > N.digits[i])
			return true;
		if (digits[i] < N.digits[i])
			return false;
	}

	// equality case
	return true;
}

template<typename T>
bool lnum::operator == (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);

	*this = strip(*this);
	N = strip(N);

	// basic checks
	if (sign != N.sign)
		return false;
	if (exp() != N.exp())
		return false;

	// per digit comparison
	for (size_t i = 1; i <= exp(); ++i)
		if (digits[exp() - i] != N.digits[exp() - i])
			return false;

	// equality case
	return true;
}

template<typename T>
bool lnum::operator != (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return !(*this == M);
}

template<typename T>
lnum lnum::operator % (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	return (*this - (*this / N) * N);
}

template<typename T>
lnum lnum::operator %= (T M)
{
	lnum N = (typeid(lnum) == typeid(T)) ? M : lnum(M);
	*this -= (*this / N) * N;
	return *this;
}

lnum lnum::operator - ()
{
	lnum New = *this;
	New.sign *= -1;
	return New;
}

lnum lnum::operator << (int n)
{
	lnum New = *this;
	for (int i = 0; i < n; ++i)
		New.digits.insert(New.digits.begin(), 0);
	return New;
}

lnum lnum::operator <<= (int n)
{
	lnum New = *this << n;
	*this = New;
	return *this;
}

lnum lnum::operator >> (int n)
{
	lnum New = *this;
	for (int i = 0; i < n; ++i)
		New.digits.erase(New.digits.begin());
	return New;
}

lnum lnum::operator >>= (int n)
{
	lnum New = *this >> n;
	*this = New;
	return *this;
}

lnum::operator bool()
{
	return *this != 0;
}

lnum::operator string()
{
	lnum New = strip(*this);

	string s = "";
	for (size_t i = 0; i < New.exp(); ++i)
		s = (char)(New.digits[i] + 48) + s;
	if (New.sign == -1)
		s = "-" + s;

	return s;
}

lnum abs(lnum N)
{
	lnum New = N;
	New.sign = 1;
	return New;
}

lnum strip(lnum N)
{
	lnum New = N;
	while (New.exp() > 1 && New.digits.back() == 0)
		New.digits.pop_back();
	return New;
}

ostream& operator << (ostream& out, lnum N)
{
	out << (string)N;
	return out;
}