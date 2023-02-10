string a = Console.ReadLine();
string num= Console.ReadLine();

List<int> list = new List<int>();

foreach (char item in num)
{

    list.Add(int.Parse(item.ToString()));

}

Console.WriteLine(list.Sum());