using System;
using System.Text; // StringBuilder 사용을 위해

// Console.WriteLine은 시간이 많이 걸리는 작업으로 이를 반복적으로 여러번 호출하면
// 시간이 오래 걸리게 되고, 시간 초과가 된다.
// Console.WriteLine을 최소한으로 호출하기 위해 StringBuilder 사용하는 것이 효율적이다.
// int n = int.Parse(Console.ReadLine());
// for (int i = 1; i <= n; i++)
// {
//     Console.WriteLine(i);
// }

int n = int.Parse(Console.ReadLine());
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= n; i++)
{
    sb.Append(i + "\n");
}

Console.WriteLine(sb.ToString());
