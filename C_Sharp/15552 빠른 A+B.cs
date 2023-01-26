using System;
using System.Text;

int t = int.Parse(Console.ReadLine());
StringBuilder sb = new StringBuilder();

for (int i = 0; i < t; i++)
{
    string s = Console.ReadLine();

    int a = int.Parse(s.Split(" ")[0]);
    int b = int.Parse(s.Split(" ")[1]);

    sb.Append(a + b + "\n");
}

Console.WriteLine(sb.ToString());
