using System;

string input = Console.ReadLine();

long a = long.Parse(input.Split(" ")[0]);
long b = long.Parse(input.Split(" ")[1]);
long c = long.Parse(input.Split(" ")[2]);
// 10의 12승의 숫자까지 나오기에 int로는 다 담아낼수가 없다.
// 긴 숫자에 사용하는 long 자료형을 사용.

Console.WriteLine(a + b + c);
