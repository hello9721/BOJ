using System;

string input = Console.ReadLine(); // 입력값 받기

int strsp1 = int.Parse(input.Split(' ')[0]);
int strsp2 = int.Parse(input.Split(' ')[1]);

// 입력 값을 공백 기준으로 나눠 각각 Parse함수를 통해 int로 변환
// 첫번째를 strsp1에, 두번째를 strsp2에.

Console.WriteLine(strsp1 - strsp2); // 둘의 뺄셈을 출력
