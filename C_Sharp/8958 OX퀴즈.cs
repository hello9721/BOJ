int n = int.Parse(Console.ReadLine());

for(int i = 0; i < n; i++)
{
	int score = 0;

    string[] temp = Console.ReadLine().Split("X");
	foreach (string item in temp)
	{

		if(item != "")
		{

			for (int j = 1; j <= item.Length; j++)
			{

				score += j;

			}

		}

	}

	Console.WriteLine(score);

}