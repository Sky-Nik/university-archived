/*
    AOS lab 1

    Created by Nikita Skybytskyi on 9/27/17
    Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#include <windows.h>
#include <iostream>
#include <string>
#include <time.h>

const int ITERATIONS = 10000000;
const int OPERATIONS = 10;

double max;

template<typename T>
double empty() {
    T a1 = 11, a2 = 222, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;
    double t = GetTickCount();
    
    for (long i = 1; i < ITERATIONS; i++)
        a1 = 11 % i + 1, a2 = 222 % i + 1, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;

    return GetTickCount() - t;
}

template<typename T>
double addition() {
    T a1 = 11, a2 = 222, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;
    double t = GetTickCount();

    for (long i = 1; i < ITERATIONS; i++) {
        a1 = 11 % i + 1, a2 = 222 % i + 1, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;

        a1 = a0 + a2; a2 = a1 + a3; a3 = a2 + a4; a4 = a3 + a5; a5 = a4 + a6;
        a6 = a5 + a7; a7 = a6 + a8; a8 = a7 + a9; a9 = a8 + a0; a0 = a9 + a1;
    }

    return GetTickCount() - t;
}

template<typename T>
double subtraction() {
    T a1 = 11, a2 = 222, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;
    double t = GetTickCount();
    
    for (long i = 1; i < ITERATIONS; i++) {
        a1 = 11 % i + 1, a2 = 222 % i + 1, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;

        a1 = a0 - a2; a2 = a1 - a3; a3 = a2 - a4; a4 = a3 - a5; a5 = a4 - a6;
        a6 = a5 - a7; a7 = a6 - a8; a8 = a7 - a9; a9 = a8 - a0; a0 = a9 - a1;
    }

    return GetTickCount() - t;
}

template<typename T>
double multiplication() {
    T a1 = 11, a2 = 222, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;

    double t = GetTickCount();

    for (int i = 1; i < ITERATIONS; i++) {
        a1 = 11 % i + 1, a2 = 222 % i + 1, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;

        a1 = a0 * a2; a2 = a1 * a2; a3 = a2 * a3; a4 = a3 * a4; a5 = a4 * a5;
        a6 = a5 * a6; a7 = a6 * a7; a8 = a7 * a8; a9 = a8 * a9; a0 = a9 * a0;
    }

    return GetTickCount() - t;
}

template<typename T>
long division() {
    T a1 = 11, a2 = 222, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;
    long t = GetTickCount();
    
    for (long i = 1; i < ITERATIONS; i++) {
        a1 = 11 % i + 1, a2 = 222 % i + 1, a3 = 33333, a4 = 444444, a5 = 555555, a6 = 66666, a7 = 7777, a8 = 88888, a9 = 999, a0 = 10101;
        
        a4 = a2 / a0; a5 = a3 / a1; a4 = a5 / a1; a3 = a6 / a2; a3 = a8 / a1;
        a1 = a0 / a2; a0 = a9 / a1; a7 = a6 / a1; a8 = a7 / a1; a6 = a8 / a2;
    }

    return GetTickCount() - t;
}

template<typename T>
void count(double arr[4][2]) {
    double t = empty<T>();
    arr[0][0] = ITERATIONS * OPERATIONS / ((addition<T>() - t) / CLOCKS_PER_SEC);
    arr[1][0] = ITERATIONS * OPERATIONS / ((subtraction<T>() - t) / CLOCKS_PER_SEC);
    arr[2][0] = ITERATIONS * OPERATIONS / ((multiplication<T>() - t) / CLOCKS_PER_SEC);
    arr[3][0] = ITERATIONS * OPERATIONS / ((division<T>() - t) / CLOCKS_PER_SEC);
}

void percents(double arr[4][2]) {
    for (long i = 0; i < 4; ++i)
        arr[i][1] = arr[i][0] / max * 100;
}

double maximum(double arr[4][2]) {
    double max = arr[0][0];

    for (int i = 1; i < 4; ++i)
        if (arr[i][0] > max)
            max = arr[i][0];

    return max;
}

void print(std::string s, double arr[4][2]) {
    char ops[4] = { '+', '-', '*', '/' };

    for (long i = 0; i < 4; ++i) {
        printf("%c  %s  %e   ", ops[i], s.c_str(), arr[i][0]);

        for (int j = 0; j < (int)arr[i][1] * 30 / 100; j++)
            printf("X");

        for (int j = (int)arr[i][1] * 30 / 100; j < 30; j++)
            printf(" ");

        printf("  %3d%%\n", (int)arr[i][1]);
    }

    printf("\n");
}

int main() {
    double ints[4][2];
    count<int>(ints);

    double longs[4][2];
    count<long>(longs);

    double chars[4][2];
    count<char>(chars);

    double floats[4][2];
    count<float>(floats);

    double doubles[4][2];
    count<double>(doubles);

    max = max(maximum(ints), max(maximum(chars), max(maximum(floats), max(maximum(longs), maximum(doubles)))));

    percents(ints);
    percents(longs);
    percents(chars);
    percents(floats);
    percents(doubles);

    print("int   ", ints);
    print("long  ", longs);
    print("char  ", chars);

    print("float ", floats);
    print("double", doubles);

    system("pause");
    return 0;
}
