using System;

string input = Console.ReadLine();

int a = int.Parse(input.Split(" ")[0]);
int b = int.Parse(input.Split(" ")[1]);
    //double c = a;   // 작은 숫자 자료형은 큰 숫자 자료형으로 자동으로 바꿀수 있다.
    //double d = b;   // byte < short < int < long < float < double

Console.WriteLine(a + b);
Console.WriteLine(a - b);
Console.WriteLine(a * b);
Console.WriteLine(a / b);
// int는 정수형이기 때문에 자동으로 몫만 반환한다.

    // Console.WriteLine(Math.Truncate(c/d));
    // 입력값은 double 이어야하고, 나눗셈을 Math.Truncate에 넣는다.
Console.WriteLine(a % b);
