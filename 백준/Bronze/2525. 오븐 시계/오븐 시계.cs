//ai 오븐
using System;

namespace Exam2525
{
    class Program
    {
        static void Main(string[] args)
        {
            String timeStr = Console.ReadLine(); // 한줄에 공백으로 구분해서 시간과 분을 입력 받음
            String[] time = timeStr.Split(' '); // 입력 받은 시간을 공백을 기준으로 시간과 분으로 나눔
            int t = Convert.ToInt32(Console.ReadLine()); // 몇분 돌릴껀지 설정
            int h = Convert.ToInt32(time[0]); // 시간
            int m = Convert.ToInt32(time[1]); // 분
            m += t;
            h = ((m / 60) + h) % 24;
            m %= 60;
            Console.WriteLine($"{h} {m}");
        }
    }
}
