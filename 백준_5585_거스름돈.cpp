//백준 5585 거스름돈
#include <iostream>
using namespace std;

int money[] = { 500, 100, 50, 10, 5, 1 };

int main(void) {
	int n;
	cin >> n;
	int rtn;
	
	rtn = 1000 - n;
	//cout << rsn;
	int rst;

	for (int i = 0; i < 6; i++)
	{
		rst += rtn / money[i];
		rtn = rtn % money[i];
		if (rtn == 0)
		{
			break;
		}

	}
	cout << rst;
	return 0;
}