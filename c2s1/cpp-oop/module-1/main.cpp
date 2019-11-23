/*
    Colloquium 1
    Computation of log(cos(sin(acos(exp(x))))) by metaprogramming

    Created by Nikita Skybytskyi on 10/19/17
    Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include <cstdio>
#include <cmath>

#ifndef Sky_Nik
#define Sky_Nik 0.159090909

// useful shortenings for types
#define sci static const __int64 // sci is like SCIence
#define int __int64
#define dbl double

// PI ~ 355/113
#define PI_num 355
#define PI_den 113
#endif

/* These three classes compute e^(M/N) using Gorner's scheme to compute
Taylor series for exponent function with center at zero:

e^x = 1 + x + x^2/2 + x^3/6 + x^4/24 + ... =

    = 1 + x * (1 + x/2 + x^2/6 + x^3/24 + ...) =

    = 1 + x * (1 + x/2 * (1 + x/3 + x^2/12 + ...)) =

    = 1 + x    * (1 + x/2  * (1 + x/3  * (1 + x/4  * (...))))
      -----       -------     -------     -------     ---
      1st term    2nd term    3rd term    4th term    etc
*/

/* This class computes the above expression from i-th to j-th term */
template<int M, int N, int i, int j>
class __Exp {
public:
    sci num = N * i * __Exp<M, N, i + 1, j>::den + M * __Exp<M, N, i + 1, j>::num;
    sci den = N * i * __Exp<M, N, i + 1, j>::den;
};

/* Base case of the above class with i = j, i.e. only one term */
template<int M, int N, int i>
class __Exp<M, N, i, i> {
public:
    sci num = N * i + M;
    sci den = N * i;
};

/* Wrap-around of the above classes, more convenient as one doesn't have to write i = 1 all the time */
template<int M, int N, int j>
class Exp {
public:
    sci num = __Exp<M, N, 1, j>::num;
    sci den = __Exp<M, N, 1, j>::den;
};

/*
These three classes compute sin(M/N) using Gorner's scheme to compute
Taylor series for sine function with center at zero:

sin(x) = x - x^3/6 + x^5/120 - x^7/5040 + ... =

       = x * (1 - x^2/6 + x^4/120 - x^6/5040 + ...) =

       = x * (1 - x^2/(2*3) * (1 - x^2/(4*5) + x^4/(4*5*6*7) + ...))) =

       = x * (1 - x^2/(2*3) * (1 - x^2/(4*5) * (1 - x^2/(6*7) * (...)))) =
              -------------    -------------    -------------    ---
              1st term         2nd term         3rd term         etc
*/

/* This class computes the above expression from i-th to j-th term */
template<int M, int N, int i, int j>
class __Sin {
public:
    sci num = (2 * i) * (2 * i + 1) * N * N * __Sin<M, N, i + 1, j>::den - M * M * __Sin<M, N, i + 1, j>::num;
    sci den = (2 * i) * (2 * i + 1) * N * N * __Sin<M, N, i + 1, j>::den;
};

/* Base case of the above class with i = j, i.e. only one term */
template<int M, int N, int i>
class __Sin<M, N, i, i> {
public:
    sci num = N * N * (2 * i) * (2 * i + 1) - M * M;
    sci den = N * N * (2 * i) * (2 * i + 1);
};

/* Wrap-around of the above classes, more convenient as one doesn't have to write i = 1 all the time */
template<int M, int N, int j>
class Sin {
public:
    sci num = M * __Sin<M, N, 1, j>::num;
    sci den = N * __Sin<M, N, 1, j>::den;
};

/*
These three classes compute cos(M/N) using Gorner's scheme to compute
Taylor series for cosine function with center at zero:

cos(x) = 1 - x^2/2 + x^4/24 - x^6/720 + ... =

       = 1 - x^2/2 * (1 - x^2/12 + x^4/360 - ...) =

       = 1 - x^2/(1*2) * (1 - x^2/(3*4) * (1 - x^2/(5*6) * (...))) =
         -------------    -------------    -------------    ---
         1st term         2nd term         3rd term         etc
*/

/* This class computes the above expression from i-th to j-th term */
template<int M, int N, int i, int j>
class __Cos {
public:
    sci num = (2 * i - 1) * (2 * i) * N * N * __Cos<M, N, i + 1, j>::den - M * M * __Cos<M, N, i + 1, j>::num;
    sci den = (2 * i - 1) * (2 * i) * N * N * __Cos<M, N, i + 1, j>::den;
};

/* Base case of the above class with i = j, i.e. only one term */
template<int M, int N, int i>
class __Cos<M, N, i, i> {
public:
    sci num = N * N * (2 * i - 1) * (2 * i) - M * M;
    sci den = N * N * (2 * i - 1) * (2 * i);
};

/* Wrap-around of the above classes, more convenient as one doesn't have to write i = 1 all the time */
template<int M, int N, int j>
class Cos {
public:
    sci num = __Cos<M, N, 1, j>::num;
    sci den = __Cos<M, N, 1, j>::den;
};

/* Tangent function, computed as tan(x) = sin(x)/cos(x) */
template<int M, int N, int j>
class Tan {
public:
    sci num = Sin<M, N, j>::num * Cos<M, N, j>::den;
    sci den = Sin<M, N, j>::den * Cos<M, N, j>::num;
};

/*
These three classes compute ln(M/N) using Gorner's scheme to compute
Taylor series for logarithmic function with center at zero:

ln(1 + x) = x - x^2/2 + x^3/3 - x^4/4 + ... =

          = x * (1 - x/2 + x^2/3 - x^3/4 + ...) =

          = x * (1 - x * (1/2 - x/3 + x^2/4 - ...)) =

          = x * (1 - x * (1/2 - x * (1/3 - x/4 + ...))) =

          = x * (1 - x    * (1/2 - x  * (1/3 - x  * (...))))
                 -----       -------     -------     ---
                 1st term    2nd term    3rd term    etc
*/

/* This class computes the above expression from i-th to j-th term */
template<int M, int N, int i, int j>
class __Ln {
public:
    sci num = M * __Ln<M, N, i + 1, j>::den - M * __Ln<M, N, i + 1, j>::num * i;
    sci den = __Ln<M, N, i + 1, j>::den *N * i;
};

/* Base case of the above class with i = j, i.e. only one term */
template<int M, int N, int i>
class __Ln<M, N, i, i> {
public:
    sci num = M;
    sci den = N * i;
};

/* Wrap-around of the above classes, more convenient as one doesn't have to write i = 1 all the time */
template<int M, int N, int j>
class Ln {
public:
    sci num = __Ln<M - N, N, 1, j>::num;
    sci den = __Ln<M - N, N, 1, j>::den;
};

/*
These three classes compute arcsin(M / N) using Gorner's scheme to compute
Taylor series for arcsine function with center at zero

Unfortunately for you, I am a bit lazy to work through all this mess, so you will have to trust me upon the correctness of these classes
*/

/* This class computes the above expression from i-th to j-th term */
template<int M, int N, int i, int j>
class __Asin {
public:
    sci num = (2 * i + 1) * i * i * 4 * N * N * __Asin<M, N, i + 1, j>::den + (2 * i - 1) * (2 * i - 1) * 2 * i * M * M * __Asin<M, N, i + 1, j>::num;
    sci den = (2 * i + 1) * i * i * 4 * N * N * __Asin<M, N, i + 1, j>::den;
};

/* Base case of the above class with i = j, i.e. only one term */
template<int M, int N, int i>
class __Asin<M, N, i, i> {
public:
    sci num = (2 * i + 1) * i * i * 4 * N * N + (2 * i - 1) * (2 * i - 1) * 2 * i * M * M;
    sci den = (2 * i + 1) * i * i * 4 * N * N;
};

/* Wrap-around of the above classes, more convenient as one doesn't have to write i = 1 all the time */
template<int M, int N, int j>
class Asin {
public:
    sci num = M * __Asin<M, N, 1, j>::num;
    sci den = N * __Asin<M, N, 1, j>::den;
};

/* This class computes arccosine usin Taylor series of arcsine and releationship between them: arccos(x) = PI/2 - arcsin(x) */
template<int M, int N, int j>
class Acos {
public:
    sci num = PI_num * Asin<M, N, j>::den - PI_den * 2 * Asin<M, N, j>::num;
    sci den = PI_den * 2 * Asin<M, N, j>::den;
};

/* This class is created purely for the needs of colloquium, remove it from production release. It computes ln(cos(sin(acos(exp(M/N))))) */
template<int M, int N>
class Composition {
public:
    sci num1 = Exp<M, N, 4>::num, den1 = Exp<M, N, 4>::den;
    sci num2 = Acos<num1, den1, 2>::num / 1e15, den2 = Acos<num1, den1, 2>::den / 1e15;
    sci num3 = Sin<num2, den2, 2>::num / 1e15, den3 = Sin<num2, den2, 2>::den / 1e15;
    sci num4 = Cos<num3, den3, 2>::num / 1e11, den4 = Cos<num3, den3, 2>::den / 1e11;
    sci num = Ln<num4, den4, 3>::num / 1e9, den = Ln<num4, den4, 3>::den / 1e9;
};

/* Driver program comparing the results of both ways to compute the above */
void main() {
    sci M = -1, N = 2;
    dbl x = (dbl)M / N;

    sci num = Composition<M, N>::num, den = Composition<M, N>::den;
    dbl y = (dbl)num / den;

    dbl err = (log(cos(sin(acos(exp(x))))) - y) / y;

    printf("Result by standard functions:\t%f\nResult by metaprogramming:\t%f\n\nError: %f\n", log(cos(sin(acos(exp(x))))), y, err);
}
