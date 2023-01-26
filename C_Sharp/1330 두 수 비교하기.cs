using System;

string n = Console.ReadLine();

int a = int.Parse(n.Split(" ")[0]);
int b = int.Parse(n.Split(" ")[1]);

if (a > b)
{
    Console.WriteLine(">");
}
else if (b > a)
{
    Console.WriteLine("<");
}
else if (a == b)
{
    Console.WriteLine("==");
}
