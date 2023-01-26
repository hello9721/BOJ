using System;
using System.Text;

int n = int.Parse(Console.ReadLine());

StringBuilder sb = new StringBuilder();
for (int i = n; i > 0; i--)
{
    sb.Append(i + "\n");
}

Console.WriteLine(sb.ToString());
