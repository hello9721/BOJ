using System;

int n = int.Parse(Console.ReadLine());
int a = 1;

for (int i = n; i > 0; i--)
{
    a = a * i;
}
Console.WriteLine(a);
