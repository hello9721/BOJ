using System;

string input = Console.ReadLine();

int a = int.Parse(input.Split(" ")[0]);
int b = int.Parse(input.Split(" ")[1]);
double c = a;
double d = b;

Console.WriteLine(a + b);
Console.WriteLine(a - b);
Console.WriteLine(a * b);
Console.WriteLine(Math.Truncate(c / d));
Console.WriteLine(a % b);