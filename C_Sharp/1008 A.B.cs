using System;

string input = Console.ReadLine();

double a = double.Parse(input.Split(" ")[0]);   // 소수점까지 표시해주기 위해
double b = double.Parse(input.Split(" ")[1]);   // double 사용

Console.WriteLine(a / b);
