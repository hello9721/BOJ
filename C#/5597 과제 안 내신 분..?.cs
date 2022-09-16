using System;

List<int> lst = new List<int>();

for (int i = 1; i <= 30; i++)
{
    lst.Add(i);
}

for (int i = 0; i < 28; i++)
{
    int n = int.Parse(Console.ReadLine());
    lst.Remove(n);
}

lst.Sort();
Console.WriteLine(lst[0]);
Console.WriteLine(lst[1]);
