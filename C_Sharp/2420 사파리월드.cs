using System;

string nm = Console.ReadLine();

long n = long.Parse(nm.Split(" ")[0]);
long m = long.Parse(nm.Split(" ")[1]);

if (n < 0 && m > 0)
{
    Console.WriteLine(m - n);
}
else if (m < 0 && n > 0)
{
    Console.WriteLine(n - m);
}
else
{
    if (n - m > 0)
    {
        Console.WriteLine(n - m);
    }
    else
    {
        Console.WriteLine(m - n);
    }
}
