#include <iostream>
#include <ctime>

#include "Factorization.h"
#include "DiscreteLog.h"
#include "Lenstra.h"
#include "QS.h"

int main() {
	ll n = 941 * 937;

	cout << "Fermat : " << fermat(n) << '\n';

	cout << "Pollard : " << pollardRho(n, 10) << '\n';

	cout << "Generator : " << generator(139, { 2, 3, 23 }) << '\n';

	// cout << "QS : " << quadraticSieve(n, 1000) << '\n'; // fix

	cout << "Lenstra : " << lenstra(n, 1000) << '\n';

	ll g = 3, b = 11; n = 17;

	cout << "Primitive : " << primitiveAlgorithm(g, b, n) << '\n';

	cout << "Shanks : " << shanksAlgorithm(g, b, n) << '\n';

	// Strangely not working
	cout << "Pollard : " << pollardRho(g, b, n, 1000) << '\n';

	cout << "Index : " << index(g, b, n) << '\n';

	cout << "Pohlig-Hellman : " << pohligHellman(g, b, n) << '\n';

	return 0;
}