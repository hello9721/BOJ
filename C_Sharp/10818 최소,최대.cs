string a = Console.ReadLine();

string[] temp = Console.ReadLine().Split(" ");
List<int> list = new List<int>();

foreach (string item in temp)
{

    list.Add(int.Parse(item));

}

Console.WriteLine(list.Min().ToString() + " " + list.Max().ToString());