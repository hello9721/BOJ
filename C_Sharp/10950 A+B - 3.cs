using System;

int T = int.Parse(Console.ReadLine());

for (int i = 0; i < T; i++)
{
    string A = Console.ReadLine();
    int a = int.Parse(A.Split(" ")[0]);
    int b = int.Parse(A.Split(" ")[1]);

    Console.WriteLine(a + b);
}
