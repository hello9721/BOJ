int n = int.Parse(Console.ReadLine());

for (int i = 0;i < n; i++)
{

    string temp = Console.ReadLine();
    string[] split = temp.Split(' ');

    int m = int.Parse(split[0]);

    string output = "";
    foreach (char item in split[1])
    {

        string a = new string(item, m);
        output += a;

    }

    Console.WriteLine(output);

}