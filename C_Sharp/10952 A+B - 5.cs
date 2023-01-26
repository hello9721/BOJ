using System;

while (true)
{
    string T = Console.ReadLine();

    if (T == "0 0")
    {
        break;
    }
    else
    {
        int a = int.Parse(T.Split(" ")[0]);
        int b = int.Parse(T.Split(" ")[1]);

        Console.WriteLine(a + b);
    }
}
