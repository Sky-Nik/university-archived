/*
	Source.cpp
	OOP lab 2

	Created by Nikita Skybytskyi on 9/14/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include "lnum.h"
#include "lreal.h"
#include "is_prime.h"

void main()
{
	cout << "Testing lnum:\n";

	lnum A = lnum(100), B = lnum(10);
	cout << "A = " << A << "\nB = " << B << '\n';

	lnum C = A + B;
	cout << A << " + " << B << " = " << C << '\n';

	lnum D = A - B;
	cout << A << " - " << B << " = " << D << '\n';

	lnum E = A * B;
	cout << A << " * " << B << " = " << E << '\n';

	lnum F = A / B;
	cout << A << " / " << B << " = " << F << '\n';
	
	cout << "\nTesting Toom-Cook:\n";
	cout << A << " * " << B << " = " << A.Toom_Cook(B, 3) << '\n';

	cout << "\nTesting Strassen:\n";
	cout << A << " * " << B << " = " << A.Strassen(B) << '\n';

	cout << "\nTesting Schonhage:\n";
	cout << A << " * " << B << " = " << A.Schonhage(B) << '\n';

	cout << "\nTesting lreal:\n";

	lreal M({ 1, 0 }, 1), N({ 1, 1, 0 }, 2);
	cout << "M = " << M << "\nN = " << N << '\n';

	lreal K = M + N;
	cout << M << " + " << N << " = " << K << '\n';

	lreal L = M - N;
	cout << M << " - " << N << " = " << L << '\n';

	lreal P = M * N;
	cout << M << " * " << N << " = " << P << '\n';

	lreal Q = N.inverse(8);
	cout << "1 / " << N << " = " << Q << '\n';

	lreal S = M / N;
	cout << M << " / " << N << " = " << S << '\n';

	cout << "\n\nTesting is_prime\n";
	cout << "some small numbers : \n";
	ll i = 5;
	for (; i < 20; i += 2)
	{
		cout << "p = " << i << "\n";
		cout << "Soloway-Strassen : " << (Soloway_Strassen(i, 10) ? ("prime") : ("composite")) << "\n";
		cout << "Lehmann          : " << (Lehmann(i, 10) ? ("prime") : ("composite")) << "\n";
		cout << "Rabin-Miller     : " << (Rabin_Miller(i, 10) ? ("prime") : ("composite")) << "\n\n";
	}
	
	cout << "Mersenne prime : \n";
	i = (1 << 19) - 1;
	cout << "p = " << i << "\n";
	cout << "Soloway-Strassen : " << (Soloway_Strassen(i, 10) ? ("prime") : ("composite")) << "\n";
	cout << "Lehmann          : " << (Lehmann(i, 10) ? ("prime") : ("composite")) << "\n";
	cout << "Rabin-Miller     : " << (Rabin_Miller(i, 10) ? ("prime") : ("composite")) << "\n\n";
	
	cout << "some large numbers : \n";
	for (i = (1 << 30) - 5; i < (1 << 30); i += 2)
	{
		cout << "p = " << i << "\n";
		cout << "Soloway-Strassen : " << (Soloway_Strassen(i, 10) ? ("prime") : ("composite")) << "\n";
		cout << "Lehmann          : " << (Lehmann(i, 10) ? ("prime") : ("composite")) << "\n";
		cout << "Rabin-Miller     : " << (Rabin_Miller(i, 10) ? ("prime") : ("composite")) << "\n\n";
	}

	// TODO: fix template methods (learn about type comparison)

	// TODO: write functions o, phi, AKS in is_prime.cpp

	// TODO: add FAST computation of Cs in Schonhage
}