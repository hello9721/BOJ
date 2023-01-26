using System;
using System.Text;

string nm = Console.ReadLine();

int n = int.Parse(nm.Split(" ")[0]);
int m = int.Parse(nm.Split(" ")[1]);

List<string> A = new List<string>();
List<string> B = new List<string>();
StringBuilder C = new StringBuilder();

for (int i = 0; i < n; i++)
{
    A.Add(Console.ReadLine());
}
for (int i = 0; i < n; i++)
{
    B.Add(Console.ReadLine());
}

for (int i = 0; i < n; i++)
{
    for (int j = 0; j < m; j++)
    {
        int a = int.Parse(A[i].Split(" ")[j]);
        int b = int.Parse(B[i].Split(" ")[j]);

        C.Append(a + b + " ");
    }
    Console.WriteLine(C.ToString());
    C.Clear();
}
