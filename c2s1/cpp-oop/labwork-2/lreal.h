/*
	lreal.h
	OOP lab 2

	Created by Nikita Skybytskyi on 9/26/17
	Copyright © 2017 Nikita Skybytskyi. All rights reserved.
*/

#pragma once
#include "lnum.h"

/*
Class modelling long real signed number R.

Inherits from lnum, maintaining most of its features yet bringing calucation of an inverse
*/
class lreal :
	public lnum
{
	int decimal_point;
public:
	friend class lnum;

	lreal(lnum);
	lreal(vector<int>, int);

protected:
	friend lreal strip(lreal);

public:
	lreal operator + (lreal);
	lreal operator - (lreal);
	lreal operator * (lreal);
	lreal operator << (int);
	lreal operator >> (int);
	lreal operator / (lreal);

	lreal inverse(int);

	operator string();

	friend ostream& operator << (ostream&, lreal);

	~lreal() = default;
};