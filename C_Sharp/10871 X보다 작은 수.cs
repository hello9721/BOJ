using System;
using System.Text;

string nx = Console.ReadLine();

int n = int.Parse(nx.Split(" ")[0]);
int x = int.Parse(nx.Split(" ")[1]);

List<int> a = new List<int>();
StringBuilder answer = new StringBuilder();

string li = Console.ReadLine();

for (int i = 0; i < n; i++)
{
    a.Add(int.Parse(li.Split(" ")[i]));
}

for (int i = 0; i < n; i++)
{
    if (a[i] < x)
    {
        answer.Append(a[i] + " ");
    }
}

Console.WriteLine(answer.ToString());
