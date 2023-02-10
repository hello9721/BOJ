string[] phrase = Console.ReadLine().Split(" ");

List<string> a = new List<string>();

foreach (string s in phrase)
{

    if (s != "")
    {
        
        a.Add(s);
    
    }

}

Console.WriteLine(a.Count);