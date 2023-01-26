using System;

int year = int.Parse(Console.ReadLine());


if (year % 400 == 0)
{
    Console.WriteLine(1);
}
else if (year % 4 == 0 && year % 100 != 0)
{
    Console.WriteLine(1);
}
else
{
    Console.WriteLine(0);
}
