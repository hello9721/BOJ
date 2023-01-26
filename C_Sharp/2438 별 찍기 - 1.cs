using System;
using System.Text;

int n = int.Parse(Console.ReadLine());

for (int i = 1; i <= n; i++)
{
    StringBuilder star = new StringBuilder();
    for (int j = 1; j <= i; j++)
    {
        star.Append("*");
    }
    Console.WriteLine(star.ToString());
}
