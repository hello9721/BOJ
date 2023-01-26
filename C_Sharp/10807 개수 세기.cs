using System;

int n = int.Parse(Console.ReadLine());
string nst = Console.ReadLine();
int v = int.Parse(Console.ReadLine());

List<int> nlst = new List<int>();
int count = 0;

for (int i = 0; i < n; i++)
{
    nlst.Add(int.Parse(nst.Split(" ")[i]));
}

for (int i = 0; i < n; i++)
{
    if (nlst[i] == v)
    {
        count++;
    }
}

Console.WriteLine(count);
