//
//
//  Generated by StarUML(tm) C++ Add-In
//
//  @ Project : Untitled
//  @ File Name : TUniversity.h
//  @ Date : 05.03.2018
//  @ Author : 
//
//


#if !defined(_TUNIVERSITY_H)
#define _TUNIVERSITY_H

#include "TStudent.h"

class TUniversity {
public:
	TUniversity(string univName);
	void printData();
	void setData(string name, int age);
private:
	TStudent student;
	string name;
};

#endif  //_TUNIVERSITY_H
