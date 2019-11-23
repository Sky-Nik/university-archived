#include "lnum.h"

// Computes z such that |z - 1 / D| < (1 >> p)

lnum lnum::inverse(int p)
{
	lnum X = lnum(48 / 17 - 32 / 17 * *this);
	for (int i = 0; i <= log2((p + 1.0) / log2(17)); ++i)
	{
		X = X * (lnum(2) - *this * X);
	}
	return X;
}