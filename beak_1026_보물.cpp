#include <iostream>//cout, cin
#include <algorithm> //sort
#include <vector>//vecotr

using namespace std;
vector<int> a;
vector<int> b;
int n;
int main(void)
{
	int num;
	cin >> n;
	//�Է� 1
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		a.push_back(num);//stack�������� ����
	}
	//�Է� 2
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		b.push_back(num);
	}
	//�Է� 3

	sort(a.begin(), a.end());
	sort(b.begin(), b.end(), greater<>());
	int res = 0;
	for (int i = 0; i < n; i++) {
		res += a[i] * b[i];
	}
	cout << res;

	return 0;

}