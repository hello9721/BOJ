using System;

while (true)
{
    string s = Console.ReadLine();

    if (s == null) { break; }
    // 아무것도 입력이 되지 않는 다면 break;

    int a = int.Parse(s.Split(" ")[0]);
    int b = int.Parse(s.Split(" ")[1]);

    Console.WriteLine(a + b);
}
