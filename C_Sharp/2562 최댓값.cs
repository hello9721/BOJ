List<int> list = new List<int>();

for (int i = 0;i < 9; i++)
{

    int temp = int.Parse(Console.ReadLine());
    list.Add(temp);

}

int max = list.Max();
int idx = list.FindIndex(x => x == max);

Console.WriteLine(max);
Console.WriteLine(idx+1);